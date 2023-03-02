from string import digits, ascii_uppercase, ascii_letters


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.__password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, new_login: str):
        if "@" not in new_login:
            raise ValueError("Логин должен содержать один символ '@'")
        if new_login.rfind("@") > new_login.rfind("."):
            raise ValueError("Логин должен содержать символ '.'")
        self.__login = new_login

    @staticmethod
    def check_password_dictionary(password):
        with open("easy_passwords.txt", "r", encoding="utf-8") as file:
            x = [i for i in file.read().split()]
        if password in x:
            return False
        return True

    @staticmethod
    def is_include_digit(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def is_include_all_register(password):
        for alpha in ascii_uppercase:
            if alpha in password[0]:
                return True
        return False

    @staticmethod
    def is_include_only_latin(password):
        for alpha in password:
            if alpha in ascii_letters:
                return True
        return False

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password: str):
        if not isinstance(new_password,str):
            raise ValueError("Пароль должен быть строкой")
        if 5 <= len(new_password) <= 11:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(new_password):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(new_password):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(new_password):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if not Registration.check_password_dictionary(new_password):
            raise ValueError('Ваш пароль содержится в списке самых легких')



r1 = Registration('qwerty@rambler.ru', 'QwrRt124') # здесь хороший логин
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

# теперь пытаемся запись плохие пароли
r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
