# pytest --lf - запускает упавшие в прошлом запуске тесты.
# pytest -sv --reruns=2 попробует перезапустить упавший тест n раз, сразу после падения
# pytest -sv --reruns=2 --reruns-delay=3 создает паузу между перезапусками
# pytest -sv --maxfail=2  данный параметр выставляет кол-во упавших тестов при котором, все авто-тесты остановятся. Параметр n - кол-во упавших тестов
# @pytest.mark.имя_маркера - имя маркера может быть любым. smoke, sanity, regression - это лишь простые примеры.
# pytest -sv -m smoke -m маркер - запустит тесты под нужным маркером
# pytest -sv -m "smoke or regression" - запустит кейсы под двумя маркерами.
# pytest практика\test_my.py -sv        Рекомендовано.
# pytest --lf - запускает упавшие в прошлом запуске тесты.
# Можно использовать в связке: # pytest практика/test_my2.py -sv --lf
# pytest project\test_demqa.py -sv



#Allure
# Pytest --alluredir=allure-results
#1 pytest практика/test_example.py --alluredir=allure-results
#2 allure serve allure-results  (Получаем allure отчет)
#3 pytest практика/test_example.py --alluredir=allure-results --clean-alluredir (удалит результаты прошлых запусков)



# Маркировка шагов
#
# def test_open_login_page(self):
#     with allure.step("Open page. Step 1"):   = маркировка
#         self.driver.get("https://demoqa.com/login")
#
#     with allure.step("Assert open page. Step 2"):
#         assert self.driver.current_url == "https://demoqa.com/login", "Ошибка ULR страницы входа"