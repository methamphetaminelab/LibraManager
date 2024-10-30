import customtkinter as ctk
import sqlite3
from booksManager import *
from readersManager import *
from reportsManager import *
from databaseManager import *
from bookTabsManager import *
from main import *

def loginChecker(root, error_label, login, password):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admins WHERE login = ? AND password = ?", (login, password))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        mainMenu(root)
    else:
        error_label.configure(text="Неверный логин или пароль", fg="red")