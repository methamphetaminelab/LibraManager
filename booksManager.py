import sqlite3
import customtkinter as ctk

def bookAdd(title, author, year, genre, quantity, error_label):
    try:
        if title == '' or author == '' or year == '' or genre == '' or quantity == '':
            error_label.configure(text='Заполните все поля', fg_color='red')
            return False

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books WHERE title = ? AND author = ?", (title, author))
        existing_book = cursor.fetchone()
        if existing_book:
            error_label.configure(text='Такая книга уже существует', fg_color='red')
            conn.close()
            return False

        cursor.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?, ?)", (title, author, year, genre, quantity))
        conn.commit()
        conn.close()
        print('Книга добавлена')
        error_label.configure(text='Книга добавлена', fg_color='green')
        return True
    except Exception as e:
        print('Ошибка bookAdd:', e)
        error_label.configure(text=f'Книга не добавлена: {e}', fg_color='red')
        return False

def bookDelete(id, error_label):
    try:
        if id == '':
            error_label.configure(text='Заполните все поля', fg_color='red')
            return False
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (id,))
        if cursor.rowcount == 0:
            error_label.configure(text='Книга не найдена', fg_color='red')
            conn.close()
            return False
        conn.commit()
        conn.close()
        print('Книга удалена')
        error_label.configure(text='Книга удалена', fg_color='green')
        return True
    except Exception as e:
        print('Ошибка bookDelete:', e)
        error_label.configure(text=f'Книга не удалена: {e}', fg_color='red')
        return False
    
def bookUpdate(id, title, author, year, genre, quantity, error_label):
    try:
        if id == '' or title == '' or author == '' or year == '' or genre == '' or quantity == '':
            error_label.configure(text='Заполните все поля', fg_color='red')
            return False
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET title = ?, author = ?, year = ?, genre = ?, quantity = ? WHERE id = ?", (title, author, year, genre, quantity, id))
        if cursor.rowcount == 0:
            error_label.configure(text='Книга не найдена', fg_color='red')
            conn.close()
            return False
        conn.commit()
        conn.close()
        print('Книга обновлена')
        error_label.configure(text='Книга обновлена', fg_color='green')
        return True
    except Exception as e:
        print('Ошибка bookUpdate:', e)
        error_label.configure(text=f'Книга не обновлена: {e}', fg_color='red')
        return False

def bookSearch(title, author, genre, error_label, report_frame):
    try:
        for widget in report_frame.winfo_children():
            widget.destroy()

        if title == '' and author == '' and genre == '':
            error_label.configure(text='Заполните хотя бы одно поле для поиска', fg_color='red')
            return False

        query = "SELECT * FROM books WHERE 1=1"
        params = []

        if title != '':
            query += " AND title LIKE ?"
            params.append(f'%{title}%')
        if author != '':
            query += " AND author LIKE ?"
            params.append(f'%{author}%')
        if genre != '':
            query += " AND genre LIKE ?"
            params.append(f'%{genre}%')

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute(query, tuple(params))
        rows = cursor.fetchall()
        conn.close()

        if len(rows) == 0:
            error_label.configure(text='Книги не найдены', fg_color='red')
            return False

        print(f'Книги найдены\n{rows}')
        for row in rows:
            ctk.CTkLabel(report_frame, text=f"Книга ID: {row[0]}, Название: {row[1]}, Автор: {row[2]}, Год: {row[3]}, Жанр: {row[4]}, Количество: {row[5]}").pack(pady=5)

        error_label.configure(text="", fg_color="transparent")
        return True

    except Exception as e:
        print(f"Ошибка bookSearch: {e}")
        error_label.configure(text=f'Книги не найдены: {e}', fg_color='red')
        return False
    
def giveBook(readerId, bookId, returnDate, error_label):
    try:
        if readerId == '' or bookId == '' or returnDate == '':
            error_label.configure(text='Заполните все поля', fg_color='red')
            return False

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT 1 FROM readers WHERE readerId = ?", (readerId,))
        if cursor.fetchone() is None:
            error_label.configure(text='Читатель не найден', fg_color='red')
            conn.close()
            return False

        cursor.execute("SELECT 1 FROM books WHERE id = ?", (bookId,))
        if cursor.fetchone() is None:
            error_label.configure(text='Книга не найдена', fg_color='red')
            conn.close()
            return False

        cursor.execute("INSERT INTO issuedBooks VALUES (NULL, ?, ?, ?)", (readerId, bookId, returnDate))
        conn.commit()
        conn.close()

        print('Книга выдана')
        error_label.configure(text='Книга выдана', fg_color='green')
        return True
    except Exception as e:
        print('Ошибка giveBook:', e)
        error_label.configure(text=f'Книга не выдана: {e}', fg_color='red')
        return False

def returnBook(readerId, bookId, error_label):
    try:
        if readerId == '' or bookId == '':
            error_label.configure(text='Заполните все поля', fg_color='red')
            return False

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute("SELECT 1 FROM issuedBooks WHERE readerId = ? AND bookId = ?", (readerId, bookId))
        if cursor.fetchone() is None:
            error_label.configure(text='Запись о выдаче книги не найдена', fg_color='red')
            conn.close()
            return False

        cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE id = ?", (bookId,))

        cursor.execute("DELETE FROM issuedBooks WHERE readerId = ? AND bookId = ?", (readerId, bookId))

        conn.commit()
        conn.close()

        print('Книга возвращена и количество увеличено')
        error_label.configure(text='Книга возвращена и количество увеличено', fg_color='green')
        return True
    except Exception as e:
        print('Ошибка returnBook:', e)
        error_label.configure(text=f'Книга не возвращена: {e}', fg_color='red')
        return False