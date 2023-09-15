class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age = age

    def hello(self):
        return (f'Hello, my name is {self.name} {self.surname}')

    def set_name(self, new_name):
        self.name = new_name

person_1 = Person('Yulia', 'Matusevich', 42)
print(person_1.name)
person_1.set_name('Elena')
print(person_1.hello())
print(f'Attributes {person_1.__dict__}')

person_2 = Person('Alex', 'Ivanov',30)
print(person_2.surname)

person_1.surname = person_2.surname
print(person_1.surname)

print(type(person_1))

print(person_1.hello())

class Tester(Person):

    def __init__(self, name, surname, age, framework):
        super().__init__(name,surname, age)
        self.framework = framework

    def test(self):
        return 'I love testing'
tester_1 = Tester('Max','Popov', 40,'Selenium')
print(tester_1.name)
print(tester_1.framework)
print(tester_1.hello())