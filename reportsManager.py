import sqlite3

def globalReport():
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM books")
        count = cursor.fetchone()[0]
        print(f"Количество книг в библиотеке: {count}")
        
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        
        for row in rows:
            print(f"Книга ID: {row[0]}, Название: {row[1]}, Автор: {row[2]}, Год: {row[3]}, Жанр: {row[4]}, Количество: {row[5]}")
        
        conn.close()
        return count, rows
    
    except Exception as e:
        print(f"Ошибка globalReport: {e}")
        return False

def generateBooksReport(title=None, author=None, year=None, genre=None, quantity=None):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        query = "SELECT COUNT(*) FROM books WHERE 1=1"
        parameters = []

        if title is not None:
            query += " AND title = ?"
            parameters.append(title)
        if author is not None:
            query += " AND author = ?"
            parameters.append(author)
        if year is not None:
            query += " AND year = ?"
            parameters.append(year)
        if genre is not None:
            query += " AND genre = ?"
            parameters.append(genre)
        if quantity is not None:
            query += " AND quantity = ?"
            parameters.append(quantity)

        cursor.execute(query, parameters)
        count = cursor.fetchone()[0]
        conn.close()

        print(f"Количество книг по заданным параметрам: {count}")
        return count
    except Exception as e:
        print(f"Ошибка generateBooksReport: {e}")
        return False

def readerReport(readerId=None, name=None, surname=None):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        query = '''
        SELECT books.id, books.title, books.author, books.year, books.genre, books.quantity 
        FROM books 
        INNER JOIN issuedBooks ON books.id = issuedBooks.bookId
        INNER JOIN readers ON issuedBooks.readerId = readers.id
        WHERE 1=1
        '''
        parameters = []

        if readerId is not None:
            query += " AND readers.readerId = ?"
            parameters.append(readerId)
        if name is not None:
            query += " AND readers.name = ?"
            parameters.append(name)
        if surname is not None:
            query += " AND readers.surname = ?"
            parameters.append(surname)

        cursor.execute(query, parameters)
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            print(f"Книга ID: {row[0]}, Название: {row[1]}, Автор: {row[2]}, Год: {row[3]}, Жанр: {row[4]}, Количество: {row[5]}")
        
        return rows
    except Exception as e:
        print(f"Ошибка readerReport: {e}")
        return False

def debtReport():
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        query = '''
        SELECT readers.readerId, readers.name, readers.surname, books.title, issuedBooks.dateToReturn 
        FROM readers 
        INNER JOIN issuedBooks ON readers.id = issuedBooks.readerId
        INNER JOIN books ON issuedBooks.bookId = books.id
        WHERE date(issuedBooks.dateToReturn) < date('now')
        '''
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            print(f"Читатель ID: {row[0]}, Имя: {row[1]}, Фамилия: {row[2]}, Книга: {row[3]}, Дата возврата: {row[4]}")
        
        return rows
    except Exception as e:
        print(f"Ошибка debtReport: {e}")
        return False