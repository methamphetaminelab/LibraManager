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

    ctk.CTkButton(addReaderTab, text="Добавить читателя", command=lambda: readerAdd(name.get(), surname.get(), readerId.get(), error_label)).pack(pady=10)

    error_label = ctk.CTkLabel(addReaderTab, text='')
    error_label.pack(pady=10)

def deleteReaderMenu(deleteReaderTab):
    readerId = ctk.CTkEntry(deleteReaderTab, placeholder_text="Номер читательского билета")
    readerId.pack(pady=10)

    ctk.CTkButton(deleteReaderTab, text="Удалить читателя", command=lambda: readerDelete(readerId.get(), error_label)).pack(pady=10)

    error_label = ctk.CTkLabel(deleteReaderTab, text='')
    error_label.pack(pady=10)

def updateReaderMenu(updateReaderTab):
    id = ctk.CTkEntry(updateReaderTab, placeholder_text="ID читателя")
    id.pack(pady=10)
    name = ctk.CTkEntry(updateReaderTab, placeholder_text="Имя")
    name.pack(pady=10)
    surname = ctk.CTkEntry(updateReaderTab, placeholder_text="Фамилия")
    surname.pack(pady=10)
    readerId = ctk.CTkEntry(updateReaderTab, placeholder_text="Номер читательского билета")
    readerId.pack(pady=10)
    
    ctk.CTkButton(updateReaderTab, text="Изменить читателя", command=lambda: readerUpdate(id.get(), name.get(), surname.get(), readerId.get(), error_label)).pack(pady=10)

    error_label = ctk.CTkLabel(updateReaderTab, text='')
    error_label.pack(pady=10)

def searchReaderMenu(searchReaderTab):
    readerId = ctk.CTkEntry(searchReaderTab, placeholder_text="Номер читательского билета")
    readerId.pack(pady=10)

    ctk.CTkButton(searchReaderTab, text="Поиск читателя", command=lambda: readerSearch(readerId.get(), error_label)).pack(pady=10)

    error_label = ctk.CTkLabel(searchReaderTab, text='')
    error_label.pack(pady=10)