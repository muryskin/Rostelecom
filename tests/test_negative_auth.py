import time
import pytest
from pages.auth_page import AuthPage

@pytest.mark.parametrize("Name", ["","1","2"*11,"8"*11,"9"*11,"0"*12],
                         ids=["empty","one","max_not_7_or_8","max_7_or_8",
                              "over_max_not_7_or_8","over_max_7_or_8"])
def test_authorisation_negative_phone(web_browser,Name):
    """Негативное тестирование авторизации с использованием
    различных сочетаний некорректного номера телефона и пароля"""
    page = AuthPage(web_browser)

    # выбираем способ авторизации: по номеру телефона (макс 11 символов)
    page.btn_phone.click()

    # вводим некорректные данные для телефона и пароля
    page.username.send_keys(Name)
    page.password.send_keys("incorrect_password")

    # нажимаем кнопку "Войти"
    page.btn.click()
    time.sleep(1)
    # проверяем, что видна форма с сообщением об ошибке авторизации
    assert page.form_error.is_visible() or page.login_error.is_visible()
    # проверяем, что текущая страница - это не страница профиля "Вход и безпасность"
    assert page.get_current_url()[:43] != 'https://b2c.passport.rt.ru/account_b2c/page'
    page.close()

@pytest.mark.parametrize("Name", ["","a","@","a@a.ru"],
                         ids=["empty","one symbol","@ symbol","incorrect"])
def test_authorisation_negative_email(web_browser,Name):
    """Негативное тестирование авторизации с использованием
    различных сочетаний некорректного email адреса и пароля"""
    page = AuthPage(web_browser)

    # выбираем способ авторизации: по email адресу
    page.btn_email.click()

    # вводим некорректные данные для почты и пароля
    page.username.send_keys(Name)
    page.password.send_keys("incorrect_password")

    # нажимаем кнопку "Войти"
    page.btn.click()
    time.sleep(1)
    # проверяем, что видна форма с сообщением об ошибке авторизации
    assert page.form_error.is_visible() or page.login_error.is_visible()
    # проверяем, что текущая страница - это не страница профиля "Вход и безпасность"
    assert page.get_current_url()[:43] != 'https://b2c.passport.rt.ru/account_b2c/page'
    page.close()

@pytest.mark.parametrize("Name", ["","a","b"*19,"c"*20],
                         ids=["empty","one","max","over_max"])
def test_authorisation_negative_login(web_browser,Name):
    """Негативное тестирование авторизации с использованием
    различных сочетаний некорректного логина и пароля"""
    page = AuthPage(web_browser)

    # выбираем способ авторизации: по логину (макс 19 символов)
    page.btn_login.click()

    # вводим некорректные данные для логина и пароля
    page.username.send_keys(Name)
    page.password.send_keys("incorrect_password")
    time.sleep(1)

    # нажимаем кнопку "Войти"
    page.btn.click()
    time.sleep(1)
    # проверяем, что видна форма с сообщением об ошибке авторизации
    assert page.form_error.is_visible() or page.login_error.is_visible()
    # проверяем, что текущая страница - это не страница профиля "Вход и безпасность"
    assert page.get_current_url()[:43] != 'https://b2c.passport.rt.ru/account_b2c/page'
    page.close()

@pytest.mark.parametrize("Name", ["","1","2"*12,"3"*13],
                         ids=["empty","one","max","over_max"])
def test_authorisation_negative_ls(web_browser,Name):
    """Негативное тестирование авторизации с использованием
    различных сочетаний некорректного номера лицевого счета и пароля"""
    page = AuthPage(web_browser)

    # выбираем способ авторазации: по номеру лицевого счета (макс 12 символов)
    page.btn_ls.click()

    # вводим некорректные данные для номера ЛС и пароля
    page.username.send_keys(Name)
    page.password.send_keys("incorrect_password")

    # нажимаем кнопку "Войти"
    page.btn.click()
    time.sleep(1)
    # проверяем, что видна форма с сообщением об ошибке авторизации
    assert page.form_error.is_visible() or page.login_error.is_visible()
    # проверяем, что текущая страница - это не страница профиля "Вход и безпасность"
    assert page.get_current_url()[:43] != 'https://b2c.passport.rt.ru/account_b2c/page'
    page.close()
