import os
from databaseManager import *

# проверяю, есть ли база данных
if not checkDatabase():
    print('Базы данных не существует')
    createDatabase()
else:
    print('База данных существует')













        
