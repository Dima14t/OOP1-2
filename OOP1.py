# Родительский (базовый) класс для класса Student
from multiprocessing.pool import worker


class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def hello(self):
        print(f"Привет. Меня зовут {self.name} {self.lastname}")

    def bay(self):
        pass

# Дочерний (производный) класс от класса Person
class Student(Person):
    #  Конструктор дочернего класса должен иметь атрибуты родительского класса
    # и атрибуты дочернего
    def __init__(self, name, lastname, age, group, ticket, from_study):
        # Вызываем конструктор родителя с его атрибутами
        super().__init__(name, lastname, age)
        # Создаем атрибуты дочернего класса
        self.group = group
        self.ticket = ticket
        self.from_study = from_study

    def bay(self):
        print("Goodbay!")

class WorkerStudent(Student):
    def __init__(self, name, lastname, age, group, ticket, from_study, job, salary ):
        super().__init__(name, lastname, age, group, ticket, from_study)
        self.job = job
        self.salary = salary


parson_1 = Person(name="Dima", lastname="Ivanov", age=24)
parson_1.hello()
student_1 = Student(name="Marina", lastname="Petrova", age=19,
                    group="432", ticket="AA456789", from_study="Очная")
student_1.hello()
student_1.bay()
parson_1.bay()

worker = WorkerStudent (name="Olga", lastname ="Sidorova",
                        age=22,group="532",
                        ticket="AA456789",from_study="Очная",
                        job="Yandex", salary=100000)

worker.hello()

class AbstractUser:
    def method(self):
        print("AbstractUser")

class AbstractBaseUser:
    def method(self):
        print("AbstractBaseUser")

class PermissionMixin:
    def method(self):
        print("PermissionMixin")

class User(AbstractUser, AbstractBaseUser, PermissionMixin):
    def hello(self):
        pass

obj = User()
obj.method()