import customtkinter as ctk
import sqlite3
from booksManager import *
from readersManager import *
from reportsManager import *
from databaseManager import *

def addBookMenu(addBookTab):
    title = ctk.CTkEntry(addBookTab, placeholder_text="Название")
    title.pack(pady=10)
    author = ctk.CTkEntry(addBookTab, placeholder_text="Автор")
    author.pack(pady=10)
    year = ctk.CTkEntry(addBookTab, placeholder_text="Год издания")
    year.pack(pady=10)
    genre = ctk.CTkEntry(addBookTab, placeholder_text="Жанр")
    genre.pack(pady=10)
    quantity = ctk.CTkEntry(addBookTab, placeholder_text="Количество экземпляров")
    quantity.pack(pady=10)
    
    ctk.CTkButton(addBookTab, text="Добавить книгу", command=lambda: bookAdd(title.get(), author.get(), year.get(), genre.get(), quantity.get(), error_label)).pack(pady=10)

    error_label = ctk.CTkLabel(addBookTab, text='')
    error_label.pack(pady=10)

def deleteBookMenu(deleteBookTab):
    id = ctk.CTkEntry(deleteBookTab, placeholder_text="ID книги")
    id.pack(pady=10)

    ctk.CTkButton(deleteBookTab, text="Удалить книгу", command=lambda: bookDelete(id.get(), error_label)).pack(pady=10)
    
    error_label = ctk.CTkLabel(deleteBookTab, text='')
    error_label.pack(pady=10)

def updateBookMenu(updateBookTab):
    id = ctk.CTkEntry(updateBookTab, placeholder_text="ID книги")
    id.pack(pady=10)
    title = ctk.CTkEntry(updateBookTab, placeholder_text="Название")
    title.pack(pady=10)
    author = ctk.CTkEntry(updateBookTab, placeholder_text="Автор")
    author.pack(pady=10)
    year = ctk.CTkEntry(updateBookTab, placeholder_text="Год издания")
    year.pack(pady=10)
    genre = ctk.CTkEntry(updateBookTab, placeholder_text="Жанр")
    genre.pack(pady=10)
    quantity = ctk.CTkEntry(updateBookTab, placeholder_text="Количество экземпляров")
    quantity.pack(pady=10)

    ctk.CTkButton(updateBookTab, text="Изменить книгу", command=lambda: bookUpdate(id.get(), title.get(), author.get(), year.get(), genre.get(), quantity.get(), error_label)).pack(pady=10)

    error_label = ctk.CTkLabel(updateBookTab, text='')
    error_label.pack(pady=10)

def searchBookMenu(searchBookTab):
    title = ctk.CTkEntry(searchBookTab, placeholder_text="Жанр")
    title.pack(pady=10)

    author = ctk.CTkEntry(searchBookTab, placeholder_text="Автор")
    author.pack(pady=10)

    genre = ctk.CTkEntry(searchBookTab, placeholder_text="Жанр")
    genre.pack(pady=10)

    ctk.CTkButton(searchBookTab, text="Поиск книги", command=lambda: bookSearch(title.get(), author.get(), genre.get(), error_label, report_frame)).pack(pady=10)

    error_label = ctk.CTkLabel(searchBookTab, text='')
    error_label.pack(pady=10)

    report_frame = ctk.CTkFrame(searchBookTab)
    report_frame.pack(pady=10, fill="both", expand=True)


def giveBookMenu(giveBookTab):
    readerId = ctk.CTkEntry(giveBookTab, placeholder_text="Номер читательского билета")
    readerId.pack(pady=10)
    bookId = ctk.CTkEntry(giveBookTab, placeholder_text="ID книги")
    bookId.pack(pady=10)
    returnDate = ctk.CTkEntry(giveBookTab, placeholder_text="Дата возврата")
    returnDate.pack(pady=10)
    
    ctk.CTkButton(giveBookTab, text="Выдать книгу", command=lambda: giveBook(readerId.get(), bookId.get(), returnDate.get(), error_label)).pack(pady=10)
    
    error_label = ctk.CTkLabel(giveBookTab, text='')
    error_label.pack(pady=10)

def returnBookMenu(returnBookTab):    
    readerId = ctk.CTkEntry(returnBookTab, placeholder_text="Номер читательского билета")
    readerId.pack(pady=10)
    bookdId = ctk.CTkEntry(returnBookTab, placeholder_text="ID книги")
    bookdId.pack(pady=10)
    
    ctk.CTkButton(returnBookTab, text="Вернуть книгу", command=lambda: returnBook(readerId.get(), bookdId.get(), error_label)).pack(pady=10)

    error_label = ctk.CTkLabel(returnBookTab, text='')
    error_label.pack(pady=10)