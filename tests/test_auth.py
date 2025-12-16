import time

import pytest

from pages.auth_page import AuthPage

def test_authorisation_phone(web_browser):
    """Тестирование авторизации с использованием
    корректного номера телефона и пароля"""
    page = AuthPage(web_browser)
    time.sleep(1)
    # выбираем способ авторизации: по номеру телефона
    page.btn_phone.click()
    # вводим корректные данные для номера телефона и пароля
    page.username.send_keys('89996665544') # 11-значный номер сотового телефона
    page.password.send_keys("&W;Ux[nm9h@V1HA")

    # нажимаем кнопку "Войти"
    page.btn.click()
    time.sleep(1)

    # проверяем, что текущая страница - это страница профиля "Вход и безпасность"
    assert page.get_current_url()[:43] == 'https://b2c.passport.rt.ru/account_b2c/page'
    page.close()

def test_authorisation_email(web_browser):
    """Тестирование авторизации с использованием
    корректной почты и пароля"""
    page = AuthPage(web_browser)
    time.sleep(1)
    # выбираем способ авторизации: по email адресу
    page.btn_email.click()
    # вводим корректные данные для почты и пароля
    page.username.send_keys('example@mail.com')
    page.password.send_keys("&W;Ux[nm9h@V1HA")

    # нажимаем кнопку "Войти"
    page.btn.click()
    time.sleep(1)

    # проверяем, что текущая страница - это страница профиля "Вход и безпасность"
    assert page.get_current_url()[:43] == 'https://b2c.passport.rt.ru/account_b2c/page'
    page.close()

def test_authorisation_login(web_browser):
    """Тестирование авторизации с использованием
    корректного логина и пароля"""
    page = AuthPage(web_browser)
    time.sleep(1)
    # выбираем способ авторизации: по логину
    page.btn_login.click()
    # вводим корректные данные для логина и пароля
    page.username.send_keys('rtkid_1234567890123')
    page.password.send_keys("&W;Ux[nm9h@V1HA")

    # нажимаем кнопку "Войти"
    page.btn.click()
    time.sleep(1)

    # проверяем, что текущая страница - это страница профиля "Вход и безпасность"
    assert page.get_current_url()[:43] == 'https://b2c.passport.rt.ru/account_b2c/page'
    page.close()

@pytest.mark.xfail(reason="у меня нет номера ЛС, поэтому введены произвольные числа. "
                          "для успешного теста их необходимо заменить на корректный номер ЛС")
def test_authorisation_ls(web_browser):
    """Тестирование авторизации с использованием
    корректного номера лицевого счета и пароля"""
    page = AuthPage(web_browser)
    time.sleep(1)
    # выбираем способ авторизации: по номеру ЛС
    page.btn_ls.click()

    # вводим корректные данные для номера ЛС и пароля
    # у меня нет номера ЛС, поэтому введены произвольные числа
    # для успешного теста их необходимо заменить на корректный номер ЛС
    page.username.send_keys('123456789012') # 12-значный номер лицевого счета
    page.password.send_keys("&W;Ux[nm9h@V1HA")

    # нажимаем кнопку "Войти"
    page.btn.click()
    time.sleep(1)

    # проверяем, что текущая страница - это страница профиля "Вход и безпасность"
    assert page.get_current_url()[:43] == 'https://b2c.passport.rt.ru/account_b2c/page'
    page.close()
