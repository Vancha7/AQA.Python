# Задача 1: XPath. Базовый поиск элемента
# Найдите элемент <employee> на странице, используя XPath
employee = driver.find_element("xpath",'//employee' )
assert employee is not None, "Элемент employee не найден"
print("✓ Элемент employee успешно найден!")


# Задача 2: XPath. Поиск вложенного элемента
# Дана HTML структура:
# <employee id="1">
#     <name>David</name>     <--- Вот этот элемент нужно найти!
#     <age>30</age>
# </employee>
# <employee id="2">
#     <name>John</name>
#     <age>25</age>
# </employee>
# Найдите элемент <name>, который находится ВНУТРИ элемента <employee>
name_in_employee = driver.find_element("xpath", "//employee/name" )

# Задача 3: XPath. Поиск по атрибуту
# Дана HTML структура:
# <employee id="1">
#     <name>David</name>
#     <age>30</age>
# </employee>
# <employee id="2">
#     <name>John</name>      <--- Нужно найти John, но только у employee с id="2"
#     <age>25</age>
# </employee>
# <employee id="3">
#     <name>Sarah</name>
#     <age>28</age>
# </employee>
# Найдите элемент <name> у сотрудника с id="2"
name_of_employee_2 = driver.find_element("xpath", '//employee[@id = "2"]/name')

# Задача 4: XPath. Поиск по тексту
# Дана HTML структура:
# <employee id="1">
#     <name>David</name>
#     <position>Developer</position>     <--- Нужно найти эту должность
# </employee>
# <employee id="2">
#     <name>John</name>
#     <position>Manager</position>
# </employee>
# <employee id="3">
#     <name>Sarah</name>
#     <position>Designer</position>
# </employee>
# Найдите элемент <position> у сотрудника, который занимает должность Developer
developer_position = driver.find_element("xpath", "//position[text()='Developer']")

# Задача 5: XPath. Поиск родителя
# Дана HTML структура:
# <employees>
#     <employee id="1">
#         <name>David</name>
#         <position>Developer</position>
#     </employee>
#     <employee id="2">
#         <name>John</name>
#         <position>Manager</position>
#     </employee>
#     <employee id="3">
#         <name>Sarah</name>
#         <position>Designer</position>   <--- Найдите employee для этой должности
#     </employee>
# </employees>
# Найдите элемент <employee>, внутри которого есть <position> с текстом 'Designer'
# Используйте найденный в прошлой задаче XPath как часть решения
employee_with_designer = driver.find_element("xpath", '//employee[position="Designer"]')

# Задача 6: XPath. Поиск по частичному совпадению (простая)
# Дана HTML структура:
# <book id="book-123">Harry Potter</book>
# <book id="book-456">Lord of the Rings</book>
# <book id="novel-789">The Hobbit</book>
# Найдите элемент <book>, у которого id начинается с "book" (используйте contains)
book = driver.find_element("xpath", "//book[contains(id,'book')]")

# Задача 7: XPath. Поиск по началу текста (starts-with)
# Дана HTML структура:
# <fruit>apple</fruit>
# <fruit>apricot</fruit>
# <fruit>banana</fruit>
# <fruit>orange</fruit>
# Найдите все фрукты, название которых начинается с "ap"
fruits_starting_with_ap = driver.find_elements("xpath", "//fruit[starts-with(text(),'ap')]")

# Задача 8: XPath. Поиск по нескольким условиям (and)
# Дана HTML структура:
# <user role="admin" status="active">John</user>
# <user role="admin" status="inactive">Jane</user>
# <user role="user" status="active">Bob</user>
# <user role="user" status="inactive">Alice</user>
# Найдите активного администратора (role="admin" И status="active")
admin_active = driver.find_element("xpath", "//user[@role = 'admin' and @status = 'active']")

# Задача 9: XPath. Поиск по нескольким условиям (or)
# Дана HTML структура:
# <product category="electronics" price="1000">Laptop</product>
# <product category="books" price="25">Python Book</product>
# <product category="electronics" price="50">Mouse</product>
# <product category="clothes" price="30">T-shirt</product>
# Найдите товары, которые либо относятся к электронике, либо стоят дороже 500
products = driver.find_elements("xpath", "//product[@category = 'electronics' or number(@price) > 500]")

# Задача 10: XPath. Последний элемент (last())
# Дана HTML структура:
# <ul>
#     <li>Первый элемент</li>
#     <li>Второй элемент</li>
#     <li>Третий элемент</li>  <--- Найдите последний элемент
#     <li>Четвертый элемент</li>
# </ul>
# Найдите последний элемент <li> в списке
last_item = driver.find_element("xpath", "//ul/li[last()]")

# Задача 11: XPath. Первый элемент
# Дана та же структура:
# <ul>
#     <li>Первый элемент</li>  <--- Найдите первый элемент
#     <li>Второй элемент</li>
#     <li>Третий элемент</li>
#     <li>Четвертый элемент</li>
# </ul>
# Найдите первый элемент <li> в списке
first_item = driver.find_element("xpath", "//ul/li[1]")

# Задача 12: XPath. Поиск по позиции
# Дана HTML структура:
# <div class="menu">
#     <a href="/home">Главная</a>
#     <a href="/news">Новости</a>      <--- Найдите эту ссылку
#     <a href="/contact">Контакты</a>
#     <a href="/about">О нас</a>
# </div>
# Найдите второй элемент ссылки (<a>) в меню
second_link = driver.find_element("xpath", "//div/a[position()=2]")

# Задача 13: XPath. Комбинируем contains и атрибуты
# Дана HTML структура:
# <input class="login-input" type="text" placeholder="Введите имя">
# <input class="login-input" type="password" placeholder="Введите пароль">
# <input class="login-input" type="email" placeholder="Введите email" value="test@mail.com">
# <button class="login-btn">Войти</button>
# Найдите поле ввода email (input), у которого в классе есть слово "login-input" И тип "email"
email_field = driver.find_element("xpath", "//input[contains(@class,'login-input') and @type = 'email']")

# Задача 14: XPath. Ищем по тексту и атрибуту
# Дана HTML структура:
# <div class="product">
#     <h3>iPhone 15</h3>
#     <span class="price">$999</span>
#     <button class="add-to-cart">Купить</button>
# </div>
# <div class="product">
#     <h3>MacBook Pro</h3>
#     <span class="price">$1999</span>
#     <button class="add-to-cart">Купить</button>  <--- Найдите эту кнопку
# </div>
# <div class="product">
#     <h3>iPad Air</h3>
#     <span class="price">$599</span>
#     <button class="add-to-cart">Купить</button>
# </div>
# Найдите кнопку "Купить" для товара "MacBook Pro"
buy_button = driver.find_element("xpath", "//div[.//h3='MacBook Pro']//button[text()='Купить']")

# Задача 15: XPath. Сложный поиск (итоговая)
# Дана HTML структура:
# <div class="catalog">
#     <div class="category">
#         <h2>Электроника</h2>
#         <div class="item">
#             <span class="name">Ноутбук</span>
#             <span class="price">1000</span>
#         </div>
#     </div>
#     <div class="category">
#         <h2>Книги</h2>
#         <div class="item">
#             <span class="name">Python для начинающих</span>  <--- Найдите цену этой книги
#             <span class="price">50</span>
#         </div>
#         <div class="item">
#             <span class="name">Java для профи</span>
#             <span class="price">75</span>
#         </div>
#     </div>
# </div>
# Найдите цену (элемент с классом "price") для книги "Python для начинающих"
price = driver.find_element("xpath", "//div[@class='item'][.//span[@class='name' and text()='Python для начинающих']]//span[@class='price']")


# Задача 16: XPath. Поиск по тегу
# Дана HTML структура:
# <html>
#     <body>
#         <h1>Заголовок страницы</h1>
#         <p>Первый параграф</p>
#         <p>Второй параграф</p>
#         <button>Нажми меня</button>
#     </body>
# </html>
# Найдите все элементы <p> (параграфы) на странице
paragraphs = driver.find_elements("xpath", "//body/p")

# Задача 17: XPath. Поиск по атрибуту class
# Дана HTML структура:
# <div class="header">Шапка сайта</div>
# <div class="menu">Главная О нас Контакты</div>
# <div class="content">Основное содержание</div>
# <div class="footer">Подвал сайта</div>
# Найдите элемент с классом "menu"
menu = driver.find_element("xpath", "//div[@class = 'menu']")