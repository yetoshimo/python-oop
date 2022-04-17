from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.test_student = Student("student_name")
        self.test2_student = Student("student2_name", {"course_name": ["course_note_1"]})

    def test_student_init_with_empty_courses(self):
        self.assertEqual("student_name", self.test_student.name)
        self.assertEqual({}, self.test_student.courses)

    def test_student_init_with_courses(self):
        self.assertEqual({"course_name": ["course_note_1"]}, self.test2_student.courses)

    def test_student_enroll_existing_course_updates_notes(self):
        self.assertEqual("Course already added. Notes have been updated.",
                         self.test2_student.enroll("course_name", ["course_note_2"]))
        self.assertEqual({"course_name": ["course_note_1", "course_note_2"]}, self.test2_student.courses)

    def test_student_enroll_add_course_notes_option_capital_y(self):
        self.assertEqual("Course and course notes have been added.",
                         self.test_student.enroll("course_name_2", "course2_note", "Y"))

        self.assertEqual({"course_name_2": "course2_note"},
                         self.test_student.courses)

    def test_student_enroll_add_course_notes_option_empty(self):
        self.assertEqual("Course and course notes have been added.",
                         self.test_student.enroll("course_name_2", "course2_note"))

        self.assertEqual({"course_name_2": "course2_note"},
                         self.test_student.courses)

    def test_student_enroll_add_course_notes_option_capital_n(self):
        self.assertEqual("Course has been added.", self.test_student.enroll("course_name_2", "", "N"))

        self.assertEqual({"course_name_2": []},
                         self.test_student.courses)

    def test_student_add_notes(self):
        self.assertEqual("Notes have been updated", self.test2_student.add_notes("course_name", "course_note_2"))

        self.assertEqual({"course_name": ["course_note_1", "course_note_2"]}, self.test2_student.courses)

    def test_student_add_notes_course_does_not_exist_expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.test2_student.add_notes("course_name_2", "course_note_2")

        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

    def test_student_leave_course(self):
        self.assertEqual("Course has been removed", self.test2_student.leave_course("course_name"))

        with self.assertRaises(Exception) as context:
            self.test2_student.leave_course("course_name")

        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))


if __name__ == "__main__":
    main()
