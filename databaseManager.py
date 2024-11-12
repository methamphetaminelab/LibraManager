import sqlite3
import csv
import os
import pandas as pd

def checkDatabase():
    if os.path.exists('library.db'):
        return True
    else:
        createDatabase()

def createDatabase():
    try:
        print('Процесс создания базы данных начат..')
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        ''')

        cursor.execute("INSERT INTO admins VALUES (NULL, 'admin', 'admin')")

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            genre TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS readers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            readerId INTEGER NOT NULL UNIQUE
        )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS issuedBooks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                readerId INTEGER NOT NULL,
                bookId INTEGER NOT NULL,
                dateToReturn TEXT NOT NULL,
                FOREIGN KEY (readerId) REFERENCES readers(id),
                FOREIGN KEY (bookId) REFERENCES books(id)
            )
        ''')

        conn.commit()
        conn.close()

        print('База данных успешно создана')
        return True
    except Exception as e:
        print(f'Ошибка createDatabase: {e}')
        return False

def exportDatabaseToCSV(label):
    try:
        print('Экспорт базы данных в CSV...')
        conn = sqlite3.connect('library.db')

        admins = pd.read_sql_query("SELECT *, 'admins' as table_name FROM admins", conn)
        books = pd.read_sql_query("SELECT *, 'books' as table_name FROM books", conn)
        readers = pd.read_sql_query("SELECT *, 'readers' as table_name FROM readers", conn)
        issuedBooks = pd.read_sql_query("SELECT *, 'issuedBooks' as table_name FROM issuedBooks", conn)

        data = pd.concat([admins, books, readers, issuedBooks], ignore_index=True)

        data.to_csv('library.csv', index=False, encoding='utf-8')
        
        conn.close()
        print('Экспорт базы данных в CSV завершён')
        label.configure(text='Экспорт базы данных в CSV завершён', fg_color='green')
        return True
    except Exception as e:
        print(f'Ошибка exportDatabaseToCSV: {e}')
        label.configure(text=f'Ошибка exportDatabaseToCSV: {e}', fg_color='red')
        return False

def importDatabaseFromCSV(label):
    try:
        print('Импорт базы данных из CSV...')
        conn = sqlite3.connect('library.db')

        data = pd.read_csv('library.csv', encoding='utf-8')

        for table_name in data['table_name'].unique():
            table_data = data[data['table_name'] == table_name].drop(columns=['table_name'])

            if table_name == 'admins':
                table_data = table_data[['id', 'login', 'password']]
                table_data.to_sql('admins', conn, if_exists='replace', index=False)

            elif table_name == 'books':
                table_data = table_data[['id', 'title', 'author', 'year', 'genre', 'quantity']]
                table_data['year'] = table_data['year'].astype(int)
                table_data['quantity'] = table_data['quantity'].astype(int)
                table_data.to_sql('books', conn, if_exists='replace', index=False)

            elif table_name == 'readers':
                table_data = table_data[['id', 'name', 'surname', 'readerId']]
                table_data['readerId'] = table_data['readerId'].astype(int)
                table_data.to_sql('readers', conn, if_exists='replace', index=False)

            elif table_name == 'issuedBooks':
                table_data = table_data[['id', 'readerId', 'bookId', 'dateToReturn']]
                table_data['readerId'] = table_data['readerId'].astype(int)
                table_data['bookId'] = table_data['bookId'].astype(int)
                table_data.to_sql('issuedBooks', conn, if_exists='replace', index=False)

        conn.commit()
        conn.close()
        print('Импорт базы данных из CSV завершён')
        label.configure(text='Импорт базы данных из CSV завершён', fg_color='green')
        return True
    except Exception as e:
        print(f'Ошибка importDatabaseFromCSV: {e}')
        label.configure(text='Ошибка importDatabaseFromCSV: {e}', fg_color='red')
        return False
