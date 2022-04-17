# 01. Person
# class Person:
#     def __init__(self, name: str, age: int):
#         self.__age = age
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#
# person = Person("George", 32)
# print(person.get_name())
# print(person.get_age())


# 02. mammal
# class mammal:
#     __kingdom = "animals"
#
#     def __init__(self, name: str, type: str, sound: str):
#         self.sound = sound
#         self.type = type
#         self.name = name
#
#     def make_sound(self):
#         return f"{self.name} makes {self.sound}"
#
#     def get_kingdom(self):
#         return mammal.__kingdom
#
#     def info(self):
#         return f"{self.name} is of type {self.type}"
#
#
# mammal = mammal("Dog", "Domestic", "Bark")
# print(mammal.make_sound())
# print(mammal.get_kingdom())
# print(mammal.info())


# 03. Profile
# from re import findall
#
#
# class Profile:
#
#     def __init__(self, username: str, password: str):
#         self.username = username
#         self.password = password
#
#     @property
#     def username(self):
#         return self.__username
#
#     @username.setter
#     def username(self, value):
#         if not 5 <= len(value) <= 15:
#             raise ValueError("The username must be between 5 and 15 characters.")
#         self.__username = value
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, value):
#         if len(value) < 8 or len(findall(r"([A-Z\d+])", value)) < 2:
#             raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
#         self.__password = value
#
#     def __str__(self):
#         return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)


# 04. Email Validator
# from re import split
#
#
# class EmailValidator:
#     __EMAIL_REGEX = '[@.]'
#
#     def __init__(self, min_length: int, mails: list, domains: list):
#         self.domains = domains
#         self.mails = mails
#         self.min_length = min_length
#
#     def __is_name_valid(self, name):
#         return self.min_length <= len(name)
#
#     def __is_mail_valid(self, mail):
#         return mail in self.mails
#
#     def __is_domain_valid(self, domain):
#         return domain in self.domains
#
#     def validate(self, email):
#         (name, mail, domain) = split(EmailValidator.__EMAIL_REGEX, email)
#         return self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)
#
#
# mails = ["gmail", "softuni"]
# domains = ["com", "bg"]
# email_validator = EmailValidator(6, mails, domains)
# print(email_validator.validate("pe77er@gmail.com"))
# print(email_validator.validate("georgios@gmail.net"))
# print(email_validator.validate("stamatito@abv.net"))
# print(email_validator.validate("abv@softuni.bg"))


# 05. Account
# class Account:
#
#     def __init__(self, id: int, balance: int, pin: int):
#         self.__pin = pin
#         self.__id = id
#         self.balance = balance
#
#     def __is_pin_valid(self, pin):
#         return self.__pin == pin
#
#     def get_id(self, pin: int):
#         if not self.__is_pin_valid(pin):
#             return f"Wrong pin"
#         return self.__id
#
#     def change_pin(self, old_pin: int, new_pin: int):
#         if not self.__is_pin_valid(old_pin):
#             return f"Wrong pin"
#         self.__pin = new_pin
#         return f"Pin changed"
#
#
# account = Account(8827312, 100, 3421)
# print(account.get_id(1111))
# print(account.get_id(3421))
# print(account.balance)
# print(account.change_pin(2212, 4321))
# print(account.change_pin(3421, 1234))
