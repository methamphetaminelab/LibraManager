import sqlite3
import os

def checkDatabase():
    if os.path.exists('library.db'):
        return True
    else:
        createDatabase()

    return False

def createDatabase():
    try:
        print('Процесс создания базы данных начат..')
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        
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
            readerId TEXT NOT NULL UNIQUE
        )
        ''')

        conn.commit()
        conn.close()

        print('База данных успешно создана')
        return True
    except Exception as e:
        print(f'Ошибка createDatabase: {e}')
        return False
    
def exportDatabaseToTXT():
    try:
        print('Экспорт базы данных в txt')
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
        with open('books.txt', 'w', encoding='utf-8') as file:
            for book in books:
                file.write(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, Год: {book[3]}, Жанр: {book[4]}, Количество: {book[5]}\n")

        cursor.execute('SELECT * FROM readers')
        readers = cursor.fetchall()
        with open('readers.txt', 'w', encoding='utf-8') as file:
            for reader in readers:
                file.write(f"ID: {reader[0]}, Имя: {reader[1]}, Фамилия: {reader[2]}, ID читателя: {reader[3]}\n")

        conn.close()
        print('Экспорт базы данных в txt успешен')
        return True
    except Exception as e:
        print(f'Ошибка exportDatabaseToTXT: {e}')
        return False

def importDatabaseFromTXT():
    try:
        print('Импорт базы данных из txt')
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        with open('books.txt', 'r', encoding='utf-8') as file:
            for line in file:
                book = line.strip().split(', ')
                cursor.execute('INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)', book)

        with open('readers.txt', 'r', encoding='utf-8') as file:
            for line in file:
                reader = line.strip().split(', ')
                cursor.execute('INSERT INTO readers VALUES (?, ?, ?, ?)', reader)

        conn.commit()
        conn.close()
        print('Импорт базы данных из txt успешен')
        return True
    except Exception as e:
        print(f'Ошибка importDatabaseFromTXT: {e}')
        return False