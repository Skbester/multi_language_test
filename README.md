# multi_language_test
Repository for task - module 3.6 step 9

This is answer on task - https://stepik.org/lesson/237240/step/9?unit=209628

Для предотвращения конфликтов окружений и файлов **confest.py**, скачайте файлы в отдельную директорию,
перейдите в неё из своего запущенного окружения(в котором работает ваш собственный тест для проверки) и
выполните проверку.

Run:

*pytest --language=es test_items.py*

Из описания задания - "Добавьте в файл с тестом команду time.sleep(30) сразу после открытия ссылки",
не забудьте сделать это самостоятельно при проверке.
Здесь в файле test_items.py достаточно раскомментировать (убрать из строки '# ') строку с time.sleep(30)
перед запуском второй проверки.

Run 2:

*pytest --language=fr test_items.py*

Браузеры:

--browser_name=chrome - Chrome используется по умолчанию

--browser_name=firefox - использовать для Firefox

