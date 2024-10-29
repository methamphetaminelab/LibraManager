## LibraManager

# Задание

Создать систему управления библиотекой, которая позволит автоматизировать процессы учета книг, читатетей и выдачи книг

# Структура БД

- library
  - books
    - id (Primary Key)
      - title
      - author
      - year
      - genre
      - quantity
  - readers
    - id (Primary Key)
      - name
      - surname
      - readerId

# Функции

-- КНИГИ --

1. Добавить книгу

   > Открывается форма для ввода информации о книге: название, автор, год издания, жанр, количество экземпляров.
   > После заполнения и сохранения информация добавляется в базу данных библиотеки.

2. Удалить книгу

   > Открывается список всех книг с возможностью поиска.
   > При выборе книги и подтверждении удаления книга удаляется из системы.

3. Изменить книгу (название, автор, год, жанры, количество)
   > Открывается список всех книг с функцией поиска.
   > При выборе книги доступна форма с редактированием информации (название, автор, год и пр.), после сохранения изменения применяются.

-- ЧИТАТЕЛИ --

1. Добавить читателя

   > Форма для ввода данных о читателе: имя, фамилия, номер читательского билета.
   > После сохранения данные добавляются в базу данных.

2. Удалить читателя

   > Открывается список читателей с возможностью поиска по номеру билета или имени.
   > При выборе читателя и подтверждении удаление, его запись удаляется из системы.

3. Изменить читателя (логин, пароль, имя, фамилия, номер читательского билета)
   > Открывается список читателей с функцией поиска.
   > При выборе доступна форма с редактированием данных, после сохранения изменения применяются.

-- ПРОЧЕЕ --

1. Выдать книгу

   > Открывается форма с полями: номер читательского билета, выбор книги и дата выдачи.
   > При сохранении в системе фиксируется, что книга выдана этому читателю.

2. Вернуть книгу

   > Открывается форма, где указывается номер читательского билета и книга, которую читатель возвращает.
   > После подтверждения книга возвращается в библиотеку.

3. Поиск книги (название, атвор, жанры)

   > Поиск книги по параметрам (название, автор или жанр).
   > Результаты отображаются в виде списка, можно выбрать книгу для детальной информации.

4. Поиск читателя (имя, номер читательского билета)
   > Поиск по номеру читательского билета или имени читателя.
   > Результат — данные о читателе с возможностью детального просмотра.

-- ОТЧЕТЫ --

1. Отчет по книгам определенного жанра

   > Фильтрация по жанру, чтобы показать количество книг выбранного жанра в библиотеке.

2. Общий отчет по книгам

   > Отображает общее количество книг всех жанров в библиотеке.

3. Отчет по читателю

   > Вводится номер читательского билета или имя читателя.
   > Выводится список всех книг, которые были выданы этому читателю.

4. Отчет о задолженностях
   > Показывает список читателей с просроченными возвратами книг, включая даты, когда книги должны были быть возвращены.

-- ДОП. ФУНКЦИИ --

1. Сохранить данные

   > Кнопка для сохранения всех данных (о книгах, читателях, выданных книгах и пр.) в файл.

2. Импортировать данные

   > Кнопка для загрузки данных из файла в систему, что позволяет восстановить данные.

3. Вход в систему
   > Форма для ввода логина и пароля, чтобы предотвратить несанкционированный доступ.

# Использование

...
