from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)

    # Элементы регистрации
    # кнопка начала регистрации "Зарегистрироваться"
    registration = WebElement(xpath='//a[@id="kc-register"]')
    # личные данные
    # имя
    reg_firstname = WebElement(xpath='//input[@name="firstName"]')
    # фамилия
    reg_lastname = WebElement(xpath='//input[@name="lastName"]')
    # регион
    # reg_region = WebElement(xpath='//input[contains(@class,"rt-input__input rt-select__input rt-input__input--rounded rt-input__input--orange")][@autocomplete="new-password"]')
    reg_region = WebElement(xpath='//input[@autocomplete="new-password"]')

    # данные для входа
    # email или номер мобильного телефона
    reg_address = WebElement(xpath='//input[@id="address"]')
    # пароль
    reg_password = WebElement(xpath='//input[@id="password"]')
    # подтверждение пароля
    reg_password_confirm = WebElement(xpath='//input[@id="password-confirm"]')

    # кнопка подтверждения регистрации "Зарегистрироваться"
    btn_submit_reg = WebElement(xpath='//button[@type="submit"]')
    # сообщения об ошибке ввода в одном из полей
    # error_messages = ManyWebElements(xpath='//span[contains(@class,"rt-input-container__meta--error")]')
    # error_messages = ManyWebElements(xpath='//div[contains(@class,"rt-input-container--error"")]')

    name_error = WebElement(xpath='//span[contains(text(),"Необходимо заполнить поле кириллицей")]')
    region_error = WebElement(xpath='//span[contains(text(),"Укажите регион")]')
    email_phone_error = WebElement(xpath='//span[contains(text(),"Введите телефон")]')
    # password_error = WebElement(xpath='//span[contains(text(),"долж")][contains(translate(.),"парол")]')
    password_error = WebElement(xpath='//span[contains(text(),"долж")]')
    password_confirm_error = WebElement(xpath='//span[contains(text(),"Пароли не совпадают")]')


    # Элементы страницы авторизации
    # кнопки выбора способа авторизации
    btn_phone = WebElement(id='t-btn-tab-phone')
    btn_email = WebElement(id='t-btn-tab-mail')
    btn_login = WebElement(id='t-btn-tab-login')
    btn_ls = WebElement(id='t-btn-tab-ls')
    # строка ввода почты/телефона/логина/лс
    username = WebElement(xpath='//input[@id="username"]')
    # строка ввода пароля
    password = WebElement(xpath='//input[@id="password"]')
    # кнопка "Войти"
    btn = WebElement(xpath='//button[@id="kc-login"]')
    # сообщение об ошибке при неудачной авторизации
    form_error = WebElement(xpath='//span[@id="form-error-message"]')

    # сообщение о неверном логине
    login_error = WebElement(xpath='//span[@id="username-meta"]')
    # login_error = WebElement(id="username-meta")

    # восстановление пароля
    # кнопка "Забыл зароль"
    btn_forgot_pass = WebElement(xpath='//a[@id="forgot_password"]')
    # изображение captcha
    img_captcha = WebElement(xpath='//img[@class="rt-captcha__image"]')
    # поле для ввода символов с картинки (captcha)
    captcha = WebElement(xpath='//input[@id="captcha"]')
    # кнопка "Продолжить"
    btn_reset = WebElement(xpath='//button[@id="reset"]')
    # поле ввода нового пароля
    password_new = WebElement(xpath='//input[@id="password-new"]')
    # поле ввода подтверждения нового пароля
    password_confirm = WebElement(xpath='//input[@id="password-confirm"]')
    # кнопка "Подтвердить сброс пароля"
    btn_confirm_reset = WebElement(xpath='//button[@id="t-btn-reset-pass"]')
