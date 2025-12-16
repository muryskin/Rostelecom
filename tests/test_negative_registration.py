import time

import pytest
# from selenium.webdriver.common.by import By

from pages.auth_page import AuthPage

@pytest.mark.parametrize("Name", ["","QWERTY","Б","Ж"*31],
                         ids=["empty","latin","cyr 1","cyr over max"])
def test_registration_negative_name(web_browser,Name):
    """Негативное тестирование Имени при регистрации"""
    page = AuthPage(web_browser)
    time.sleep(3)

    # Нажимаем кнопку "Зарегистрироваться", чтобы перейти к регистрации
    page.registration.click()
    # корректные данные: Имя необходимо заполнить кириллицей. От 2 до 30 символов.
    page.reg_firstname.send_keys(Name)

    # Нажимаем кнопку "Зарегистрироваться"
    page.btn_submit_reg.click()

    time.sleep(1)
    # Проверяем, что некорректные данные в поле Имя вызывают ошибку
    assert page.name_error.is_visible()
    page.close()

@pytest.mark.parametrize("Name", ["","QWERTY","Б","Ж"*31],
                         ids=["empty","latin","cyr 1","cyr over max"])
def test_registration_negative_lastname(web_browser,Name):
    """Негативное тестирование Фамилии при регистрации"""
    page = AuthPage(web_browser)
    time.sleep(3)

    # Нажимаем кнопку "Зарегистрироваться", чтобы перейти к регистрации
    page.registration.click()
    # корректные данные: Фамилию необходимо заполнить кириллицей. От 2 до 30 символов.
    page.reg_lastname.send_keys(Name)

    # Нажимаем кнопку "Зарегистрироваться"
    page.btn_submit_reg.click()

    time.sleep(1)
    # Проверяем, что некорректные данные в поле Фамилия вызывают ошибку
    assert page.name_error.is_visible()
    page.close()

def test_registration_negative_region(web_browser):
    """Негативное тестирование Региона при регистрации"""
    page = AuthPage(web_browser)
    time.sleep(3)

    # Нажимаем кнопку "Зарегистрироваться", чтобы перейти к регистрации
    page.registration.click()
    # Оставляем поле пустым
    # page.reg_region.send_keys("")

    # Нажимаем кнопку "Зарегистрироваться"
    page.btn_submit_reg.click()

    time.sleep(1)
    # Проверяем, что некорректные данные в поле Регион вызывают ошибку
    assert page.region_error.is_visible()
    page.close()

@pytest.mark.parametrize("phone", ["","1","3"*12],
                         ids=["empty", "one", "over max"])
def test_registration_negative_phone(web_browser,phone):
    """Негативное тестирование Номера Телефона при регистрации"""
    page = AuthPage(web_browser)
    time.sleep(3)

    # Нажимаем кнопку "Зарегистрироваться", чтобы перейти к регистрации
    page.registration.click()
    # корректные данные: телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX
    page.reg_address.send_keys(phone)

    # Нажимаем кнопку "Зарегистрироваться"
    page.btn_submit_reg.click()

    time.sleep(1)
    # Проверяем, что некорректные данные в поле Телефон вызывают ошибку
    assert page.email_phone_error.is_visible()
    page.close()

@pytest.mark.parametrize("email", ["","q","@","q@","@q",".ru","q.ru",
                                   "@.ru","q@.ru","@q.ru"])
def test_registration_negative_email(web_browser,email):
    """Негативное тестирование Email при регистрации"""
    page = AuthPage(web_browser)
    time.sleep(3)

    # Нажимаем кнопку "Зарегистрироваться", чтобы перейти к регистрации
    page.registration.click()
    # корректные данные: email в формате example@email.ru
    page.reg_address.send_keys(email)

    # Нажимаем кнопку "Зарегистрироваться"
    page.btn_submit_reg.click()

    time.sleep(1)
    # Проверяем, что некорректные данные в поле Email вызывают ошибку
    assert page.email_phone_error.is_visible()
    page.close()

@pytest.mark.parametrize("Pass", ["","1Ab","1"*8,"A"*8,"b"*8,
                                  "1"*20,"A"*20,"b"*20,
                                  "1A"*5,"1b"*5,"Ab"*5,"1Ab"+"!"*18],
                         ids=["empty", "less min", "min 8 digit", "min 8 UP", "min 8 down",
                              "max 20 digit", "max 20 UP", "max 20 down",
                              "digit+UP", "digit+down", "UP+down", "over max"])
def test_registration_negative_password(web_browser,Pass):
    """Негативное тестирование Пароля при регистрации"""
    page = AuthPage(web_browser)
    time.sleep(3)

    # Нажимаем кнопку "Зарегистрироваться", чтобы перейти к регистрации
    page.registration.click()
    # корректные данные:
    # Длина пароля должна быть не менее 8 символов
    # Длина пароля должна быть не более 20 символов
    # Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру
    # Пароль должен содержать хотя бы одну заглавную букву
    # Пароль должен содержать хотя бы одну строчную букву
    page.reg_password.send_keys(Pass)

    # Нажимаем кнопку "Зарегистрироваться"
    page.btn_submit_reg.click()

    time.sleep(1)
    # Проверяем, что некорректные данные в поле Пароль вызывают ошибку
    assert page.password_error.is_visible()
    page.close()

def test_registration_negative_password_confirm(web_browser,Pass="k<YdPjIF!,BY5=X"):
    """Негативное тестирование Подтверждения Пароля при регистрации"""
    page = AuthPage(web_browser)
    time.sleep(3)

    # Нажимаем кнопку "Зарегистрироваться", чтобы перейти к регистрации
    page.registration.click()
    # вводим корректный пароль
    page.reg_password.send_keys(Pass)
    # поле Подтверждения Пароля оставляем пустым
    page.reg_password_confirm.send_keys('')

    # Нажимаем кнопку "Зарегистрироваться"
    page.btn_submit_reg.click()

    time.sleep(1)
    # Проверяем, что некорректные данные в поле Подтверждение пароля вызывают ошибку
    assert page.password_confirm_error.is_visible()
    page.close()
