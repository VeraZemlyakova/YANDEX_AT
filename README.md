# Проект автоматизированного тестирования сайта Yandex
(на Python 3.9 с использованием PyTest и Selenium)

В данном репозитории содержится код для автоматизированного тестирования сайта Yandex.
Проект создан в рамках выполнения тестового задания на позицию разработчика 
в тестировании. 

В репозитории "YANDEX_AT" находятся папки:

- pages, содержащая файлы:
  - base_page.py - с описанием базового класса страницы;
  - main_page.py - с описанием класса главной страницы сайта;
  - locators.py - с описанием локаторов элементов страниц сайта;
- tests, содержащая файл с тестовыми сценариями test_main_page.py;
- driver, для размещения файла веб-драйвера браузера Mozilla Firefox;

а также файы:
  - QAP_тестовое_задание.docx - с тестовым заданием;
  - data.py - с данными для прохождения тестовых сценариев;
  - conftest.py - с фикстурами автотестов;
  - requirements.txt, где перечислены необходимые для выполнения автотестов библиотеки Python.


Для запуска тестов необходимо:

1) Скачать с https://github.com/mozilla/geckodriver/releases и распаковать 
в папку driver файл веб-драйвера для браузера Mozilla Firefox - geckodriver.exe

2) установить необходимые библиотеки Python:
  pip install -r requirements.txt

3) для выполнения автотестов запустить команду:
  python -m pytest -v
