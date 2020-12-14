"""Задание: запуск автотестов для разных языков интерфейса"""

import time # Для вызова time.sleep(30)

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_backet_is_exists(browser):
    browser.get(link)
    # Раскомментируйте строку ниже для проверки с --language=fr
    # time.sleep(30)
    button = len(browser.find_elements_by_class_name("btn-add-to-basket"))
    assert button > 0,"Кнопка 'Добавить в корзину' не найдена"
