# LibraManager

## Задание

Создать систему управления библиотекой, которая позволит автоматизировать процессы учета книг, читатетей и выдачи книг

## Структура БД

- library.db > база данных
  - admins > администраторы
    - id > айди
    - login > логин
    - password > пароль
  - books > книги
    - id > айди
    - title > название
    - author > автор
    - year > год выпуска
    - genre > жанры
    - quantity > количество
  - readers > читатели
    - id > айди
    - name > имя
    - surname > фамилия
    - readerId > номер читательского билета
  - issuedBooks > взятые книги
    - id > айди
    - readerId > номер читательского билета
    - bookId > айди книги
    - dateToReturn > дата возврата

## Функции

### КНИГИ

1. Добавить книгу

   > Открывается форма для ввода информации о книге.
   > После заполнения и сохранения информация добавляется в базу данных.

2. Удалить книгу

   > Открывается форма для ввода bookId книги.
   > Книга удаляется из базы данных.

3. Изменить книгу (название, автор, год, жанры, количество)

   > Открывается форма для ввода информации о книге.
   > После заполнения и сохранения информация изменяется в базе данных.

4. Поиск книги (жанры)

   > Поиск книги по жанру.
   > Результаты отображаются в виде списка.

5. Выдать книгу

   > Открывается форма с полями, где нужно указать читателя, книгу и дату возврата.
   > При сохранении в системе фиксируется, что книга выдана этому читателю.

6. Вернуть книгу

   > Открывается форма, где указывается читатель и книга, которую читатель возвращает.
   > После подтверждения книга возвращается в библиотеку.

### ЧИТАТЕЛИ

1. Добавить читателя

   > Форма для ввода данных о читателе.
   > После сохранения данные добавляются в базу данных.

2. Удалить читателя

   > Открывается форма для ввода readerId читателя(номер читательского билета).
   > Читатель удаляется из базы данных.

3. Изменить читателя

   > Открывается форма для ввода данных о читателе.
   > При выборе доступна форма с редактированием данных, после сохранения изменения применяются.

4. Поиск читателя

   > Поиск по номеру читательского билета.
   > Результат — данные о читателе.

### ОТЧЕТЫ

1. Общий отчет по книгам

   > Отображает общее количество книг в библиотеке, а также сами книги.

2. Отчет по жанру

   > Вводится жанр.
   > Выводятся книги соответствующего жанра.

3. Отчет по читателю

   > Вводится readerId читателя.
   > Выводится список всех книг, которые были выданы этому читателю.

4. Отчет о задолженностях

   > Показывает список читателей с просроченными возвратами книг, включая даты, когда книги должны были быть возвращены.

### ДОП. ФУНКЦИИ

1. Сохранить данные

   > Кнопка экспорта данных.

2. Импортировать данные

   > Кнопка импорта данных.

3. Вход в систему (при запуске программы)

   > Форма для ввода логина и пароля, чтобы предотвратить несанкционированный доступ.

## Использование

Использовался [Python 3.13.0](https://www.python.org/)

1. `pip install -r requirements.txt`
2. `python main.py`
3. Вход в систему: (изначально admin/admin)
