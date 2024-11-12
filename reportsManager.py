import sqlite3
import customtkinter as ctk

def globalReport(error_label, report_frame):
    try:
        for widget in report_frame.winfo_children():
            widget.destroy()

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM books")
        count = cursor.fetchone()[0]
        
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        conn.close()

        print(f"Количество книг: {count}\n{rows}")
        error_label = error_label.configure(text=f"Количество книг: {count}", fg_color='transparent')

        for row in rows:
            ctk.CTkLabel(report_frame, text=f"Книга ID: {row[0]}, Название: {row[1]}, Автор: {row[2]}, Год: {row[3]}, Жанр: {row[4]}, Количество: {row[5]}").pack(pady=5)
    except Exception as e:
        print(f"Ошибка globalReport: {e}")
        error_label = error_label.configure(text=f"Ошибка globalReport: {e}", fg_color='red')
        return False
    
def parameterReport(genre, error_label, report_frame):
    try:
        for widget in report_frame.winfo_children():
            widget.destroy()

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM books WHERE genre LIKE ?", (f"%{genre}%",))
        count = cursor.fetchone()[0]

        cursor.execute("SELECT * FROM books WHERE genre LIKE ?", (f"%{genre}%",))
        rows = cursor.fetchall()
        conn.close()

        print(f"Количество книг по заданным параметрам: {count}\n{rows}")
        error_label = error_label.configure(text=f'Количество книг по жанрам: {count}', fg_color='transparent')
        for row in rows:
            ctk.CTkLabel(report_frame, text=f"Книга ID: {row[0]}, Название: {row[1]}, Автор: {row[2]}, Год: {row[3]}, Жанр: {row[4]}, Количество: {row[5]}").pack(pady=5)

    except Exception as e:
        print(f"Ошибка parameterReport: {e}")
        error_label = error_label.configure(text=f'Ошибка parameterReport: {e}', fg_color='red')
        return False

def readerReport(readerId, error_label, report_frame):
    try:
        for widget in report_frame.winfo_children():
            widget.destroy()

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM issuedBooks WHERE readerId = ?", (readerId,))
        count = cursor.fetchone()[0]

        cursor.execute("SELECT * FROM issuedBooks WHERE readerId = ?", (readerId,))
        rows = cursor.fetchall()
        conn.close()

        print(f"Количество выданных книг: {count}\n{rows}")
        error_label = error_label.configure(text=f'Найнено: {count}', fg_color='transparent')
        for row in rows:
            ctk.CTkLabel(report_frame, text=f"Номер билета: {row[1]}, Номер книги: {row[2]}, Дата возврата: {row[3]}").pack(pady=5)

    except Exception as e:
        print(f"Ошибка readerReport: {e}")
        error_label = error_label.configure(text=f"Ошибка readerReport: {e}", fg_color='red')
        return False
    
def issuedReport(error_label, report_frame):
    try:
        for widget in report_frame.winfo_children():
            widget.destroy()

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute("SELECT readers.name, readers.surname, readers.readerId, issuedBooks.dateToReturn FROM issuedBooks INNER JOIN readers ON issuedBooks.readerId = readers.id WHERE issuedBooks.dateToReturn < date('now')")
        rows = cursor.fetchall()
        conn.close()

        print("Читатели с просроченными возвратами книг:\n")
        error_label = error_label.configure(text='Читатели с просроченными возвратами книг:', fg_color='transparent')
        for row in rows:
            ctk.CTkLabel(report_frame, text=f"Номер билета: {row[1]}, Номер книги: {row[2]}, Дата возврата: {row[3]}").pack(pady=5)

    except Exception as e:
        print(f"Ошибка issuedReport: {e}")
        error_label = error_label.configure(text=f"Ошибка issuedReport: {e}", fg_color='red')
        return False
