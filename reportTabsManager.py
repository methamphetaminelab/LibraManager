import customtkinter as ctk
import sqlite3
from booksManager import *
from readersManager import *
from reportsManager import *
from databaseManager import *

def makeGlobalReport(globalReportTab):
    for widget in globalReportTab.winfo_children():
        widget.destroy()

    ctk.CTkButton(globalReportTab, text="Общий отчет", command=lambda: makeGlobalReport(globalReportTab)).pack(pady=10)

    count, rows = globalReport()
    ctk.CTkLabel(globalReportTab, text=f"Количество книг в библиотеке: {count}").pack(pady=10)

    for row in rows:
        ctk.CTkLabel(globalReportTab, text=f"Книга ID: {row[0]}, Название: {row[1]}, Автор: {row[2]}, Год: {row[3]}, Жанр: {row[4]}, Количество: {row[5]}").pack(pady=5)

def globalReportMenu(globalReportTab):
    ctk.CTkButton(globalReportTab, text="Общий отчет", command=lambda: makeGlobalReport(globalReportTab)).pack(pady=10)

def makeParameterReport(parameterReportTab):
    for widget in parameterReportTab.winfo_children():
        widget.destroy()
    
    title = ctk.CTkEntry(parameterReportTab, placeholder_text="Название")
    title.pack(pady=10)
    author = ctk.CTkEntry(parameterReportTab, placeholder_text="Автор")
    author.pack(pady=10)
    year = ctk.CTkEntry(parameterReportTab, placeholder_text="Год издания")
    year.pack(pady=10)
    genre = ctk.CTkEntry(parameterReportTab, placeholder_text="Жанры")
    genre.pack(pady=10)
    quantity = ctk.CTkEntry(parameterReportTab, placeholder_text="Количество экземпляров")
    quantity.pack(pady=10)

    ctk.CTkButton(parameterReportTab, text="Отчет по параметрам", command=lambda: makeParameterReport(parameterReportTab)).pack(pady=10)

    count, rows = parameterReport(title.get(), author.get(), year.get(), genre.get(), quantity.get())
    ctk.CTkLabel(parameterReportTab, text=f"Количество книг в библиотеке: {count}").pack(pady=10)

    for row in rows:
        ctk.CTkLabel(parameterReportTab, text=f"Книга ID: {row[0]}, Название: {row[1]}, Автор: {row[2]}, Год: {row[3]}, Жанр: {row[4]}, Количество: {row[5]}").pack(pady=5)

def parameterReportMenu(parameterReportTab):
    title = ctk.CTkEntry(parameterReportTab, placeholder_text="Название")
    title.pack(pady=10)
    author = ctk.CTkEntry(parameterReportTab, placeholder_text="Автор")
    author.pack(pady=10)
    year = ctk.CTkEntry(parameterReportTab, placeholder_text="Год издания")
    year.pack(pady=10)
    genre = ctk.CTkEntry(parameterReportTab, placeholder_text="Жанры")
    genre.pack(pady=10)
    quantity = ctk.CTkEntry(parameterReportTab, placeholder_text="Количество экземпляров")
    quantity.pack(pady=10)

    ctk.CTkButton(parameterReportTab, text="Отчет по параметрам", command=lambda: makeParameterReport(parameterReportTab)).pack(pady=10)

def makeReaderReport(readerReportTab):
    for widget in readerReportTab.winfo_children():
        widget.destroy()

    readerId = ctk.CTkLabel(readerReportTab, text="Номер читательского билета")
    readerId.pack(pady=10)

    ctk.CTkButton(readerReportTab, text="Отчет по читателю", command=lambda: makeReaderReport(readerReportTab)).pack(pady=10)

    count, rows = readerReport(readerId.get())
    ctk.CTkLabel(readerReportTab, text=f"Количество выданных книг: {count}").pack(pady=10)

    for row in rows:
        ctk.CTkLabel(readerReportTab, text=f"Книга ID: {row[0]}, Название: {row[1]}, Автор: {row[2]}, Год: {row[3]}, Жанр: {row[4]}, Количество: {row[5]}").pack(pady=5)

def readerReportMenu(readerReportTab):
    readerId = ctk.CTkEntry(readerReportTab, placeholder_text="Номер читательского билета")
    readerId.pack(pady=10)

    ctk.CTkButton(readerReportTab, text="Отчет по читателю", command=lambda: makeReaderReport(readerReportTab)).pack(pady=10)

def makeIssuedReport(issuedReportTab):
    for widget in issuedReportTab.winfo_children():
        widget.destroy()

    ctk.CTkButton(issuedReportTab, text="Отчет по просроченным возвратам", command=lambda: makeIssuedReport(issuedReportTab)).pack(pady=10)

    rows = issuedReport()
    for row in rows:
        ctk.CTkLabel(issuedReportTab, text=f"Читатель: {row[0]} {row[1]}, ID: {row[2]}, дата возврата: {row[3]}").pack(pady=5)

def issuedReportMenu(issuedReportTab):
    ctk.CTkButton(issuedReportTab, text="Отчет по просроченным возвратам", command=lambda: makeIssuedReport(issuedReportTab)).pack(pady=10)