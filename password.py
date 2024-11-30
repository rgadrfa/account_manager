import time

from user_class import User, UserFile, UserLogging
import re

#Класс для работы с регистрацией паролей, имени, почты
class UserPasswordName:

    """
        Вход пользователя в систему
    """
    @staticmethod
    def login(username, password):

        user = User(username, password, None)

        if username != '' and password != '':
            if user.user_search() == 1:

                user_path = UserLogging(username, password,None)

                user_path.user_create_log()
                user_path.user_create_session_1()

            if user.user_search() == 2:
                return 1

            if user.user_search() == 0:
                return 2
        else:
            return 0

    """
        Регистрация пользователя
    """
    @staticmethod
    def registration(username, password, password_1, mail):

        user = User(username, password,mail)

        if user.user_search() == 0:
            if password != '' and username != '' and password_1 != '' and mail != '':
                if password == password:
                    #Цифр не больше 4, букв латиницы не менее 5, всего символов от 4 до 20
                    if not re.match(r'^(.*?\d.*?){0,4}(?!(.*\d){5})[a-zA-Z0-9_]{5,20}$', username):
                        return 3
                    #Цифр не больше 20, букв латиницы не менее 4, всего символов от 4 до 20
                    if not re.match(r'^(.*?\d.*?){0,20}(?!(.*\d){4})[a-zA-Z0-9*!]{4,15}$', password):
                        return 4

                    #Регистрация пользователя
                    user.user_add()

                    #Логирование пользователя
                    user_path = UserLogging(username, password,None)
                    time.sleep(2)
                    user_path.user_create_log()
                    user_path.user_create_session_1()

                else:
                    return 1
            else:
                return 2
        else:
            return 0