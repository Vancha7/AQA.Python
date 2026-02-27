# Задание 1: Базовое наследование
# 1. Создай родительский класс `Transport`.
#    Добавь для него метод `move`, который будет выводить на экран фразу "Транспорт движется".
# 2. Создай дочерний класс `Car`, который наследуется от `Transport`.
#    Не добавляй пока в него никаких новых методов или атрибутов.
# 3. Создай объект (экземпляр) класса `Car` и вызови у него метод `move()`.
#    Убедись, что он выведет фразу от родительского класса.

class Transport:
    def move(self):
        print("Транспорт движется")

class Car(Transport):
    pass
car = Car()
car.move()

# Задание 2: Переопределение методов (Method Overriding)
# 1. Используй классы из предыдущей задачи (или создай заново):
#    - Родительский класс `Transport` с методом `move`, который выводит "Транспорт движется".
# 2. Создай дочерний класс `Bicycle` (Велосипед), который наследуется от `Transport`.
# 3. В классе `Bicycle` переопредели (напиши заново) метод `move` так,
#    чтобы он выводил на экран фразу "Велосипед крутит педали".
# 4. Создай объект класса `Bicycle` и вызови у него метод `move()`.
#    Убедись, что выводится фраза про велосипед, а не про транспорт.

class Transport:
    def move(self):
        print("Транспорт движется")

class Bicycle(Transport):
    def move(self):
        print("Велосипед крутит педали")

bicycle = Bicycle()
bicycle.move()

# Задание 3: Вызов методов родителя (super())
# 1. Создай родительский класс `Device` (Устройство).
#    - Добавь метод `turn_on`, который выводит: "Устройство включается в сеть".
# 2. Создай дочерний класс `Laptop` (Ноутбук), который наследуется от `Device`.
# 3. В классе `Laptop` переопредели метод `turn_on`.
#    Внутри этого метода нужно:
#    - Сначала вызвать метод `turn_on` родительского класса (используй `super()`).
#    - Затем добавить свою фразу: "Ноутбук загружает операционную систему".
# 4. Создай объект класса `Laptop` и вызови его метод `turn_on()`.
# Подсказка: вызов родительского метода через super() выглядит так:
# super().имя_метода()

class Device:
    def turn_on(self):
        print("Устройство включается в сеть")

class Laptop(Device):
    def turn_on(self):
        super().turn_on()
        print("Ноутбук загружает операционную систему")
device = Laptop()
device.turn_on()


# Задание 4: Множественное наследование
# 1. Создай два родительских класса:
#    - `Flyer` (Летающий): с методом `fly`, который выводит "Могу летать".
#    - `Swimmer` (Плавающий): с методом `swim`, который выводит "Могу плавать".
# 2. Создай класс `Duck` (Утка), который наследуется ОТ ОБОИХ классов: `Flyer` и `Swimmer`.
#    Внутри класса `Duck` пока ничего не пиши (используй `pass`).
# 3. Создай объект класса `Duck` и вызови у него оба метода: `fly()` и `swim()`.
#    Убедись, что утка умеет и летать, и плавать.
# Подсказка: при множественном наследовании родители перечисляются в скобках через запятую:
# class Child(Parent1, Parent2):
class Flyer:
    def fly(self):
        print("Могу летать")

class Swimmer:
    def swim(self):
        print("Могу плавать")

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
duck.fly()
duck.swim()

# Задание 5: Проверка принадлежности к классу (isinstance)
# 1. Создай класс `Animal` (Животное) с методом `speak`, который выводит "Издает звук".
# 2. Создай два дочерних класса:
#    - `Dog` (Собака): переопредели метод `speak` на вывод "Гав!".
#    - `Cat` (Кошка): переопредели метод `speak` на вывод "Мяу!".
# 3. Создай по одному объекту каждого класса: `dog` и `cat`.
# 4. Используя функцию `isinstance()`, напиши проверки:
#    - Является ли `dog` объектом класса `Dog`? (выведи результат)
#    - Является ли `dog` объектом класса `Animal`? (выведи результат)
#    - Является ли `cat` объектом класса `Dog`? (выведи результат)
#    - Является ли `cat` объектом класса `Animal`? (выведи результат)
# Подсказка: isinstance(объект, Класс) возвращает True или False.
# Просто выведи результаты этих проверок на экран через print().
class Animal:
    def speak(self):
        print("Издает звук")

class Dog(Animal):
    def speak(self):
        print("Гав!")
class Cat(Animal):
    def speak(self):
        print("Мяу!")

dog = Dog()
cat = Cat()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(cat, Dog))
print(isinstance(cat, Animal))

# Задание 6: Атрибуты класса и наследование
# 1. Создай родительский класс `Employee` (Сотрудник).
#    - Добавь атрибут класса `company = "Рога и Копыта"`.
#    - Добавь метод `__init__`, который принимает `name` и сохраняет его как атрибут экземпляра.
#    - Добавь метод `show_info`, который выводит: "Имя: {name}, Компания: {company}".
# 2. Создай дочерний класс `Developer` (Разработчик), наследующий от `Employee`.
#    - В `__init__` добавь ещё один параметр `programming_language` и сохрани его.
#    - Переопредели метод `show_info` так, чтобы он выводил:
#      "Имя: {name}, Компания: {company}, Язык: {programming_language}".
#    - Используй `super().__init__(name)` для вызова родительского конструктора.
# 3. Создай объект `dev = Developer("Анна", "Python по блокам.")` и вызови его метод `show_info()`.
# Подсказка: чтобы обратиться к атрибуту класса внутри метода, пиши `self.company`.
class Employee:
    company = "Рога и Копыта"
    def __init__(self, name):
        self.name = name
    def show_info(self):
        print(f"Имя: {self.name}, Компания: {self.company}")

class Developer(Employee):
    def __init__(self, name, programming_language):
        super().__init__(name)
        self.programming_language = programming_language
    def show_info(self):
         print(f"Имя: {self.name}, Компания: {self.company}, Язык: {self.programming_language}")

dev = Developer("Анна", "Python по блокам.")
dev.show_info()

# Задание 7: Множественное наследование и порядок разрешения методов (MRO)
#
# 1. Создай класс `A` с методом `who_am_i`, который выводит "Я класс A".
# 2. Создай класс `B` с методом `who_am_i`, который выводит "Я класс B".
# 3. Создай класс `C` с методом `who_am_i`, который выводит "Я класс C".
# 4. Создай класс `D(A, B)` (наследуется от A и B, в этом порядке). Внутри `pass`.
# 5. Создай класс `E(B, C)` (наследуется от B и C, в этом порядке). Внутри `pass`.
# 6. Создай класс `F(D, E)` (наследуется от D и E, в этом порядке). Внутри `pass`.
# 7. Создай объект класса `F` и вызови его метод `who_am_i`.
# 8. Выведи на экран `F.__mro__` чтобы увидеть порядок поиска методов.
#
# Подсказка: метод ищется слева направо по дереву наследования.
class A:
    def who_am_i(self):
        print("Я класс А")
class B:
    def who_am_i(self):
        print("Я класс В")
class C:
    def who_am_i(self):
        print("Я класс С")

class D(A, B):
    pass
class E(B, C):
    pass
class F(D, E):
    pass
obj = F()
obj.who_am_i()
print(F.__mro__)

# Задание 8: Проверка подклассов (issubclass)
# 1. Создай класс `Vehicle` (Транспортное средство).
# 2. Создай класс `GroundVehicle` (Наземный транспорт), наследующий от `Vehicle`.
# 3. Создай класс `WaterVehicle` (Водный транспорт), наследующий от `Vehicle`.
# 4. Создай класс `AmphibiousVehicle` (Транспорт-амфибия), наследующий от `GroundVehicle` и `WaterVehicle`.
# 5. Используя функцию `issubclass()`, проверь и выведи на экран:
#    - Является ли `AmphibiousVehicle` подклассом `Vehicle`?
#    - Является ли `AmphibiousVehicle` подклассом `GroundVehicle`?
#    - Является ли `AmphibiousVehicle` подклассом `WaterVehicle`?
#    - Является ли `GroundVehicle` подклассом `AmphibiousVehicle`?
#    - Является ли `Vehicle` подклассом `object`?
# Подсказка: issubclass(ДочернийКласс, РодительскийКласс) возвращает True/False.
class Vehicle:
    pass
class GroundVehicle(Vehicle):
    pass
class WaterVehicle(Vehicle):
    pass
class AmphibusVehicle(GroundVehicle, WaterVehicle):
    pass
print(issubclass(AmphibusVehicle, Vehicle))
print(issubclass(AmphibusVehicle, GroundVehicle))
print(issubclass(AmphibusVehicle, WaterVehicle))
print(issubclass(GroundVehicle, AmphibusVehicle))
print(issubclass(Vehicle, object))

# Задание 9: super() с множественным наследованием
# 1. Создай класс `Base` с методом `__init__`, который выводит "Base init".
# 2. Создай класс `A(Base)` с методом `__init__`, который:
#    - Выводит "A init"
#    - Вызывает `super().__init__()`
# 3. Создай класс `B(Base)` с методом `__init__`, который:
#    - Выводит "B init"
#    - Вызывает `super().__init__()`
# 4. Создай класс `C(A, B)` с методом `__init__`, который:
#    - Выводит "C init"
#    - Вызывает `super().__init__()`
# 5. Создай объект класса `C` и посмотри на порядок вызовов.
# 6. Выведи `C.__mro__` чтобы понять, почему порядок именно такой.
# Подсказка: super() вызывает следующий класс по цепочке MRO.
class Base:
    def __init__(self):
        print("Base init")
class A(Base):
    def __init__(self):
        print("A init")
        super().__init__()
class B(Base):
    def __init__(self):
        print("B init")
        super().__init__()
class C(A, B):
    def __init__(self):
        print("C init")
        super().__init__()
c = C()
print(C.__mro__)

# Задание 10: Наследование и переопределение __str__
# 1. Создай класс `Person` с методом `__init__`, который принимает `name` и `age`.
# 2. Добавь метод `__str__`, который возвращает строку: "Имя: {name}, Возраст: {age}".
# 3. Создай класс `Student`, который наследует от `Person`.
# 4. В классе `Student` переопредели метод `__str__` так, чтобы он возвращал:
#    "Студент: {name}, Возраст: {age}".
# 5. Создай объект `student = Student("Анна", 20)` и выведи его через `print()`.
# Подсказка: print(объект) автоматически вызывает __str__.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}"
class Student(Person):
    def __str__(self):
        return f"Студент: {self.name}, Возраст: {self.age}"
student = Student("Анна", 20)
print(student)

# Задание 11: Наследование и super() в __init__
# 1. Создай класс `Product` с методом `__init__`, который принимает `name` и `price`.
#    Сохрани их как атрибуты.
# 2. Создай класс `Food`, который наследует от `Product`.
# 3. В классе `Food` добавь в `__init__` третий параметр `expiration_date` (срок годности).
#    - Вызови `super().__init__(name, price)` для инициализации родительских атрибутов.
#    - Сохрани `expiration_date` как атрибут.
# 4. Создай объект `food = Food("Молоко", 80, "10.03.2026")`.
# 5. Выведи на экран все три атрибута через `print(food.name, food.price, food.expiration_date)`.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Food(Product):
    def __init__(self, name, price, expiration_date):
        super().__init__(name, price)
        self.expiration_date = expiration_date
food = Food("Молоко", 80, "10.03.2026")
print(food.name, food.price, food.expiration_date)

# Задание 12: Защищённые атрибуты и наследование
# 1. Создай класс `BankAccount` с методом `__init__`, который принимает `owner` и `balance`.
#    - Сохрани `owner` как публичный атрибут.
#    - Сохрани `balance` как защищённый атрибут (с одним подчёркиванием: `_balance`).
# 2. Добавь метод `get_balance`, который возвращает значение `_balance`.
# 3. Добавь метод `deposit`, который принимает сумму и увеличивает `_balance` на эту сумму.
# 4. Создай класс `SavingsAccount`, который наследует от `BankAccount`.
# 5. В классе `SavingsAccount` добавь метод `add_interest`, который увеличивает `_balance` на 10%.
# 6. Создай объект `savings = SavingsAccount("Иван", 1000)`.
# 7. Вызови `savings.add_interest()` и затем выведи баланс через `savings.get_balance()`.
# Подсказка: защищённые атрибуты доступны в дочерних классах.
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount


class SavingsAccount(BankAccount):
    def add_interest(self):
        self._balance = self._balance / 100 * 110


savings = SavingsAccount("Иван", 1000)
savings.add_interest()
savings.get_balance()
print(savings.get_balance())


# Задание 13: Приватные атрибуты и наследование
# 1. Создай класс `Parent` с методом `__init__`, который создаёт:
#    - Публичный атрибут `pub = "публичный"`
#    - Защищённый атрибут `_prot = "защищённый"`
#    - Приватный атрибут `__priv = "приватный"` (с двумя подчёркиваниями)
# 2. Добавь метод `get_priv`, который возвращает значение `__priv`.
# 3. Создай класс `Child`, который наследует от `Parent`.
# 4. В классе `Child` добавь метод `try_access`, который пытается:
#    - Вывести `self.pub`
#    - Вывести `self._prot`
#    - Вывести `self.__priv` (закомментируй эту строку, чтобы программа работала)
#    - Вывести `self.get_priv()` (это работает всегда)
# 5. Создай объект `child = Child()` и вызови `child.try_access()`.
# Подсказка: напрямую к `__priv` из дочернего класса доступа нет.
class Parent:
    def __init__(self, pub, _prot, __priv):
        self.pub = pub
        self._prot = _prot
        self.__priv = __priv
    def get_priv(self):
        return self.__priv
class Child(Parent):
    def try_access(self):
        print(self.pub)
        print(self._prot)
#  print(self.__priv)
        print(self.get_priv())
child = Child("публичный","защищённый", "приватный")
child.try_access()

# Задание 14: Наследование и множественный __init__
# 1. Создай класс `A` с методом `__init__`, который выводит "A init".
# 2. Создай класс `B` с методом `__init__`, который выводит "B init".
# 3. Создай класс `C(A, B)` с методом `__init__`, который:
#    - Выводит "C init"
#    - Вызывает `super().__init__()`
# 4. Создай объект класса `C` и посмотри, какие __init__ вызываются и в каком порядке.
# 5. Выведи `C.__mro__` чтобы увидеть порядок поиска.
# Подсказка: super() вызывает следующий класс по цепочке MRO.
class A:
    def __init__(self):
        print("A init")
class B:
    def __init__(self):
        print("B init")
class C(A, B):
    def __init__(self):
        print("C init")
        super().__init__()
c = C()
print(C.__mro__)

# Задание 15: Наследование и проверка типов
# 1. Создай класс `Animal` с методом `speak`, который возвращает "Звук".
# 2. Создай класс `Dog(Animal)` с методом `speak`, который возвращает "Гав".
# 3. Создай класс `Cat(Animal)` с методом `speak`, который возвращает "Мяу".
# 4. Создай функцию `make_sound(animal)`, которая:
#    - Проверяет, является ли `animal` объектом класса `Animal` (через `isinstance`).
#    - Если да, вызывает и выводит результат метода `speak`.
#    - Если нет, выводит "Это не животное".
# 5. Создай объекты `dog`, `cat` и строку `"привет"`.
# 6. Вызови функцию для каждого из них.
class Animal:
    def speak(self):
        return "Звук"
class Dog(Animal):
    def speak(self):
        return "Гав"
class Cat(Animal):
    def speak(self):
        return "Мяу"
def make_sound(animal):
    if (isinstance(animal, Animal)):
      print(animal.speak())
    else:
      print("Это не животное")
dog = Dog()
cat = Cat()
stri = "привет"
make_sound(cat)
make_sound(dog)
make_sound(stri)

# Задание 16: Наследование и классовые атрибуты
# 1. Создай класс `Counter` с атрибутом класса `count = 0`.
# 2. Добавь метод `__init__`, который увеличивает `Counter.count` на 1 при создании каждого нового объекта.
# 3. Добавь метод `get_count`, который возвращает текущее значение `Counter.count`.
# 4. Создай класс `SubCounter(Counter)`, внутри `pass`.
# 5. Создай три объекта: два от `Counter` и один от `SubCounter`.
# 6. Выведи значение счётчика через `get_count` у любого объекта.
# Подсказка: атрибуты класса общие для всех наследников, если не переопределены.
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    def get_count(self):
        return Counter.count
class SubCounter(Counter):
    pass
objec = Counter()
objec1 = Counter()
objec2 = SubCounter()
print(objec.get_count())

# Задание 17: super() и доступ к методам родителя
# 1. Создай класс `Parent` с методом `hello`, который возвращает "Привет от Parent".
# 2. Создай класс `Child(Parent)`.
# 3. В классе `Child` переопредели метод `hello`, чтобы он:
#    - Сначала вызывал родительский метод через `super().hello()` и выводил результат
#    - Потом выводил "И привет от Child"
# 4. Создай объект `child = Child()` и вызови его метод `hello()`.
# Подсказка: print(super().hello()) не сработает, сначала получи результат, потом выводи.
class Parent:
    def hello(self):
        return "Привет от Parent"
class Child(Parent):
    def hello(self):
        get = super().hello()
        print(get)
        print("И привет от Child")
child = Child()
child.hello()

# Задание 18: Наследование и перегрузка операторов
# 1. Создай класс `Point` с методом `__init__`, который принимает `x` и `y`.
# 2. Перегрузи оператор `__add__` (сложение), чтобы он возвращал новый объект `Point`
#    с координатами `x + other.x` и `y + other.y`.
# 3. Создай класс `Point3D(Point)` с методом `__init__`, который принимает `x`, `y`, `z`.
#    Вызови `super().__init__(x, y)` и сохрани `z`.
# 4. Перегрузи оператор `__add__` в `Point3D`, чтобы он возвращал новый объект `Point3D`
#    с координатами `x + other.x`, `y + other.y`, `z + other.z`.
#    Используй `super().__add__(other)` для сложения x и y, и добавь z отдельно.
# 5. Создай два объекта `p1 = Point3D(1, 2, 3)` и `p2 = Point3D(4, 5, 6)`.
# 6. Сложи их: `p3 = p1 + p2` и выведи координаты `p3` (например, через `print(p3.x, p3.y, p3.z)`).
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
p1 = Point3D(1, 2, 3)
p2 = Point3D(4, 5, 6)
p3 = p1 + p2
print(p3.x, p3.y, p3.z)

# Задание 19: Наследование и property
# 1. Создай класс `Rectangle` с методом `__init__`, который принимает `width` и `height`.
# 2. Добавь свойство `area` (с декоратором `@property`), которое возвращает `width * height`.
# 3. Создай класс `Square(Rectangle)`.
# 4. В классе `Square` переопредели `__init__`, чтобы он принимал только `side`.
#    Вызови `super().__init__(side, side)`.
# 5. Создай объект `square = Square(5)` и выведи его площадь через свойство `area`.
# Подсказка: свойство `area` наследуется и работает автоматически.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width * self.height
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
square = Square(5)
print(square.area)

# Задание 20: Наследование и исключения
# 1. Создай класс `MyException(Exception)` - пустой (просто `pass`).
# 2. Создай функцию `check_positive(number)`, которая:
#    - Если число меньше 0, выбрасывает исключение `MyException` с сообщением "Отрицательное число!".
#    - Иначе возвращает "Всё хорошо".
# 3. В основной части программы:
#    - Оберни вызов `check_positive(-5)` в `try-except`.
#    - В блоке `except MyException as e` выведи сообщение исключения.
#    - Добавь блок `else`, который выводит результат, если исключения не было.
#    - Добавь блок `finally`, который выводит "Проверка завершена".
# 4. Для проверки вызови функцию ещё раз с числом 10.
# Подсказка: чтобы передать сообщение в исключение, пиши `raise MyException("текст")`.
class MyException(Exception):
    pass
def check_positive(number):
    if number < 0:
        raise MyException("Отрицательное число!")
    else:
        print("Всё хорошо")
try:
    check_positive(-5)
except MyException as e:
    print(e)
else:
    print("Всё хорошо")
finally:
    print("Проверка завершена")
try:
    check_positive(10)
except MyException as e:
    print(e)
else:
    print("Всё хорошо")
finally:
    print("Проверка завершена")

# Задание 21: Наследование и classmethod с наследованием
# 1. Создай класс `Person` с методом `__init__`, который принимает `name` и `age`.
# 2. Добавь классовый метод `from_birth_year` (декоратор `@classmethod`), который:
#    - Принимает `name` и `birth_year`
#    - Вычисляет возраст как 2026 - birth_year
#    - Возвращает новый объект `cls(name, возраст)` (используй `cls`, а не `Person`)
# 3. Создай класс `Student(Person)`, внутри `pass`.
# 4. Создай объект `student = Student.from_birth_year("Анна", 2000)`.
# 5. Выведи `student.name` и `student.age`.
# 6. Выведи тип объекта (`type(student)`) чтобы убедиться, что это Student.
# Подсказка: использование `cls` в classmethod позволяет создавать объекты того класса,
#           от которого вызван метод (Person или Student).
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2026 - birth_year
        return cls(name, age)
class Student(Person):
    pass
student = Student.from_birth_year("Анна", 2000)
print(student.name, student.age)
print(type(student))

# Задание 22: Наследование и staticmethod
# 1. Создай класс `Math` со статическим методом `add` (декоратор `@staticmethod`),
#    который принимает два числа и возвращает их сумму.
# 2. Создай класс `AdvancedMath(Math)`, внутри `pass`.
# 3. Вызови метод `add` через класс `Math` (Math.add(5, 3)) и выведи результат.
# 4. Вызови метод `add` через класс `AdvancedMath` (AdvancedMath.add(10, 7)) и выведи результат.
# 5. Вызови метод `add` через объект класса `AdvancedMath` и выведи результат.
# Подсказка: статические методы не имеют self или cls, работают как обычные функции,
#           но лежат внутри класса. Наследуются как обычные методы.
class Math:
    @staticmethod
    def add(a, b):
        return a + b
class AdvancedMath(Math):
    pass

print((Math.add(5, 3)))
print((AdvancedMath.add(10, 7)))
obj = AdvancedMath()
print(obj.add(5, 3))

# Задание 23: Наследование и множественные конструкторы
# 1. Создай класс `User` с методом `__init__`, который принимает `username` и `email`.
# 2. Добавь классовый метод `from_string` (декоратор `@classmethod`), который:
#    - Принимает строку вида "username:email"
#    - Разделяет строку по двоеточию (метод `split(':'))
#    - Возвращает новый объект `cls(username, email)`
# 3. Создай класс `Admin(User)`, внутри `pass`.
# 4. Создай объект `admin = Admin.from_string("admin:admin@site.com")`.
# 5. Выведи `admin.username` и `admin.email`.
# Подсказка: split(':') вернёт список из двух элементов.
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    @classmethod
    def from_string(cls, string):
        username, email = string.split(":")
        return cls(username, email)
class Admin(User):
    pass
admin = Admin.from_string("admin:admin@site.com")
print(admin.username, admin.email)

# Задание 24: Наследование и property setter
# 1. Создай класс `Circle` с методом `__init__`, который принимает `radius`.
#    Сделай `radius` защищённым атрибутом (`_radius`).
# 2. Добавь свойство `radius` (геттер), которое возвращает значение `_radius`.
# 3. Добавь сеттер для `radius` (с декоратором `@radius.setter`), который:
#    - Проверяет, что новое значение больше 0. Если нет, выводит "Радиус должен быть положительным".
#    - Если проверка пройдена, присваивает `_radius = value`.
# 4. Создай класс `BigCircle(Circle)`, внутри `pass`.
# 5. Создай объект `big = BigCircle(10)`, выведи радиус.
# 6. Попробуй установить отрицательный радиус: `big.radius = -5`.
# 7. Установи радиус 15 и выведи его снова.
# Подсказка: property и его сеттер наследуются и работают так же.
class Circle:
    def __init__(self, radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if value < 0:
            print("Радиус должен быть положительным")
        else:
            self._radius = value
class BigCircle(Circle):
    pass
big = BigCircle(10)
print(big.radius)
big.radius = -5
big.radius = 15
print(big.radius)

# Задание 25: Наследование и __slots__
# 1. Создай класс `Point` с __slots__ = ['x', 'y'].
# 2. Добавь метод __init__, который принимает x и y и сохраняет их.
# 3. Создай класс `Point3D(Point)` с __slots__ = ['z'] (только z, x и y уже есть в родителе).
# 4. Добавь в Point3D метод __init__, который принимает x, y, z.
#    Вызови super().__init__(x, y) и сохрани z.
# 5. Создай объект `p = Point3D(1, 2, 3)`.
# 6. Выведи p.x, p.y, p.z.
# 7. Попробуй создать новый атрибут `p.color = "red"` и посмотри, что будет (закомментируй эту строку).
# Подсказка: __slots__ ограничивает набор атрибутов. В дочерних классах нужно
#           добавлять свои __slots__, чтобы расширить список разрешённых атрибутов.
class Point:
    __slots__ = ["x", "y"]
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Point3D(Point):
    __slots__ = ["z"]
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
p = Point3D(1, 2, 3)
print(p.x, p.y, p.z)
#p.color = "red"
print(p.x, p.y, p.z)

# Задание 26: Наследование и сравнение объектов
# 1. Создай класс `Person` с методом __init__, который принимает name и age.
# 2. Перегрузи метод __eq__ (равенство), чтобы он сравнивал возраст двух объектов.
#    Два человека считаются равными, если у них одинаковый возраст.
# 3. Перегрузи метод __lt__ (меньше), чтобы он сравнивал возраст.
# 4. Создай класс `Employee(Person)`, внутри pass.
# 5. Создай объекты:
#    - p1 = Person("Анна", 25)
#    - p2 = Person("Иван", 30)
#    - e1 = Employee("Петр", 25)
# 6. Выведи результаты сравнений:
#    - p1 == p2
#    - p1 == e1 (сравнение Person и Employee)
#    - p1 < p2
# Подсказка: методы сравнения наследуются и работают с объектами любого дочернего класса.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__ (self, other):
        return self.name == other.name
    def __lt__(self, other):
        return self.name < other.name
class Employee(Person):
    pass
p1 = Person("Анна", 25)
p2 = Person("Иван", 30)
e1 = Employee("Петр", 25)
print(p1 == p2)
print(p1 == e1)
print(p1 < p2)

# Задание 27: Наследование и декораторы
# 1. Создай класс `Logger` с методом `log(message)`, который выводит f"LOG: {message}".
# 2. Создай класс `Application` с методом `run`, который выводит "Приложение запущено".
# 3. Создай класс `LoggedApplication(Application, Logger)` (в этом порядке).
# 4. В классе `LoggedApplication` переопредели метод `run`, чтобы он:
#    - Сначала вызывал `self.log("Запуск приложения")`
#    - Потом вызывал родительский `run` через `super().run()`
# 5. Создай объект `app = LoggedApplication()` и вызови `app.run()`.
# Подсказка: множественное наследование позволяет комбинировать функциональность.
class Logger:
    def log(self, message) -> None:
        print(f"LOG: {message}")
class Application:
    def run(self) -> None:
        print("Приложение запущено")
class LoggedApplication(Application, Logger):
    def run(self):
        self.log("Запуск приложения")
        super().run()
app = LoggedApplication()
app.run()

# Задание 28: Наследование и композиция
# 1. Создай класс `Engine` с методом `start`, который возвращает "Двигатель запущен".
# 2. Создай класс `Wheels` с методом `rotate`, который возвращает "Колёса крутятся".
# 3. Создай класс `Car`, который НЕ наследуется от Engine и Wheels, а использует их внутри.
#    - В `__init__` создай атрибуты `self.engine = Engine()` и `self.wheels = Wheels()`.
#    - Добавь метод `drive`, который вызывает `engine.start()` и `wheels.rotate()`
#      и возвращает объединённую строку (например, через f"{self.engine.start()} {self.wheels.rotate()}").
# 4. Создай объект `car = Car()` и выведи результат метода `drive()`.
# Подсказка: это композиция (объект содержит другие объекты), а не наследование.
class Engine:
    def start(self):
        return "Двигатель запущен"
class Wheels:
    def rotate(self):
        return "Колёса крутятся"
class Car:
    def __init__(self):
        self.wheels = Wheels()
        self.engine = Engine()
    def drive(self):
        return f"{self.engine.start()} {self.wheels.rotate()}"
car = Car()
print(car.drive())

# Задание 29: Наследование и isinstance с интерфейсами
# 1. Создай класс `Flyable` (интерфейс) с методом `fly`, который возвращает "Летит".
# 2. Создай класс `Swimmable` (интерфейс) с методом `swim`, который возвращает "Плывёт".
# 3. Создай класс `Duck(Flyable, Swimmable)`:
#    - Реализуй метод `fly` (возвращает "Утка летит")
#    - Реализуй метод `swim` (возвращает "Утка плывёт")
# 4. Создай класс `Plane(Flyable)`:
#    - Реализуй метод `fly` (возвращает "Самолёт летит")
# 5. Создай функцию `test_fly(obj)`, которая проверяет `isinstance(obj, Flyable)`:
#    - Если да, вызывает и выводит `obj.fly()`
#    - Если нет, выводит "Не умеет летать"
# 6. Создай объекты `duck = Duck()` и `plane = Plane()`.
# 7. Вызови `test_fly` для каждого.
# Подсказка: интерфейсы — это просто классы, от которых наследуются.
class Flyable:
    def fly(self):
        return "Летит"
class Swimmable:
    def swim(self):
        return "Плывёт"
class Duck(Flyable, Swimmable):
    def fly(self):
        return "Утка летит"
    def swim(self):
        return "Утка плывёт"
class Plane(Flyable):
    def fly(self):
        return "Самолёт летит"
def test_fly(obj):
        if isinstance(obj, Flyable):
            print(obj.fly())
        else:
            print("Не умеет летать")
duck = Duck()
plane = Plane()
test_fly(plane)
test_fly(duck)

# Задание 30: Цепочка наследования
# 1. Создай класс `Grandparent` с методом `who`, который возвращает "Я дедушка/бабушка".
# 2. Создай класс `Parent(Grandparent)` с методом `who`, который возвращает "Я родитель".
#    Внутри метода вызови `super().who()` и сохрани результат, но верни только свою строку.
# 3. Создай класс `Child(Parent)` с методом `who`, который возвращает "Я ребёнок".
#    Внутри метода вызови `super().who()` и сохрани результат, но верни только свою строку.
# 4. Создай объект `child = Child()` и вызови его метод `who()`.
# 5. Выведи результат.
# Подсказка: методы вызываются по цепочке, но каждая ступень может делать что-то своё.
class Grandparent:
    def who(self):
        return "Я дедушка/бабушка"
class Parent(Grandparent):
    def who(self):
        result = super().who()
        return "Я родитель"
class Child(Parent):
    def who(self):
        result1 = super().who()
        return "Я ребёнок"
child = Child()
print(child.who())

# Задание 31: Наследование и счётчик объектов
# 1. Создай класс `Counter` с атрибутом класса `total_objects = 0`.
# 2. В `__init__` увеличивай `Counter.total_objects` на 1.
# 3. Добавь метод `get_count`, который возвращает `Counter.total_objects`.
# 4. Создай класс `MyClass(Counter)`, внутри `pass`.
# 5. Создай три объекта: два от `Counter` и один от `MyClass`.
# 6. Выведи общее количество созданных объектов через `get_count` у любого объекта.#
# Подсказка: атрибут класса общий для всех, включая наследников.
class Counter:
    total_objects = 0
    def __init__(self):
        Counter.total_objects += 1
    def get_count(self):
        return Counter.total_objects
class MyClass(Counter):
    pass
counter1 = Counter()
counter2 = Counter()
my_class = MyClass()
print(counter1.get_count())\

# Задание 32: Наследование и переопределение __str__ с super
# 1. Создай класс `Book` с методом __init__, который принимает `title` и `author`.
# 2. Переопредели метод `__str__`, чтобы он возвращал f"'{title}' by {author}".
# 3. Создай класс `EBook(Book)` с методом __init__, который принимает `title`, `author` и `size_mb`.
#    Вызови super().__init__(title, author) и сохрани `size_mb`.
# 4. Переопредели метод `__str__` в `EBook`:
#    - Вызови super().__str__() и сохрани результат
#    - Верни f"{результат_от_родителя}, Size: {size_mb}MB"
# 5. Создай объект `ebook = EBook("1984", "Оруэлл", 2.5)` и выведи его через `print()`.
# Подсказка: super().__str__() вернёт строку от родителя, которую можно использовать.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"'{self.title}' by {self.author}"
class EBook(Book):
    def __init__(self, title, author, size_mb):
        super().__init__(title, author)
        self.size_mb = size_mb
    def __str__(self):
        book_str = super().__str__()
        return f"{book_str}, Size: {self.size_mb}MB"
ebook = EBook("1984", "Оруэлл", 2.5)
print(ebook)

# Задание 33: Наследование и множественное наследование с одинаковыми методами
# 1. Создай класс `A` с методом `say_hello`, который возвращает "Привет от A".
# 2. Создай класс `B` с методом `say_hello`, который возвращает "Привет от B".
# 3. Создай класс `C(A, B)` (в этом порядке), внутри `pass`.
# 4. Создай класс `D(B, A)` (в этом порядке), внутри `pass`.
# 5. Создай объекты `c = C()` и `d = D()`.
# 6. Выведи результаты `c.say_hello()` и `d.say_hello()`.
# 7. Выведи `C.__mro__` и `D.__mro__` чтобы увидеть порядок поиска методов.
# Подсказка: метод берётся из первого класса в цепочке наследования, где он найден.
class A:
    def say_hello(self):
        return "Привет от A"
class B:
    def say_hello(self):
        return "Привет от B"
class C(A, B):
    pass
class D(B, A):
    pass
c = C()
d = D()
print(c.say_hello())
print(d.say_hello())
print(C.__mro__)
print(D.__mro__)

# Задание 34: Наследование и вызов родительского метода с аргументами
# 1. Создай класс `Printer` с методом `print_message(self, text)`, который выводит f"Печать: {text}".
# 2. Создай класс `ColoredPrinter(Printer)`.
# 3. В классе `ColoredPrinter` переопредели метод `print_message`, который принимает `text` и `color`.
#    - Вызови родительский метод `print_message` через `super().print_message(text)`
#    - Добавь вывод: f"Цвет: {color}"
# 4. Создай объект `cp = ColoredPrinter()`.
# 5. Вызови `cp.print_message("Привет", "красный")`.
# Подсказка: родительский метод ожидает только `text`, поэтому передаём ему только текст.
class Printer:
    def print_message(self,text):
        print(f"Печать: {text}")
class ColoredPrinter(Printer):
    def print_message(self, text, color):
        super().print_message(text)
        print(f"Цвет: {color}")
cp = ColoredPrinter()
cp.print_message("Привет", "красный")

# Задание 35: Наследование и проверка атрибутов
# 1. Создай класс `Vehicle` с методом `__init__`, который принимает `brand` и `model`.
# 2. Добавь метод `info`, который возвращает f"{brand} {model}".
# 3. Создай класс `Car(Vehicle)` с методом `__init__`, который принимает `brand`, `model`, `doors`.
#    Вызови super().__init__(brand, model) и сохрани `doors`.
# 4. Переопредели метод `info` так, чтобы он возвращал f"{super().info()}, дверей: {doors}".
# 5. Создай объект `car = Car("Toyota", "Corolla", 4)`.
# 6. Выведи результат `car.info()`.
# 7. Проверь через `hasattr(car, 'doors')` и `hasattr(car, 'brand')`, выведи результаты.
# Подсказка: hasattr(объект, 'имя_атрибута') возвращает True/False.
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def info(self):
        return f"{self.brand} {self.model}"
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    def info(self):
        return f"{super().info()}, дверей: {self.doors}"
car = Car("Toyota", "Corolla", 4)
print(car.info())
print(hasattr(car, "doors"))
print(hasattr(car, "brand"))