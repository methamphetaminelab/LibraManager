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
