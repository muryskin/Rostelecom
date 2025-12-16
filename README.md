Стажировка по тестированию с компанией Ростелеком

https://b2c.passport.rt.ru/

Основная цель тестирования — проверить работоспособность функций страницы авторизации.

Функциональное тестирование:

- проверка функциональных элементов на странице,
- тестирование регистрации пользователей,
- тестирование авторизации пользователей,
- тестирование восстановления пароля.
Проведено ручное тестирование для проверки функциональности сайта и пользовательского интерфейса.
Разработаны автоматизированные тесты для критических бизнес-процессов (регистрация, авторизация, восстановление пароля).

Тест-кейсы и найденные баги:

https://docs.google.com/spreadsheets/d/1DBVY8lY5byCSo6Yp9XBt_UQ7H-WkeYKyWY6fuhtXMY0/edit?usp=sharing

Файлы автоматического тестирования:

/tests/test_auth.py - тестирование авторизации пользователей по телефону, email, логину, лицевому счету

/tests/test_negative_auth.py - негативное тестирование авторизации пользователей по телефону, email, логину, лицевому счету

/tests/test_negative_registration.py - негативное тестирование регистрации пользователей

/tests/test_pass_recovery.py - тестирование восстановления пароля по телефону, email, логину, лицевому счету

/tests/test_registration.py - тестирование регистрации пользователей


Отчеты по проведенным авто-тестам

Все тесты успешно выполняются в соответствии с заданными ожиданиями:

report_auth.html - отчеты по тестированию test_auth.py

report_negative_auth.html - отчеты по тестированию test_negative_auth.py

report_negative_registration_1.html, report_negative_registration_2.html, report_negative_registration_3.html - отчеты по тестированию test_negative_registration.py

report_pass_recovery_email.html, report_pass_recovery_login.html, report_pass_recovery_ls.html, report_pass_recovery_phone.html - отчеты по тестированию test_pass_recovery.py

report_registration.html - отчеты по тестированию test_registration.py


Использованное рабочее окружение:

Python: 3.13.7

Platform: macOS-12.7.6-x86_64-i386-64bit-Mach-O

Packages: pytest: 7.4.4, pluggy: 1.6.0

Plugins: variables: 3.1.0, html: 4.1.1, metadata: 3.1.1, base-url: 2.1.0, selenium: 4.1.0
