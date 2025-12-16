import time

import pytest

from pages.auth_page import AuthPage

def test_password_recovery_phone(web_browser, name = '89991112233',
                                 new_pass='R9Gmbz{&XarR/;E'):
    """Тестирование восстановления пароля с использованием
        корректного номера телефона"""
    page = AuthPage(web_browser)
    time.sleep(2)
    # нажимаем кнопку "Забыл пароль"
    page.btn_forgot_pass.click()

    # выбираем способ авторизации: по номеру телефона
    page.btn_phone.click()
    # вводим телефон
    page.username.send_keys(name)

    # ручной ввод капчи, за 10 секунд
    if page.img_captcha.is_visible():
        page.captcha.click()
        time.sleep(10) # время для ручного ввода captcha
    time.sleep(1)
    # нажимаем кнопку "Продолжить"
    page.btn_reset.click()
    time.sleep(2)

    # ручной ввод кода подтверждения
    # время для ручного ввода кода из СМС/email
    time.sleep(60)

    # ввод нового пароля и подтверждения
    page.password_new.send_keys(new_pass)
    page.password_confirm.send_keys(new_pass)
    # нажатие на кнопку "Подтвердить сброс пароля"
    page.btn_confirm_reset.click()

    # проверяем работу авторизации по новому паролю, т.е. пароль успешно сменен
    # выбираем способ авторизации: по номеру телефона
    page.btn_email.click()
    page.btn_phone.click()
    # входим в личный кабинет с номером телефона и новым паролем
    page.username.clear()
    page.username.send_keys(name)
    page.password.send_keys(new_pass)
    # нажимаем кнопку "Войти"
    page.btn.click()
    time.sleep(1)
    # проверяем, что текущая страница - это страница профиля "Вход и безопасность"
    assert page.get_current_url()[:43] == 'https://b2c.passport.rt.ru/account_b2c/page'
    page.close()

def test_password_recovery_email(web_browser, name = 'example@mail.com',
                                 new_pass='R9Gmbz{&XarR/;E'):
    """Тестирование восстановления пароля с использованием
        корректного email адреса"""
    page = AuthPage(web_browser)
    time.sleep(2)
    # нажимаем кнопку "Забыл пароль"
    page.btn_forgot_pass.click()

    # выбираем способ авторизации: по email
    page.btn_email.click()
    # вводим email
    page.username.send_keys(name)

    # ручной ввод капчи, за 10 секунд
    if page.img_captcha.is_visible():
        page.captcha.click()
        time.sleep(10) # время для ручного ввода captcha
    time.sleep(1)
    # нажимаем кнопку "Продолжить"
    page.btn_reset.click()
    time.sleep(2)

    # ручной ввод кода подтверждения
    # время для ручного ввода кода из СМС/email
    time.sleep(60)

    # ввод нового пароля и подтверждения
    page.password_new.send_keys(new_pass)
    page.password_confirm.send_keys(new_pass)
    # нажатие на кнопку "Подтвердить сброс пароля"
    page.btn_confirm_reset.click()

    # проверяем работу авторизации по новому паролю, т.е. пароль успешно сменен
    # выбираем способ авторизации: по email
    page.btn_phone.click()
    page.btn_email.click()
    time.sleep(1)
    # входим в личный кабинет с email и новым паролем
    page.username.send_keys(name)
    page.password.send_keys(new_pass)
    # нажимаем кнопку "Войти"
    page.btn.click()
    time.sleep(1)
    # проверяем, что текущая страница - это страница профиля "Вход и безопасность"
    assert page.get_current_url()[:43] == 'https://b2c.passport.rt.ru/account_b2c/page'
    page.close()

def test_password_recovery_login(web_browser, name = 'rtkid_1234567890123',
                                 new_pass='$i$xybXg_#z4e?S'):
    """Тестирование восстановления пароля с использованием
        корректного логина"""
    page = AuthPage(web_browser)
    time.sleep(2)
    # нажимаем кнопку "Забыл пароль"
    page.btn_forgot_pass.click()
    # выбираем способ авторизации: по логину
    page.btn_login.click()
    # вводим логин
    page.username.send_keys(name)

    # ручной ввод капчи, за 10 секунд
    if page.img_captcha.is_visible():
        page.captcha.click()
        time.sleep(10) # время для ручного ввода captcha
    time.sleep(1)
    # нажимаем кнопку "Продолжить"
    page.btn_reset.click()
    time.sleep(2)

    # ручной ввод кода подтверждения
    # время для ручного ввода кода из СМС/email
    time.sleep(60)

    # ввод нового пароля и подтверждения
    page.password_new.send_keys(new_pass)
    page.password_confirm.send_keys(new_pass)
    # нажатие на кнопку "Подтвердить сброс пароля"
    page.btn_confirm_reset.click()

    # проверяем работу авторизации по новому паролю, т.е. пароль успешно сменен
    # выбираем способ авторизации: по логину
    page.btn_phone.click()
    page.btn_login.click()
    # входим в личный кабинет с логином и новым паролем
    page.username.clear()
    page.username.send_keys(name)
    page.password.send_keys(new_pass)
    # нажимаем кнопку "Войти"
    page.btn.click()
    time.sleep(1)
    # проверяем, что текущая страница - это страница профиля "Вход и безопасность"
    assert page.get_current_url()[:43] == 'https://b2c.passport.rt.ru/account_b2c/page'
    page.close()

@pytest.mark.xfail(reason="у меня нет номера ЛС, поэтому введены произвольные числа. "
                          "для успешного теста их необходимо заменить на корректный номер ЛС")
def test_password_recovery_ls(web_browser, name = '123456789012',
                                 new_pass='$i$xybXg_#z4e?S'):
    """Тестирование восстановления пароля с использованием
        корректного номера ЛС"""
    page = AuthPage(web_browser)
    time.sleep(2)
    # нажимаем кнопку "Забыл пароль"
    page.btn_forgot_pass.click()
    # выбираем способ авторизации: по номеру ЛС
    page.btn_ls.click()
    # вводим ЛС
    page.username.send_keys(name)

    # ручной ввод капчи, за 10 секунд
    if page.img_captcha.is_visible():
        page.captcha.click()
        time.sleep(10) # время для ручного ввода captcha
    time.sleep(1)
    # нажимаем кнопку "Продолжить"
    page.btn_reset.click()
    time.sleep(2)

    # ручной ввод кода подтверждения
    # время для ручного ввода кода из СМС/email
    time.sleep(60)

    # ввод нового пароля и подтверждения
    page.password_new.send_keys(new_pass)
    page.password_confirm.send_keys(new_pass)
    # нажатие на кнопку "Подтвердить сброс пароля"
    page.btn_confirm_reset.click()

    # проверяем работу авторизации по новому паролю, т.е. пароль успешно сменен
    # выбираем способ авторизации: по номеру ЛС
    page.btn_login.click()
    page.btn_ls.click()
    # входим в личный кабинет с номером ЛС и новым паролем
    page.username.clear()
    page.username.send_keys(name)
    page.password.send_keys(new_pass)
    # нажимаем кнопку "Войти"
    page.btn.click()
    time.sleep(1)
    # проверяем, что текущая страница - это страница профиля "Вход и безопасность"
    assert page.get_current_url()[:43] == 'https://b2c.passport.rt.ru/account_b2c/page'
    page.close()