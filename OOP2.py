"""
Инкабуляция - один из основных принципов ООП, который подрозумивает сокрытие внутринного состояния объекта
и представление доступа к нему только через спец методы.
Это позволяет защитить данные от никоректного использования
"""
class Person:
    def __init__(self, name, lastname, age, passport):
        self.name = name
        self.lastname = lastname

    # Защитные атрибуты
        self._age = age

    # Приватный атрибут
        self.__passport = passport

    def change_name(self, name):
        self.name = name

    def get_passport(self):
        return self.__passport

    def set_passport(self, passport):
        if not passport.isdigit():
            raise ValueError("Паспорт должен быть цифрой")
        self.__passport = passport

person_1 = Person(name="Vova", lastname="Ivanov", age=19, passport = "12345")
person_1.set_passport('3455345f') # если ты внесешь букву выведиться ошибка
# (о букве f) / если цифра значит все хорошо
print(person_1.get_passport())

