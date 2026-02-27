# Задача №1 | Создание класса и общие атрибуты
# 1. Создай класс с именем Robot.
# 2. Добавь в класс общий (классовый) атрибут species.
#    Установи для него значение "Humanoid Robot".
# 3. Код должен содержать только объявление класса и атрибута.
#    Ничего выводить на экран не нужно.
from ast import increment_lineno
from itertools import product, count
from turtledemo.penrose import start


class Robot:
    species="Humanoid Robot"

# Задача №2 | Конструктор __init__
# 1. Создай класс Dog.
# 2. Добавь конструктор (метод __init__), который принимает параметры:
#    - name (кличка)
#    - age (возраст)
# 3. Внутри конструктора сохрани эти параметры как атрибуты экземпляра
#    (self.name и self.age).
# 4. Ничего выводить на экран не нужно.
class  Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Задача №3 | Объект класса
# 1. Используй класс Dog из предыдущей задачи (или создай его заново).
# 2. Создай экземпляр (объект) класса Dog с именем "Rex" и возрастом 5.
# 3. Сохрани этот объект в переменную my_dog.
# 4. Ничего выводить на экран не нужно.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
my_dog = Dog("Rex", 5)

# Задача №4 | Методы класса
# 1. Создай класс Car.
# 2. Добавь конструктор (__init__), который принимает параметр brand (марка)
#    и сохраняет его как атрибут экземпляра self.brand.
# 3. Добавь метод info, который возвращает строку вида:
#    "Марка автомобиля: {brand}"
#    (метод ничего не выводит на экран, а именно возвращает строку).
# 4. Код должен содержать только объявление класса.
class Car:
    def __init__(self, brand):
        self.brand = brand
    def display_info(self):
        return "Марка автомобиля: " + self.brand + " ."

# Задача №5 | Понимание параметра self
# 1. Создай класс Counter.
# 2. Добавь конструктор, который принимает начальное значение start
#    и сохраняет его в атрибут экземпляра self.value.
# 3. Добавь метод increment, который увеличивает self.value на 1.
#    Метод ничего не принимает (кроме self) и ничего не возвращает.
# 4. Добавь метод get_value, который возвращает текущее self.value.
# 5. Код должен содержать только объявление класса.
class Counter:
    def __init__(self, start):
        self.value = start
    def increment(self):
        self.value += 1
    def get_value(self):
       return self.value

# Задача №6 | Общие атрибуты и объекты
# 1. Создай класс Employee.
# 2. Добавь общий (классовый) атрибут company со значением "TechCorp".
# 3. Добавь конструктор, который принимает name и сохраняет как атрибут экземпляра.
# 4. Создай два объекта Employee: с именами "Anna" и "Oleg".
# 5. Сохрани их в переменные emp1 и emp2 соответственно.
# 6. Код должен содержать объявление класса и создание объектов.
class Employee:
    company = "TechCorp"
    def __init__(self, name):
        self.name = name
emp1 = Employee("Anna")
emp2 = Employee("Oleg")

# Задача №7 | Методы с возвратом значений
# 1. Создай класс Rectangle.
# 2. Добавь конструктор, который принимает width и height (ширина и высота)
#    и сохраняет их как атрибуты экземпляра.
# 3. Добавь метод area, который возвращает площадь прямоугольника.
# 4. Добавь метод perimeter, который возвращает периметр.
# 5. Код должен содержать только объявление класса.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width + self.height) * 2

# Задача №8 | Атрибуты по умолчанию в конструкторе
# 1. Создай класс Book.
# 2. Добавь конструктор с параметрами:
#    - title (обязательный)
#    - author (обязательный)
#    - year (необязательный, значение по умолчанию — 2023)
# 3. Сохрани все три параметра как атрибуты экземпляра.
# 4. Код должен содержать только объявление класса.\
class Book:
    def __init__(self, title , author, year=2023):
        self.title = title
        self.author = author
        self.year = year

# Задача №9 | Строковое представление объекта
# 1. Создай класс Person.
# 2. Добавь конструктор, который принимает name и age.
# 3. Добавь метод __str__, который возвращает строку:
#    "Имя: {name}, Возраст: {age}"
# 4. Код должен содержать только объявление класса.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

# Задача №10 | Взаимодействие методов
# 1. Создай класс BankAccount.
# 2. Добавь конструктор, который принимает owner (владелец)
#    и устанавливает начальный баланс balance = 0.
# 3. Добавь метод deposit(amount), который увеличивает баланс на amount.
# 4. Добавь метод withdraw(amount), который уменьшает баланс на amount,
#    но только если на счету достаточно средств.
#    Если средств недостаточно, баланс не меняется.
#    Метод ничего не возвращает и ничего не выводит.
# 5. Добавь метод get_balance, который возвращает текущий баланс.
# 6. Код должен содержать только объявление класса.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
            self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
    def get_balance(self):
        return self.balance

# Задача №11 | Общие атрибуты и методы класса
# 1. Создай класс Library.
# 2. Добавь общий (классовый) атрибут total_books = 0.
# 3. Добавь конструктор, который принимает name (название библиотеки)
#    и сохраняет как атрибут экземпляра.
# 4. Добавь метод add_book, который увеличивает общий счётчик total_books на 1.
#    Метод ничего не принимает (кроме self) и ничего не возвращает.
# 5. Добавь классовый метод get_total_books, который возвращает значение total_books.
#    (Не забудь про декоратор @classmethod)
# 6. Код должен содержать только объявление класса.
class Library:
    total_books = 0
    def __init__(self, name):
        self.name = name
    def add_book(self):
        type(self).total_books += 1
    @classmethod
    def get_total_books(cls):
        return cls.total_books

# Задача №12 | Статические методы
# 1. Создай класс MathUtils.
# 2. Добавь статический метод add, который принимает два числа и возвращает их сумму.
#    (Не забудь про декоратор @staticmethod)
# 3. Добавь статический метод multiply, который принимает два числа и возвращает их произведение.
# 4. Код должен содержать только объявление класса.
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def multiply(a, b):
        return a * b

# Задача №13 | Свойства (property)
# 1. Создай класс Circle.
# 2. Добавь конструктор, который принимает radius и сохраняет его в атрибут _radius.
# 3. Добавь метод radius (геттер) с декоратором @property,
#    который возвращает значение _radius.
# 4. Добавь метод radius (сеттер) с декоратором @radius.setter,
#    который принимает новое значение и проверяет:
#    - если значение > 0, сохраняет его в _radius
#    - если значение <= 0, ничего не меняет (просто пропускает)
# 5. Код должен содержать только объявление класса.
class  Circle:
    def __init__(self, radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value

# Задача №14 | Инкапсуляция (приватные атрибуты)
# 1. Создай класс Student.
# 2. Добавь конструктор, который принимает name и grade (оценка).
# 3. Сделай так, чтобы атрибут grade был "приватным" (с двумя подчёркиваниями в начале: __grade).
# 4. Добавь метод get_grade, который возвращает текущее значение __grade.
# 5. Добавь метод set_grade, который принимает новое значение и проверяет:
#    - если значение от 2 до 5 включительно, сохраняет его в __grade
#    - если значение вне этого диапазона, ничего не меняет
# 6. Код должен содержать только объявление класса.
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade
    def get_grade(self):
        return self.__grade
    def set_grade(self,new_grade):
        if 2 <= new_grade <= 5:
            self.__grade = new_grade

# Задача №15 | Магический метод __len__
# 1. Создай класс Playlist.
# 2. Добавь конструктор, который принимает название плейлиста (name)
#    и создаёт пустой список songs (атрибут экземпляра).
# 3. Добавь метод add_song, который принимает название песни и добавляет её в список songs.
# 4. Добавь магический метод __len__, который возвращает количество песен в плейлисте (длину списка songs).
# 5. Код должен содержать только объявление класса.
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    def add_song(self, name_song):
        self.songs.append(name_song)
    def __len__(self):
        return len(self.songs)

# Задача №16 | Сравнение объектов (__eq__)
# 1. Создай класс Product.
# 2. Добавь конструктор, который принимает name и price.
# 3. Добавь магический метод __eq__, который сравнивает два товара.
#    Два товара считаются равными, если у них одинаковые name И price.
# 4. Код должен содержать только объявление класса.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

# Задача №17 | Наследование (базовый класс)
# 1. Создай класс Animal.
# 2. Добавь конструктор, который принимает name и сохраняет как атрибут.
# 3. Добавь метод speak, который возвращает строку "Some sound".
# 4. Создай класс Dog, который наследует от Animal.
# 5. В классе Dog переопредели метод speak так, чтобы он возвращал "Woof!".
# 6. Код должен содержать только объявление классов.
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Some sound"
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Задача №18 | Наследование и super()
# 1. Создай класс Employee (сотрудник).
# 2. Добавь конструктор, который принимает name и salary.
# 3. Создай класс Manager, который наследует от Employee.
# 4. В конструкторе Manager добавь третий параметр department.
# 5. Используй super(), чтобы вызвать конструктор родителя и передать ему name и salary,
#    а department сохрани как атрибут экземпляра в самом Manager.
# 6. Код должен содержать только объявление классов.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def __init__(self,name, salary, department):
        super().__init__(name, salary)
        self.department = department

# Задача №19 | Множественное наследование
# 1. Создай класс Flyer с методом fly, который возвращает "Flying".
# 2. Создай класс Swimmer с методом swim, который возвращает "Swimming".
# 3. Создай класс Duck, который наследует от Flyer и Swimmer.
#    (Порядок наследования: сначала Flyer, потом Swimmer)
# 4. В классе Duck не нужно добавлять новые методы или конструктор.
# 5. Код должен содержать только объявление трёх классов.
class Flyer:
    def fly(self):
        return "Flying"
class Swimmer:
    def swim(self):
        return "Swimming"
class Duck(Flyer, Swimmer):

# Задача №20 | Методы и атрибуты экземпляра
# 1. Создай класс Smartphone.
# 2. Добавь конструктор, который принимает brand и model.
# 3. Добавь метод make_call, который принимает phone_number и возвращает строку:
#    "Calling {phone_number} from {brand} {model}"
# 4. Код должен содержать только объявление класса.
class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def make_call(self, phone_number):
        return f"Calling {phone_number} from {self.brand} {self.model}"

# Задача №21 | Общие атрибуты и метод класса
# 1. Создай класс Counter.
# 2. Добавь общий (классовый) атрибут count = 0.
# 3. Добавь метод __init__, который увеличивает общий счётчик count на 1 при создании каждого нового объекта.
# 4. Добавь классовый метод get_count, который возвращает текущее значение count.
# 5. Код должен содержать только объявление класса.
class Counter:
    count = 0
    def __init__(self):
        type(self).count += 1
    @classmethod
    def get_count(cls):
        return cls.count

# Задача №22 | Магический метод __str__
# 1. Создай класс Laptop.
# 2. Добавь конструктор, который принимает brand и ram (оперативная память в ГБ).
# 3. Добавь магический метод __str__, который возвращает строку:
#    "Ноутбук: {brand}, RAM: {ram} ГБ"
# 4. Код должен содержать только объявление класса.

class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram
    def __str__(self):
        return f"Ноутбук: {self.brand}, RAM: {self.ram} ГБ"

# Задача №23 | Статический метод
# 1. Создай класс StringUtils.
# 2. Добавь статический метод is_palindrome, который принимает строку
#    и возвращает True, если строка читается одинаково слева направо и справа налево,
#    и False в противном случае.
#    (Регистр букв учитывать, пробелы не удалять)
# 3. Код должен содержать только объявление класса.
class StringUtils:
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]

# Задача №24 | Композиция классов
# 1. Создай класс Engine.
# 2. Добавь конструктор, который принимает horsepower и сохраняет как атрибут.
# 3. Добавь метод start, который возвращает строку "Engine started".
# 4. Создай класс Car.
# 5. Добавь конструктор, который принимает brand и engine (объект класса Engine).
# 6. Добавь метод start, который вызывает метод start у объекта engine и возвращает его результат.
# 7. Код должен содержать только объявление двух классов.
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    def start(self):
        return "Engine started"
class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine
    def start(self):
        return self.engine.start()

# Задача №25 | Приватные атрибуты и геттеры
# 1. Создай класс User.
# 2. Добавь конструктор, который принимает username и password.
# 3. Сделай атрибут password приватным (__password).
# 4. Добавь метод check_password, который принимает строку
#    и возвращает True, если она совпадает с сохранённым паролём, иначе False.
# 5. Код должен содержать только объявление класса.
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
    def check_password(self, password):
        return password == self.__password

# Задача №26 | Магический метод __repr__
# 1. Создай класс Point.
# 2. Добавь конструктор, который принимает x и y.
# 3. Добавь магический метод __repr__, который возвращает строку:
#    f"Point({self.x}, {self.y})"
# 4. Код должен содержать только объявление класса.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Задача №27 | Свойства (property) - геттер и сеттер
# 1. Создай класс BankAccount.
# 2. Добавь конструктор, который принимает owner и balance (начальный баланс).
# 3. Сделай атрибут balance приватным (__balance).
# 4. Добавь свойство balance (геттер), которое возвращает текущий баланс.
# 5. Добавь сеттер для balance, который проверяет:
#    - если новое значение >= 0, то сохраняет его
#    - если новое значение < 0, то ничего не меняет
# 6. Код должен содержать только объявление класса.
class BankAccount:
    def __init__(self, owner,balance):
        self.owner = owner
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value

# Задача №28 | Наследование и переопределение методов
# 1. Создай класс Vehicle.
# 2. Добавь конструктор, который принимает brand и speed.
# 3. Добавь метод move, который возвращает строку "Транспорт движется".
# 4. Создай класс Car, который наследует от Vehicle.
# 5. Переопредели метод move так, чтобы он возвращал строку "Машина едет со скоростью {speed} км/ч".
# 6. Код должен содержать только объявление классов.
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def move(self):
        return "Транспорт движется"
class Car(Vehicle):
    def move(self):
        return f"Машина едет со скоростью {self.speed} км/ч"

# Задача №29 | super() в конструкторе
# 1. Создай класс Person.
# 2. Добавь конструктор, который принимает name и age.
# 3. Создай класс Student, который наследует от Person.
# 4. В конструкторе Student добавь третий параметр student_id.
# 5. Используй super(), чтобы вызвать конструктор Person и передать ему name и age.
# 6. student_id сохрани как атрибут экземпляра в классе Student.
# 7. Код должен содержать только объявление классов.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

# Задача №30 | Множественное наследование и порядок разрешения методов
# 1. Создай класс A с методом info, который возвращает "Class A".
# 2. Создай класс B с методом info, который возвращает "Class B".
# 3. Создай класс C, который наследует от A и B (в указанном порядке: сначала A, потом B).
# 4. В классе C НЕ переопределяй метод info.
# 5. Код должен содержать только объявление трёх классов.
class A:
    def info(self):
        return "Class A"
class B:
    def info(self):
        return "Class B"
class C(A,B):
    pass

# Задача №31 | Счётчик объектов
# 1. Создай класс Magic.
# 2. Добавь общий (классовый) атрибут spell_count = 0.
# 3. Добавь конструктор, который при создании каждого нового объекта увеличивает spell_count на 1.
# 4. Добавь классовый метод get_spell_count, который возвращает текущее значение spell_count.
# 5. Добавь метод cast_spell, который возвращает строку "Абракадабра!".
# 6. Код должен содержать только объявление класса.
class Magic:
    spell_count = 0
    def __init__(self):
        Magic.spell_count += 1
    @classmethod
    def get_spell_count(cls):
        return cls.spell_count
    def cast_spell(self):
        return "Абракадабра!"

# Задача №32 | Магический метод __add__
# 1. Создай класс Box.
# 2. Добавь конструктор, который принимает items (список предметов).
# 3. Добавь магический метод __add__, который объединяет две коробки.
#    При сложении box1 + box2 должен возвращаться новый объект Box,
#    у которого items = box1.items + box2.items.
# 4. Код должен содержать только объявление класса.
class Box:
    def __init__(self, items):
        self.items = items
    def __add__(self, other):
        return Box(self.items + other.items)

# Задача №33 | Композиция классов
# 1. Создай класс Author.
# 2. Добавь конструктор, который принимает name и country.
# 3. Создай класс Book.
# 4. Добавь конструктор, который принимает title и author (объект класса Author).
# 5. Добавь метод get_info, который возвращает строку:
#    f"'{title}' by {author.name} ({author.country})"
# 6. Код должен содержать только объявление двух классов.
class Author:
    def __init__(self, name, country):
        self.name = name
        self.country = country
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        return f"'{self.title}' by {self.author.name} ({self.author.country})"

# Задача №34 | Приватные атрибуты и методы доступа
# 1. Создай класс Wallet.
# 2. Добавь конструктор, который принимает owner и amount.
# 3. Сделай атрибут amount приватным (__amount).
# 4. Добавь метод add_money, который принимает сумму и увеличивает __amount на эту сумму.
# 5. Добавь метод get_amount, который возвращает текущее значение __amount.
# 6. Код должен содержать только объявление класса.
class Wallet:
    def __init__(self, owner, amount):
        self.owner = owner
        self.__amount = amount
    def add_money(self, sum_amount):
        self.__amount += sum_amount
    def get_amount(self):
        return self.__amount

# Задача №35 | Свойства (property) с вычисляемым значением
# 1. Создай класс Rectangle.
# 2. Добавь конструктор, который принимает width и height.
# 3. Сделай атрибуты width и height публичными (не приватными).
# 4. Добавь свойство area (только геттер), которое возвращает площадь прямоугольника.
# 5. Добавь свойство perimeter (только геттер), которое возвращает периметр.
# 6. Код должен содержать только объявление класса.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width * self.height
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)