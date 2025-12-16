import time
import pytest
from pages.auth_page import AuthPage

@pytest.mark.parametrize("Name", ["Г"*2,"Д"*30],
                         ids=["cyr 2 min","cyr 30 max"])
@pytest.mark.parametrize("Lastname", ["Г"*2,"Д"*30],
                         ids=["cyr 2 min","cyr 30 max"])
def test_registration_name(web_browser,Name,Lastname):
    """Тестирование ввода Имени и Фамилии при регистрации"""
    page = AuthPage(web_browser)
    time.sleep(2)

    # Нажимаем кнопку "Зарегистрироваться", чтобы перейти к регистрации
    page.registration.click()
    # Вводим Имя и Фамилию кириллицей от 2 до 30 символов.
    page.reg_firstname.send_keys(Name)
    page.reg_lastname.send_keys(Lastname)

    # Нажимаем кнопку "Зарегистрироваться"
    page.btn_submit_reg.click()

    time.sleep(1)
    # проверяем, что информация в полях Имя и Фамилия не вызывает ошибок
    assert page.name_error.is_visible() == False
    page.close()

@pytest.mark.xfail(reason="в атоматическом режиме выбор региона не удаётся. "
                          "при ручном тестировании регион успешно выбирается.")
def test_registration_region(web_browser):
    """Тестирование ввода Региона при регистрации"""
    page = AuthPage(web_browser)
    time.sleep(2)

    # Нажимаем кнопку "Зарегистрироваться", чтобы перейти к регистрации
    page.registration.click()
    # В поле "Регион" вводим название региона
    page.reg_region.send_keys("Самарская обл")
    # В выпадающем меню выбираем совпадающий с введенным текстом регион
    # и кникаем на него (здесь трудность: регион в выпадающем списке выделяется,
    # но "клик" не происходит и поле остаётся пустым)
    page.reg_region.click_down()

    # Нажимаем кнопку "Зарегистрироваться"
    page.btn_submit_reg.click()

    time.sleep(1)
    # проверяем, что информация в поле Регион не вызывает ошибок
    assert page.region_error.is_visible() == False
    page.close()

@pytest.mark.parametrize("phone", ["7"+"1"*10,"+7"+"2"*10,"375"+"4"*9, "+375"+"5"*9],
                         ids=["7 max", "+7 max","375 max", "+375 max"])
def test_registration_phone(web_browser,phone):
    """Тестирование ввода Телефона при регистрации"""
    page = AuthPage(web_browser)
    time.sleep(2)

    # Нажимаем кнопку "Зарегистрироваться", чтобы перейти к регистрации
    page.registration.click()
    # Вводим номер телефона в формате +7ХХХХХХХХХХ или +375XXXXXXXXX
    page.reg_address.send_keys(phone)

    # Нажимаем кнопку "Зарегистрироваться"
    page.btn_submit_reg.click()

    time.sleep(1)
    # проверяем, что информация в поле Телефон не вызывает ошибок
    assert page.email_phone_error.is_visible() == False
    page.close()

@pytest.mark.parametrize("email", ["q@q.ru"])
def test_registration_email(web_browser,email):
    """Тестирование ввода Email при регистрации"""
    page = AuthPage(web_browser)
    time.sleep(2)

    # Нажимаем кнопку "Зарегистрироваться", чтобы перейти к регистрации
    page.registration.click()
    # Вводим email в формате example@email.ru
    page.reg_address.send_keys(email)

    # Нажимаем кнопку "Зарегистрироваться"
    page.btn_submit_reg.click()

    time.sleep(1)
    # проверяем, что информация в поле Email не вызывает ошибок
    assert page.email_phone_error.is_visible() == False
    page.close()

@pytest.mark.parametrize("Pass", ["1Ab"*5], ids=["correct pass"])
def test_registration_password(web_browser,Pass):
    """Тестирование ввода Пароля при регистрации"""
    page = AuthPage(web_browser)
    time.sleep(2)

    # Нажимаем кнопку "Зарегистрироваться", чтобы перейти к регистрации
    page.registration.click()

    # Вводим корректный пароль
    # Длина пароля должна быть не менее 8 символов
    # Длина пароля должна быть не более 20 символов
    # Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру
    # Пароль должен содержать хотя бы одну заглавную букву
    # Пароль должен содержать хотя бы одну строчную букву
    page.reg_password.send_keys(Pass)

    # Поле "подтверждение пароля" оставляем пустым

    # Нажимаем кнопку "Зарегистрироваться"
    page.btn_submit_reg.click()

    time.sleep(1)
    # проверяем, что информация в поле Пароль не вызывает ошибок
    assert page.password_error.is_visible() == False
    page.close()

@pytest.mark.parametrize("Pass", ["1Ab"*5], ids=["correct pass"])
def test_registration_password_confirm(web_browser,Pass):
    """Тестирование ввода Подтверждения Пароля при регистрации"""
    page = AuthPage(web_browser)
    time.sleep(2)

    # Нажимаем кнопку "Зарегистрироваться", чтобы перейти к регистрации
    page.registration.click()
    # Вводим корректный пароль
    page.reg_password.send_keys(Pass)
    # Вводим подтверждение пароля
    page.reg_password_confirm.send_keys(Pass)

    # Нажимаем кнопку "Зарегистрироваться"
    page.btn_submit_reg.click()

    time.sleep(1)
    # проверяем, что информация в поле Подтверждение Пароля не вызывает ошибок
    assert page.password_confirm_error.is_visible() == False
    page.close()
