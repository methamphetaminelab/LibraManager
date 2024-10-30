import sqlite3

def readerAdd(name, surname, readerId):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO readers VALUES (NULL, ?, ?, ?)", (name, surname, readerId))
        conn.commit()
        conn.close()
        print('Читатель добавлен')
        return True
    except Exception as e:
        print(f"Ошибка readerAdd: {e}")
        return False

def readerDelete(id):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM readers WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        print('Читатель удален')
        return True
    except Exception as e:
        print(f"Ошибка readerDelete: {e}")
        return False

def readerUpdate(id, name, surname, readerId):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE readers SET name = ?, surname = ?, readerId = ? WHERE id = ?", (name, surname, readerId, id))
        conn.commit()
        conn.close()
        print('Читатель обновлен')
        return True
    except Exception as e:
        print(f"Ошибка readerUpdate: {e}")
        return False

def readerSearch(name=None, surname=None, readerId=None):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        query = "SELECT * FROM readers WHERE 1=1"
        parameters = []

        if name is not None:
            query += " AND name = ?"
            parameters.append(name)
        if surname is not None:
            query += " AND surname = ?"
            parameters.append(surname)
        if readerId is not None:
            query += " AND readerId = ?"
            parameters.append(readerId)

        cursor.execute(query, parameters)
        rows = cursor.fetchall()
        conn.close()
        print(f'Читатели найдены\n{rows}')
        return rows
    except Exception as e:
        print(f"Ошибка readerSearch: {e}")
        return False