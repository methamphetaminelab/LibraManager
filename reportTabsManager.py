import customtkinter as ctk
import sqlite3
from booksManager import *
from readersManager import *
from reportsManager import *
from databaseManager import *

def globalReportMenu(globalReportTab):
    ctk.CTkButton(globalReportTab, text="Общий отчет", command=lambda: globalReport(error_label, report_frame)).pack(pady=10)

    error_label = ctk.CTkLabel(globalReportTab, text='', fg_color='transparent')
    error_label.pack(pady=10)

    report_frame = ctk.CTkFrame(globalReportTab)
    report_frame.pack(pady=10, fill="both", expand=True)

def parameterReportMenu(parameterReportTab):
    genre = ctk.CTkEntry(parameterReportTab, placeholder_text="Жанр")
    genre.pack(pady=10)

    ctk.CTkButton(parameterReportTab, text="Отчет по жанрам", command=lambda: parameterReport(genre.get(), error_label, report_frame)).pack(pady=10)

    error_label = ctk.CTkLabel(parameterReportTab, text='', fg_color='transparent')
    error_label.pack(pady=10)

    report_frame = ctk.CTkFrame(parameterReportTab)
    report_frame.pack(pady=10, fill="both", expand=True)


def readerReportMenu(readerReportTab):
    readerId = ctk.CTkEntry(readerReportTab, placeholder_text="Номер читательского билета")
    readerId.pack(pady=10)

    ctk.CTkButton(readerReportTab, text="Отчет по читателю", command=lambda: readerReport(readerId.get(), error_label, report_frame)).pack(pady=10)

    error_label = ctk.CTkLabel(readerReportTab, text='', fg_color='transparent')
    error_label.pack(pady=10)

    report_frame = ctk.CTkFrame(readerReportTab)
    report_frame.pack(pady=10, fill="both", expand=True)

def issuedReportMenu(issuedReportTab):
    ctk.CTkButton(issuedReportTab, text="Отчет по просроченным возвратам", command=lambda: issuedReport(error_label, report_frame)).pack(pady=10)

    error_label = ctk.CTkLabel(issuedReportTab, text='', fg_color='transparent')
    error_label.pack(pady=10)

    report_frame = ctk.CTkFrame(issuedReportTab)
    report_frame.pack(pady=10, fill="both", expand=True)