import unittest
from IA_Testing_Lab.test_worker import Worker


class WorkerTests(unittest.TestCase):
    name = "Test Worker"
    salary = 1000
    energy = 3

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_worker_initialized_with_correct_args(self):
        """Test if the worker is initialized with correct name, salary and energy"""

        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)

    def test_worker_energy_is_incremented_after_rest(self):
        """Test if the worker's energy is incremented after the rest method is called"""

        self.worker.rest()

        self.assertEqual(self.energy + 1, self.worker.energy)

    def test_worker_work_with_negative_or_zero_energy_raises_error(self):
        """Test if an error is raised if the worker tries to work with negative energy or equal to 0"""
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_work_when_energy_is_above_zero_salary_is_increased_after_work(self):
        """Test if the worker's money is increased by his salary correctly after the work method is called"""
        self.worker.work()

        self.assertEqual(self.salary, self.worker.money)

    def test_worker_work_energy_is_decreased_after_work(self):
        """Test if the worker's energy is decreased after the work method is called"""
        self.worker.work()

        self.assertEqual(self.energy - 1, self.worker.energy)

    def test_worker_get_info_string(self):
        """Test if the get_info method returns the proper string with correct values"""
        expected_get_info = f'{self.name} has saved 0 money.'
        actual_get_info = self.worker.get_info()

        self.assertEqual(expected_get_info, actual_get_info)


if __name__ == "__main__":
    unittest.main()
