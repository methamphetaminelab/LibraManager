import customtkinter as ctk
import sqlite3
from booksManager import *
from readersManager import *
from reportsManager import *
from databaseManager import *
from bookTabsManager import *
from reportTabsManager import *
from readersTabsManager import *
from utils import loginChecker

def mainMenu(root):
    # Очистка окна
    for widget in root.winfo_children():
        widget.destroy()
    
    # Создание нового окна
    root.geometry("800x600")
    root.title("LibraManager")

    # Добавление вкладок
    tabview = ctk.CTkTabview(root)
    tabview.pack(expand=True, fill="both")

    booksTab = tabview.add("Книги")
    readersTab = tabview.add("Читатели")
    reportsTab = tabview.add("Отчеты")
    otherTab = tabview.add("Прочее")

    # Под-вкладки для книг
    booksTabview = ctk.CTkTabview(booksTab)
    booksTabview.pack(expand=True, fill="both")

    addBookTab = booksTabview.add("Добавить книгу")
    deleteBookTab = booksTabview.add("Удалить книгу")
    updateBookTab = booksTabview.add("Изменить книгу")
    searchBookTab = booksTabview.add("Поиск книги")
    giveBookTab = booksTabview.add("Выдать книгу")
    returnBookTab = booksTabview.add("Вернуть книгу")

    # Заполняем под-вкладки для книг
    addBookMenu(addBookTab)
    deleteBookMenu(deleteBookTab)
    updateBookMenu(updateBookTab)
    searchBookMenu(searchBookTab)
    giveBookMenu(giveBookTab)
    returnBookMenu(returnBookTab)

    # Под-вкладки для читателей
    readersTabview = ctk.CTkTabview(readersTab)
    readersTabview.pack(expand=True, fill="both")

    addReaderTab = readersTabview.add("Добавить читателя")
    deleteReaderTab = readersTabview.add("Удалить читателя")
    updateReaderTab = readersTabview.add("Обновить читателя")
    searchReaderTab = readersTabview.add("Поиск читателя")

    # Заполняем под-вкладки для читателей
    addReaderMenu(addReaderTab)
    deleteReaderMenu(deleteReaderTab)
    updateReaderMenu(updateReaderTab)
    searchReaderMenu(searchReaderTab)

    # Под-вкладки для отчетов
    reportsTabview = ctk.CTkTabview(reportsTab)
    reportsTabview.pack(expand=True, fill="both")

    globalReportTab = reportsTabview.add("Общий отчет")
    parameterReportTab = reportsTabview.add("Отчет по параметрам")
    readerReportTab = reportsTabview.add("Отчет по читателю")
    returnReportTab = reportsTabview.add("Отчет по задолжностям")

    # Заполняем под-вкладки для отчетов
    globalReportMenu(globalReportTab)
    parameterReportMenu(parameterReportTab)
    readerReportMenu(readerReportTab)
    issuedReportMenu(returnReportTab)

    # Прочее
    importDataButton = ctk.CTkButton(otherTab, text="Импорт данных", command=importDatabaseFromCSV)
    exportDataButton = ctk.CTkButton(otherTab, text="Экспорт данных", command=exportDatabaseToCSV)

    importDataButton.pack(pady=10)
    exportDataButton.pack(pady=10)

def main():
    # Проверка существования базы данных
    checkDatabase()

    # Создание окна с авторизацией
    root = ctk.CTk()
    root.geometry("300x200")
    root.title("LibraManager")

    # Авторизация
    login = ctk.CTkEntry(root, placeholder_text="Логин")
    password = ctk.CTkEntry(root, placeholder_text="Пароль", show="*")
    login.pack(pady=10)
    password.pack(pady=10)

    loginButton = ctk.CTkButton(root, text="Войти", command=lambda: loginChecker(root, error_label, login.get(), password.get()))
    loginButton.pack(pady=10)

    error_label = ctk.CTkLabel(root, text="")
    error_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
