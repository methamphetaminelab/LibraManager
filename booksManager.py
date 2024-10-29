import sqlite3

def bookAdd(title, author, year, genre, quantity):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?, ?)", (title, author, year, genre, quantity))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print('Ошибка bookAdd:', e)
        return False

def bookDelete(id):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print('Ошибка bookDelete:', e)
        return False
    
def bookUpdate(id, title, author, year, genre, quantity):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET title = ?, author = ?, year = ?, genre = ?, quantity = ? WHERE id = ?", (title, author, year, genre, quantity, id))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print('Ошибка bookUpdate:', e)
        return False

def bookSearch(title=None, author=None, year=None, genre=None, quantity=None):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        query = "SELECT * FROM books WHERE 1=1"
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
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print(f"Ошибка bookSearch: {e}")
        return False