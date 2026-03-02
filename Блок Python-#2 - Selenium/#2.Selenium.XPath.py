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

# Задача 17: XPath. Поиск по атрибуту class
# Дана HTML структура:
# <div class="header">Шапка сайта</div>
# <div class="menu">Главная О нас Контакты</div>
# <div class="content">Основное содержание</div>
# <div class="footer">Подвал сайта</div>
# Найдите элемент с классом "menu"
menu = driver.find_element("xpath", "//div[@class = 'menu']")

# Задача 18: XPath. Поиск по тексту
# Дана HTML структура:
# <button>Отправить</button>
# <button>Сохранить</button>
# <button>Отмена</button>
# <button>Удалить</button>
# Найдите кнопку с текстом "Сохранить"
save_button = driver.find_element("xpath", "//button[text()='Сохранить']")

# Задача 19: XPath. Поиск по нескольким атрибутам
# Дана HTML структура:
# <input type="text" name="username" placeholder="Введите имя">
# <input type="password" name="password" placeholder="Введите пароль">
# <input type="email" name="email" placeholder="Введите email">
# <input type="text" name="phone" placeholder="Введите телефон">
# Найдите поле ввода с type="text" И name="username"
username_field = driver.find_element("xpath", "//input[@type='text' and @name='username']")

# Задача 20: XPath. Поиск по части атрибута (contains)
# Дана HTML структура:
# <img src="/images/logo.png" alt="Логотип компании">
# <img src="/photos/product1.jpg" alt="Фото товара 1">
# <img src="/photos/product2.jpg" alt="Фото товара 2">
# <img src="/icons/settings.png" alt="Иконка настроек">
# Найдите все изображения, у которых в атрибуте src есть слово "photos"
product_photos = driver.find_elements("xpath", "//img[contains(@src, 'photos')]")

# Задача 21: XPath. Поиск по части текста (contains)
# Дана HTML структура:
# <h2>Товар: Ноутбук Apple MacBook</h2>
# <h2>Товар: Смартфон Samsung Galaxy</h2>
# <h2>Товар: Планшет iPad Air</h2>
# <h2>Товар: Наушники Sony</h2>
# Найдите все заголовки, в тексте которых есть слово "Apple"
apple_products = driver.find_elements("xpath", "//h2[contains(text(),'Apple')]")

# Задача 22: XPath. Поиск по началу текста (starts-with)
# Дана HTML структура:
# <a href="/home">Главная</a>
# <a href="/products/new">Новые товары</a>
# <a href="/products/popular">Популярные товары</a>
# <a href="/contacts">Контакты</a>
# Найдите все ссылки, у которых текст начинается со слова "Новые"
new_links = driver.find_elements("xpath", "//a[starts-with(text(),'Новые')]")

# Задача 23: XPath. Комбинация тегов и атрибутов
# Дана HTML структура:
# <div id="header">
#     <span class="title">Мой сайт</span>
# </div>
# <div id="content">
#     <span class="title">Добро пожаловать!</span>
#     <p class="text">Рады видеть вас на нашем сайте</p>
# </div>
# <div id="footer">
#     <span class="title">Контакты</span>
#     <p>Email: info@site.com</p>
# </div>
# Найдите элемент span с классом "title", который находится внутри div с id="content"
content_title = driver.find_element("xpath", "//div[@id='content']//span[@class = 'title']")

# Задача 24: XPath. Поиск родителя
# Дана HTML структура:
# <div class="product">
#     <h3>Кофеварка</h3>
#     <span class="price">4990 руб.</span>
#     <button class="buy">Купить</button>
# </div>
# <div class="product">
#     <h3>Микроволновка</h3>      <--- От этого элемента начнем поиск
#     <span class="price">8990 руб.</span>
#     <button class="buy">Купить</button>
# </div>
# <div class="product">
#     <h3>Холодильник</h3>
#     <span class="price">24990 руб.</span>
#     <button class="buy">Купить</button>
# </div>
# Найдите цену товара "Микроволновка" (используйте поиск по h3 и подъем к родителю)
price = driver.find_element("xpath", "//div[.//h3='Микроволновка']//span[@class='price']")

# Задача 25: XPath. Поиск по нескольким условиям (последняя базовая)
# Дана HTML структура:
# <ul>
#     <li class="completed">Купить хлеб</li>
#     <li class="active">Сделать уроки</li>
#     <li class="completed">Позвонить маме</li>
#     <li class="active">Выучить XPath</li>  <--- Найдите этот элемент
#     <li class="pending">Посмотреть фильм</li>
# </ul>
# Найдите активный элемент (class="active") с текстом "Выучить XPath"
task = driver.find_element("xpath", "//li[@class='active' and text()='Выучить XPath']")

# Задача 26: XPath. Поиск по нескольким классам
# Дана HTML структура:
# <div class="card">Простая карточка</div>
# <div class="card featured">Рекомендуемый товар</div>
# <div class="card new">Новый товар</div>
# <div class="card featured hot">Горячее предложение</div>  <--- Найдите этот div
# <div class="card">Обычный товар</div>
# Найдите div, у которого есть класс "featured" И класс "hot" одновременно
featured_hot = driver.find_element("xpath", "//div[contains(@class, 'featured') and contains(@class, 'hot')]")

# Задача 27: XPath. Поиск по позиции (первый и последний)
# Дана HTML структура:
# <ul>
#     <li>Понедельник</li>
#     <li>Вторник</li>
#     <li>Среда</li>
#     <li>Четверг</li>
#     <li>Пятница</li>
# </ul>
# Найдите первый и последний дни недели
first_day = driver.find_element("xpath", "//ul/li[1]")  # Должен найти "Понедельник"
last_day = driver.find_element("xpath", "//ul/li[last()]")   # Должен найти "Пятница"

# Задача 28: XPath. Поиск по отсутствию атрибута
# Дана HTML структура:
# <input name="username" placeholder="Имя">
# <input name="email" placeholder="Email" required>
# <input name="password" placeholder="Пароль" required>
# <input name="phone" placeholder="Телефон">
# Найдите все поля, у которых НЕТ атрибута "required"
not_required_fields = driver.find_elements("xpath","//input[not(@required)]")

# Задача 29: XPath. Поиск по нескольким условиям (or)
# Дана HTML структура:
# <div class="alert success">Операция выполнена успешно</div>
# <div class="alert warning">Внимание! Проверьте данные</div>
# <div class="alert error">Ошибка ввода</div>
# <div class="alert info">Новое сообщение</div>
# Найдите все сообщения с классом "success" ИЛИ с классом "error"
success_or_error = driver.find_elements("xpath", "//div[@class='success' or @class='error']")

# Задача 30: XPath. Комбинируем всё (последняя задача)
# Дана HTML структура:
# <table>
#     <tr>
#         <td>Иван</td>
#         <td>Петров</td>
#         <td>25 лет</td>
#         <td>Москва</td>
#     </tr>
#     <tr>
#         <td>Мария</td>
#         <td>Иванова</td>
#         <td>30 лет</td>
#         <td>СПб</td>
#     </tr>
#     <tr>
#         <td>Петр</td>              <--- Найдите возраст этого человека
#         <td>Сидоров</td>
#         <td>28 лет</td>
#         <td>Казань</td>
#     </tr>
# </table>
# Найдите возраст Петра Сидорова (ячейку с текстом "28 лет")
age = driver.find_element("xpath", "//tr[.//td[contains(text(),'Петр')]]//td[3]")

# Задача 31: XPath. Поиск по ID
# Дана HTML структура:
# <div id="header">Шапка</div>
# <div id="content">Контент</div>
# <div id="footer">Подвал</div>
# Найдите элемент с id="content"
content = driver.find_element("xpath", "//div[@id = 'content']")

# Задача 32: XPath. Поиск по имени тега
# Дана HTML структура:
# <h1>Заголовок</h1>
# <h2>Подзаголовок</h2>
# <h3>Раздел 1</h3>
# <h3>Раздел 2</h3>
# Найдите все элементы <h3>
h3_elements = driver.find_elements("xpath", "//h3")

# Задача 33: XPath. Поиск по атрибуту name
# Дана HTML структура:
# <input name="search" placeholder="Поиск...">
# <input name="email" placeholder="Email">
# <input name="password" type="password">
# Найдите поле с именем "search"
search_field = driver.find_element("xpath", "//input[@name='search']")

# Задача 34: XPath. Поиск по типу (type)
# Дана HTML структура:
# <input type="text" placeholder="Имя">
# <input type="email" placeholder="Email">
# <input type="password" placeholder="Пароль">
# <input type="submit" value="Отправить">
# Найдите кнопку отправки формы (input с type="submit")
submit_button = driver.find_element("xpath", "//input[@type = 'submit']")

# Задача 35: XPath. Поиск по нескольким атрибутам (последняя базовая)
# Дана HTML структура:
# <a href="/home" class="nav-link">Главная</a>
# <a href="/products" class="nav-link">Товары</a>
# <a href="/contacts" class="nav-link">Контакты</a>
# <a href="/login" class="btn">Войти</a>
# Найдите ссылку с классом "nav-link" и текстом "Товары"
products_link = driver.find_element("xpath", "//a[@class = 'nav-link' and text()='Товары']")

# Задача 36: XPath. Поиск по вложенности
# Дана HTML структура:
# <div class="container">
#     <p>Первый параграф</p>
#     <div class="inner">
#         <p>Второй параграф</p>  <--- Найдите этот параграф
#     </div>
#     <p>Третий параграф</p>
# </div>
# Найдите параграф, который находится внутри div с классом "inner"
inner_paragraph = driver.find_element("xpath", "//div[@class = 'inner']/p")

# Задача 37: XPath. Поиск по части атрибута href
# Дана HTML структура:
# <a href="https://google.com">Google</a>
# <a href="https://youtube.com">YouTube</a>
# <a href="https://mail.google.com">Gmail</a>
# <a href="https://maps.google.com">Google Maps</a>
# Найдите все ссылки, в адресе которых есть "google"
google_links = driver.find_elements("xpath", "//a[contains(@href, 'google')]")

# Задача 38: XPath. Поиск элемента, который НЕ содержит текст
# Дана HTML структура:
# <p>Доступно</p>
# <p>Недоступно</p>
# <p>В ожидании</p>
# <p></p>  <--- Пустой параграф
# <p>Доступно</p>
# Найдите все НЕпустые параграфы (которые содержат какой-то текст)
non_empty_paragraphs = driver.find_elements("xpath", "//p[not(text()='')]")

# Задача 39: XPath. Поиск по позиции (четные/нечетные)
# Дана HTML структура:
# <ul>
#     <li>Элемент 1</li>
#     <li>Элемент 2</li>
#     <li>Элемент 3</li>
#     <li>Элемент 4</li>
#     <li>Элемент 5</li>
#     <li>Элемент 6</li>
# </ul>
# Найдите все четные элементы списка (2, 4, 6)
even_elements = driver.find_elements("xpath", "//li[position() mod 2 = 0]")

# Задача 40 (упрощенная): XPath. Поиск по нескольким условиям
# Дана HTML структура:
# <div class="product available" data-price="50000">Ноутбук</div>
# <div class="product unavailable" data-price="20000">Планшет</div>
# <div class="product available" data-price="30000">Смартфон</div>
# <div class="product available" data-price="5000">Наушники</div>
# <div class="product unavailable" data-price="15000">Монитор</div>
# Найдите все доступные товары (class содержит "available") с ценой больше 10000
# (цена хранится в атрибуте data-price)
expensive_available = driver.find_elements("xpath", "//div[contains(@class, 'available') and number(@data-price) > 10000]")