# Avito QA trainee assignment spring 2025


Здравствуйте, меня зовут *Карпов Егор*. Подробно расскажу о выплонении заданий для стажёров и предоставлю инструкцию по запуску автотестов. 

### Структура проекта:

    ├── README.md - Описание проекта и инструкция
    ├── Task_1 - Папка 1 задания
    │   ├── bug-report.md - Баг-репорт в Markdown
    │   ├── bug-report.xlsx - Баг-репорт в Excel
    │   └── image - Папка со скриншотами багов
    │
    └── task_2 - Папка 2 задания
        ├── TESTCASES_get_id.md - Тест-кейсы к API в Markdown
        ├── TESTCASES_get_sellerID.md - Тест-кейсы к API в Markdown
        ├── TESTCASES_get_statistic.md - Тест-кейсы к API в Markdown
        ├── TESTCASES_post.md - Тест-кейсы к API в Markdown
        ├── TESTCASES_get_statistic_v2.md - Тест-кейсы к API в Markdown
        ├── TESTCASES_get_delete.md - Тест-кейсы к API в Markdown
        ├── TESTCASES_get_id.xlsx - Тест-кейсы к API в Excel
        ├── TESTCASES_get_sellerID.xlsx - Тест-кейсы к API в Excel
        ├── TESTCASES_get_statistic.xlsx - Тест-кейсы к API в Excel
        ├── TESTCASES_post.xlsx - Тест-кейсы к API в Excel
        ├── TESTCASES_get_statistic_v2.xlsx - Тест-кейсы к API в Excel
        ├── TESTCASES_get_delete.xlsx - Тест-кейсы к API в Excel
        │
        ├── tests - Папка с автотестами API
        │   ├── main.py - Точка входа в программу
        │   ├── test_get_item.py - Автотесты к API
        │   ├── test_get_items_by_sellerID.py - Автотесты к API
        │   ├── test_get_statistic.py - Автотесты к API
        │   └── test_post.py - Автотесты к API
        │   └── test_get_statistic_v2.py - Автотесты к API
        │   └── test_delete.py - Автотесты к API
        └── Баг-репорт API.md - Баг-репорт к найденным багам

---

### Задание 1. Поиск багов на странице Авито

Для удобства подготовлено 2 файла с баг-репортом о найденных ошибках на предоставленной странице Авито:

[Markdown-документ](./Task_1/bug-report.md)

[Excel-таблица](./Task_1/bug-report.xlsx)

Содержание одинаковое.

---

### Задание 2. Тестирование микросервиса

Составлены тест-кейсы ко всем ручкам:

Версия 1:

[Тест-кейс для ручки "Создать объявления"](./Task_2/TESTCASES_post.md)

[Тест-кейс для ручки "Получить объявления по его идентификатору"](./Task_2/TESTCASES_get_id.md)

[Тест-кейс для ручки "Получить все объявления по идентификатору продавца"](./Task_2/TESTCASES_get_sellerID.md)

[Тест-кейс для ручки "Получить статистику по айтем id"](./Task_2/TESTCASES_get_statistic.md)

Версия 2:

[Тест-кейс для ручки "Получить статистику по айтем id версия 2"](./Task_2/TESTCASES_get_statistic_v2.md)

[Тест-кейс для ручки "Удалить объявление"](./Task_2/TESTCASES_delete.md)

Для удобства подготовлено 2 файла с баг-репортом о найденных багах при тестировании API:

[Markdown-документ](./Task_2/bug_report.md)

[Excel-таблица](./Task_2/bug_report.xlsx)

Содержание одинаковое.

*Инструкция по запуску автотестов*:

1. Склонируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале  
    ```  
    git clone https://github.com/Dwanlisid046/Avito-qa-trainee
    ```  

2. Убедитесь, что на вашем компьютере установлен Python. В командной строке/терминале выполните команду  
    ```  
    python -v  
    ```    
Если он не установлен, то установите с официального [сайта Python](https://www.python.org/downloads/), выбрав подходящую версию для вашей операционной системы, и пройдите шаг сначала. В процессе установки обязательно поставьте галочку в чекбоксе "Add python.exe to PATH". 

3. Через командную строку/терминал перейдите в корневую директорию проекта, выполнив команду  
   ```  
   cd /здесь укажите путь до директории с проектом  
   ```

4. Установите необходимые зависимости из файла `requirements.txt`, выполнив команду    
   ```  
   pip install -r requirements.txt  
   ```  
   если она не выполняется, то попробуйте  
   ```  
   pip3 install -r requirements.txt  
   ```  

5. Через командную строку/терминал перейдите в папку tests, выполнив команду   
   ```  
   cd task_2/tests 
   ```  
     
6. Наконец, запустите тесты, выполнив команду    
   ```  
   python main.py
   ```  
