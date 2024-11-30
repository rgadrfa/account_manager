import hashlib
import json
import uuid
import os
from datetime import datetime
import logging

#Main Класс User
class User:

    #Конструктор пользователя по его имени (user) и паролю (password)
    #при этом объекты user и password инскапсулированы
    def __init__(self, user, password,mail):
        self._user = user
        self._password = password
        self._mail = mail


    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    #Статический метод для просмотра данных файла data_person
    @staticmethod
    def open_user_file(mode='r'):

        #Объявление переменой с содержанием глобального пути
        global file_path
        file_path = './database/data_person.json'

        #Чтение данных файла
        try:
            with open(file_path, mode) as js_file:
                file = json.load(js_file)
            return file

        #При отсуствие файла он создаётся повторно
        except (FileNotFoundError, json.JSONDecodeError):

            #Стандартная конструкция файла
            default_data = {
                'user': {
                    "admin":{
                        "user_name": "admin",
                        "password": "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918",
                        "priority": "admin",
                        "mail": "none",
                        "date_reg": "none"
                    }
                }
            }

            with open(file_path, 'w') as js_file:
                json.dump(default_data, js_file, indent=4)
            return default_data

    #Функция проверки пользователя на существование, по его имени и паролю
    #В если имя и пароль совпадает, функция выдаст 1, если пароль неверный то 2,
    # если пользователя вообще нет то 0
    def user_search(self,param = 1):
        result = 0
        #получение данных из открытого файла с помощью цикла
        #Чёткая проверка по паролю и по имени
        if param == 1:
            for user_id, user_info in self.open_user_file()['user'].items():
                if user_info['user_name'] == self._user:
                    if user_info['password'] == self._password:
                        result = 1
                        break
                    result = 2
                    break
            return result
        #Проверка по имени
        else:
            for user_id, user_info in self.open_user_file()['user'].items():
                if user_info['user_name'] == self._user:
                    result = 1
                    break
            return result

    #Функция длы вывода информации о пользователе (пароль, приоритет, имя)
    def user_get(self):
        user_inf_list = []

        for user_id, user_info in self.open_user_file()['user'].items():
            if user_info['user_name'] == self._user:
                user_inf_list.extend([
                    user_id, user_info['user_name'], user_info['password'],
                    user_info['priority'],user_info['mail'],user_info['date_reg']
                ])
                break
        return user_inf_list

    #Функция для регистрации нового пользователя
    def user_add(self):

        dt = datetime.now()

        #Уникальный id
        new_user_id = str(uuid.uuid1())

        #регистрация информация по форме
        new_user = {
            'user_name': self._user,
            'password': self.hash_password(self._password),
            'priority': 'default',
            'mail': self._mail,
            'date_reg': dt.strftime('%Y-%m-%d_%H.%M.%S')
        }

        #Выгрузка данных из файла data_person
        file = self.open_user_file()

        #Обновление данных о пользователе в файле data_person
        file['user'][new_user_id] = new_user

        #Запись данных в файл data_person
        with open(file_path, 'w') as js_file:
            json.dump(file, js_file, indent=4)

    def user_name_rename(self):
        pass

    def user_password_rename(self):
        pass

    def user_priority_rename(self):
        pass

#Класс для работы с файловой системой пользователей
class UserFile(User):
    def __init__(self, user, password, mail=None, base_path='.'):
        super().__init__(user, password,mail)
        self.base_path = base_path
        self.user_dir = f'{base_path}/database/user/{self.user_get()[0]}/log session'

        # Создаем директорию для файлов пользователя, если она не существует
        if not os.path.exists(self.user_dir):
            os.makedirs(self.user_dir)

"""
Класс для регистрации логов пользователей
"""
class UserLogging(UserFile):
    def __init__(self, user, password, mail=None, base_path='.'):
        super().__init__(user, password, mail)

    #Регистрация файла пользователя с логами за всю сессию
    def user_create_log(self):
        dt = datetime.now()
        log_filename = f'{dt.strftime('%Y-%m-%d_%H.%M.%S')}.log'
        with open(os.path.join(self.user_dir, log_filename), 'w') as file:
            file.write(str(dt))

    #Генератор файла текущей сессии
    def user_create_session_1(self):
        dt = datetime.now()
        inf = []
        inf.extend([dt.strftime('%Y-%m-%d_%H.%M.%S'),self.user_get()[1],self.user_get()[3]])
        file_path = './current session.log'
        with open(file_path,'w+') as file:
            for index_user in inf:
                file.write(f'{index_user}\n')