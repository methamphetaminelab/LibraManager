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

def parameterReport(title=None, author=None, year=None, genre=None, quantity=None):
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

        cursor.execute(query, parameters)
        rows = cursor.fetchall()
        conn.close()

        print(f"Количество книг по заданным параметрам: {count}")
        return count, rows
    except Exception as e:
        print(f"Ошибка generateBooksReport: {e}")
        return False

def readerReport(readerId):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM issuedBooks WHERE readerId = ?", (readerId,))
        count = cursor.fetchone()[0]

        cursor.execute("SELECT * FROM issuedBooks WHERE readerId = ?", (readerId,))
        rows = cursor.fetchall()

        conn.close()

        print(f"Количество выданных книг: {count}\n{rows}")
        return count, rows
    except Exception as e:
        print(f"Ошибка readerReport: {e}")
        return False
    
def issuedReport():
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute("SELECT readers.name, readers.surname, readers.readerId, issuedBooks.dateToReturn FROM issuedBooks INNER JOIN readers ON issuedBooks.readerId = readers.id WHERE issuedBooks.dateToReturn < date('now')")
        rows = cursor.fetchall()
        conn.close()

        print("Читатели с просроченными возвратами книг:\n")
        for row in rows:
            print(f"{row[0]} {row[1]}, ID: {row[2]}, дата возврата: {row[3]}")
        return rows
    except Exception as e:
        print(f"Ошибка issuedReport: {e}")
        return False
