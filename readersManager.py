import sqlite3

def readerAdd(name, surname, readerId, error_label):
    try:
        if name == '' or surname == '' or readerId == '':
            error_label.configure(text='Заполните все поля', fg_color='red')
            return False
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO readers VALUES (NULL, ?, ?, ?)", (name, surname, readerId))
        if cursor.rowcount == 0:
            error_label.configure(text='Читатель не добавлен', fg_color='red')
            conn.close()
            return False
        conn.commit()
        conn.close()
        print('Читатель добавлен')
        error_label.configure(text='Читатель добавлен', fg_color='green')
        return True
    except Exception as e:
        print(f"Ошибка readerAdd: {e}")
        error_label.configure(text=f'Читатель не добавлен: {e}', fg_color='red')
        return False

def readerDelete(readerId, error_label):
    try:
        if readerId == '':
            error_label.configure(text='Заполните все поля', fg_color='red')
            return False
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM readers WHERE readerId = ?", (readerId,))
        if cursor.rowcount == 0:
            error_label.configure(text='Читатель не найден', fg_color='red')
            conn.close()
            return False
        conn.commit()
        conn.close()
        print('Читатель удален')
        error_label.configure(text='Читатель удален', fg_color='green')
        return True
    except Exception as e:
        print(f"Ошибка readerDelete: {e}")
        error_label.configure(text=f'Читатель не удален: {e}', fg_color='red')
        return False

def readerUpdate(id, name, surname, readerId, error_label):
    try:
        if id == '' or name == '' or surname == '' or readerId == '':
            error_label.configure(text='Заполните все поля', fg_color='red')
            return False
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE readers SET name = ?, surname = ?, readerId = ? WHERE id = ?", (name, surname, readerId, id))
        if cursor.rowcount == 0:
            error_label.configure(text='Читатель не найден', fg_color='red')
            conn.close()
            return False
        conn.commit()
        conn.close()
        print('Читатель обновлен')
        error_label.configure(text='Читатель обновлен', fg_color='green')
        return True
    except Exception as e:
        print(f"Ошибка readerUpdate: {e}")
        error_label.configure(text=f'Читатель не обновлен: {e}', fg_color='red')
        return False

def readerSearch(readerId, error_label):
    try:
        if readerId == '':
            error_label.configure(text='Заполните все поля', fg_color='red')
            return False
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM readers WHERE readerId = ?", (readerId,))
        rows = cursor.fetchall()
        if len(rows) == 0:
            error_label.configure(text='Читатель не найден', fg_color='red')
            conn.close()
            return False
        conn.close()
        print(f'Читатели найдены\n{rows}')
        error_label.configure(text=f'Читатели найдены\n{rows}', fg_color='green')
        return rows
    except Exception as e:
        print(f"Ошибка readerSearch: {e}")
        error_label.configure(text=f'Читатели не найдены: {e}', fg_color='red')
        return False