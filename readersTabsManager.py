import customtkinter as ctk
import sqlite3
from booksManager import *
from readersManager import *
from reportsManager import *
from databaseManager import *

def addReaderMenu(addReaderTab):
    name = ctk.CTkEntry(addReaderTab, placeholder_text="Имя")
    name.pack(pady=10)
    surname = ctk.CTkEntry(addReaderTab, placeholder_text="Фамилия")
    surname.pack(pady=10)
    readerId = ctk.CTkEntry(addReaderTab, placeholder_text="Номер читательского билета")
    readerId.pack(pady=10)

    ctk.CTkButton(addReaderTab, text="Добавить читателя", command=lambda: readerAdd(name.get(), surname.get(), readerId.get())).pack(pady=10)

def deleteReaderMenu(deleteReaderTab):
    id = ctk.CTkEntry(deleteReaderTab, placeholder_text="ID читателя")
    id.pack(pady=10)

    ctk.CTkButton(deleteReaderTab, text="Удалить читателя", command=lambda: readerDelete(id.get())).pack(pady=10)

def updateReaderMenu(updateReaderTab):
    id = ctk.CTkEntry(updateReaderTab, placeholder_text="ID читателя")
    id.pack(pady=10)
    name = ctk.CTkEntry(updateReaderTab, placeholder_text="Имя")
    name.pack(pady=10)
    surname = ctk.CTkEntry(updateReaderTab, placeholder_text="Фамилия")
    surname.pack(pady=10)
    readerId = ctk.CTkEntry(updateReaderTab, placeholder_text="Номер читательского билета")
    readerId.pack(pady=10)

    ctk.CTkButton(updateReaderTab, text="Изменить читателя", command=lambda: readerUpdate(id.get(), name.get(), surname.get(), readerId.get())).pack(pady=10)

def searchReaderMenu(searchReaderTab):
    name = ctk.CTkEntry(searchReaderTab, placeholder_text="Имя")
    name.pack(pady=10)
    surname = ctk.CTkEntry(searchReaderTab, placeholder_text="Фамилия")
    surname.pack(pady=10)
    readerId = ctk.CTkEntry(searchReaderTab, placeholder_text="Номер читательского билета")
    readerId.pack(pady=10)

    ctk.CTkButton(searchReaderTab, text="Поиск читателя", command=lambda: readerSearch(name.get(), surname.get(), readerId.get())).pack(pady=10)