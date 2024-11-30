import tkinter
import time
import os

from tkinter import ttk, messagebox
from user_class import User
from password import UserPasswordName


class WindowPassword(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.font_size = 10
        self.set_font()

        self.geometry('490x220')
        self.title('Пароль')
        self.resizable(False, False)

        #Ввод
        self.entry_name = tkinter.Entry(self, font=self.font_label)
        self.entry_name.place(x=147, y=60, width=200, height=30)

        self.entry_password = tkinter.Entry(self, show='*', font=self.font_label)
        self.entry_password.place(x=147, y=100, width=200, height=30)

        #Текст
        self.label_1 = tkinter.Label(text='Введите данные', font=('JetBrains Mono', 12))
        self.label_1.place(x=80, y=10, width=280, height=30)

        self.label_name = tkinter.Label(text='Пароль:', font=self.font_label)
        self.label_name.place(x=70, y=100, width=60, height=30)

        self.label_password = tkinter.Label(text='Логин:', font=self.font_label)
        self.label_password.place(x=70, y=60, width=60, height=30)

        self.label_inf = tkinter.Label(font = self.font_label)
        self.label_inf.place(x=27, y=150, width=390, height=60)

        #Кнопки
        self.button = tkinter.Button(text = 'Вход', font = self.font_label,command = self.button_sing)
        self.button.place(x=355, y=60, width=130, height=30)

        self.button_1 = tkinter.Button(text = 'Регистрация', font = self.font_label,command = self.open_registration_window)
        self.button_1.place(x=355, y=90, width=130, height=30)

        self.button = tkinter.Button(text='Восстановление', font=self.font_label)
        self.button.place(x=355, y=120, width=130, height=30)

        self.button = tkinter.Button(text='Смена пароля', font=self.font_label)
        self.button.place(x=355, y=150, width=130, height=30)

    def set_font(self):
        self.font_label = ('JetBrains Mono', self.font_size)

    #Функция кнопки входа
    def button_sing(self):

        username = self.entry_name.get()
        password = self.entry_password.get()

        result = UserPasswordName.login(username,User.hash_password(password))
        match result:
            case 1:
                self.label_inf['text'] = 'Неверный пароль'
            case 2:
                self.label_inf['text'] = 'Такого пользователя нет, зарегистрируйтесь'
            case 0:
                self.label_inf['text'] = 'Данные не введены'
            case _:
                time.sleep(1)
                self.open_main_window()

    def open_registration_window(self):
        self.destroy()
        registration_window = WindowRegistration()
        registration_window.mainloop()

    def open_main_window(self):
        self.destroy()
        main_window = WindowMain()
        main_window.mainloop()


class WindowRegistration(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.font_size = 10
        self.set_font()

        self.geometry('490x260')
        self.title('Пароль')
        self.resizable(False, False)

        #Ввод
        self.entry_name = tkinter.Entry(self, font=self.font_label)
        self.entry_name.place(x=147, y=60, width=200, height=30)

        self.entry_password = tkinter.Entry(self, font=self.font_label)
        self.entry_password.place(x=147, y=100, width=200, height=30)

        self.entry_password_1 = tkinter.Entry(self, font=self.font_label)
        self.entry_password_1.place(x=147, y=140, width=200, height=30)

        self.entry_email = tkinter.Entry(self, font=self.font_label)
        self.entry_email.place(x=147, y=180, width=200, height=30)

        #Текст
        self.label_1 = tkinter.Label(text = 'Введите данные', font = ('JetBrains Mono', 12))
        self.label_1.place(x=80, y=10, width=280, height=30)

        self.label_password_1 = tkinter.Label(text='Повторите пароль:', font=self.font_label)
        self.label_password_1.place(x=5, y=140, width=140, height=30)

        self.label_name = tkinter.Label(text = 'Пароль:', font = self.font_label)
        self.label_name.place(x=70, y=100, width=60, height=30)

        self.label_password = tkinter.Label(text = 'Логин:', font = self.font_label)
        self.label_password.place(x=70, y=60, width=60, height=30)

        self.label_mail = tkinter.Label(text='Почта:', font=self.font_label)
        self.label_mail.place(x=70, y=180, width=60, height=30)

        self.label_inf = tkinter.Label(font = self.font_label)
        self.label_inf.place(x=27, y=220, width=390, height=30)

        #Кнопки
        self.button = tkinter.Button(text = 'Регистрация', font = self.font_label, command = self.button_sing)
        self.button.place(x=355, y=60, width=130, height=30)

    def set_font(self):
        self.font_label = ('JetBrains Mono', self.font_size)

    #Функция кнопки регистрации
    def button_sing(self):

        username = self.entry_name.get()
        password = self.entry_password.get()
        mail = self.entry_email.get()
        password_1 = self.entry_password_1.get()

        result = UserPasswordName.registration(username,password,password_1,mail)
        match result:
            case 0:
                self.label_inf['text'] = 'Такой пользователь уже есть'
            case 1:
                self.label_inf['text'] = 'Пароли не совпадают'
            case 2:
                self.label_inf['text'] = 'Данные не введены'
            case 3:
                self.label_inf['text'] = ('Имя должно содержать только латинские буквы \n'
                                          'Цифр не больше 4, букв латиницы не менее 5, всего символов от 4 до 20')
            case 4:
                self.label_inf['text'] = ('Пароль должен содержать только латинские буквы и цифры,\n'
                               'Цифр не больше 20, букв латиницы не менее 4, всего символов от 4 до 20')
            case _:
                time.sleep(1)
                self.open_main_window()


    def open_main_window(self):
        self.destroy()
        main_window = WindowMain()
        main_window.mainloop()


class WindowMain(tkinter.Tk):
    def __init__(self):
        super().__init__()

        # Инициализация переменных
        self.font_size = 10
        self.set_font()

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        # Чтение информации из файла
        try:
            with open('current session.log', 'r') as file:
                self.information = file.read().splitlines()
        except FileNotFoundError:
            self.other_window_open()
            return

        # Настройка окна
        self.geometry('1015x600')
        self.title('Окно пользователя')
        self.resizable(False, False)

        # Создание интерфейса
        self.priority_user_interface()

    def on_closing(self):
        """Обработчик события закрытия окна."""
        os.remove('current session.log')
        time.sleep(1)
        self.destroy()

    def priority_user_interface(self):
        """Создание главного меню в зависимости от приоритета пользователя"""
        priority = self.information[2]

        match priority:
            case 'admin':
                self.AdminGIU()
            case 'default':
                self.DefaultGUI()

    def set_font(self):
        """Установка шрифта для элементов интерфейса"""
        self.font_label = ('JetBrains Mono', self.font_size)

    def AdminGIU(self):
        self.create_main_menu_admin()

    def DefaultGUI(self):
        self.create_main_menu_default()

    def ModerGUI(self):
        pass

    def create_main_menu_default(self):
        """Создание главного меню приложения"""
        file_menu_default = tkinter.Menu(self, tearoff=False, font=self.font_label)
        self.add_menu_commands_default(file_menu_default)

        main_menu = tkinter.Menu(self, font=self.font_label)
        main_menu.add_cascade(label="Главное", menu=file_menu_default)
        main_menu.add_cascade(label="Заполнитель")
        main_menu.add_cascade(label="Заполнитель")
        self.config(menu=main_menu)

    def add_menu_commands_default(self, file_menu):
        """Добавление команд в главное меню"""
        file_menu.add_command(
            label="Панель управления файлами",
            font=self.font_label
        )
        file_menu.add_command(
            label="Информация о текущей сессии",
            font=self.font_label,
            command=self.open_info
        )
        file_menu.add_separator()
        file_menu.add_command(
            label="Выход",
            font=self.font_label,
            command=self.exit_user
        )



    def create_main_menu_admin(self):
        """Создание главного меню приложения"""
        file_menu_admin = tkinter.Menu(self, tearoff=False, font=self.font_label)
        self.add_menu_commands_admin(file_menu_admin)

        main_menu = tkinter.Menu(self, font=self.font_label)
        main_menu.add_cascade(label="Главное", menu=file_menu_admin)
        main_menu.add_cascade(label="Заполнитель")
        main_menu.add_cascade(label="Заполнитель")
        self.config(menu=main_menu)

    def add_menu_commands_admin(self, file_menu):
        """Добавление команд в главное меню"""
        file_menu.add_command(
            label="Панель управления пользователями",
            font=self.font_label,
            command=self.create_tree_view
        )
        file_menu.add_command(
            label="Панель управления файлами",
            font=self.font_label
        )
        file_menu.add_command(
            label="Информация о текущей сессии",
            font=self.font_label,
            command=self.open_info
        )
        file_menu.add_separator()
        file_menu.add_command(
            label="Выход",
            font=self.font_label,
            command=self.exit_user
        )

    def create_tree_view(self):
        """Создание дерева пользователей"""
        people = self.get_user_table()

        columns = (
            "user",
            "password",
            "priority",
            "mail",
            "date_reg",
            'ID'
        )

        style = ttk.Style(self)
        style.configure('Treeview', font=self.font_label)
        style.map('Treeview', foreground=[])

        self.tree = ttk.Treeview(self, columns=columns, show="headings", style='Treeview')
        self.tree.place(x=7, y=50, width=1000, height=540)

        self.tree.heading("user", text="Пользователь", anchor=tkinter.W)
        self.tree.heading("password", text="Пароль", anchor=tkinter.W)
        self.tree.heading("priority", text="Приоритет", anchor=tkinter.W)
        self.tree.heading("mail", text="Почта пользователя", anchor=tkinter.W)
        self.tree.heading("date_reg", text="Дата регистрации", anchor=tkinter.W)
        self.tree.heading("ID", text="ID пользователя", anchor=tkinter.W)

        self.tree.column("#1", width=60)
        self.tree.column("#2", width=90)
        self.tree.column("#3", width=80)
        self.tree.column("#4", width=80)
        self.tree.column("#5", width=120)
        self.tree.column("#6", width=245)

        self.button_redaction = tkinter.Button(
            text='Редактировать',
            font=self.font_label,
            state='disabled',
            command=self.other_window_open_1
        )
        self.button_redaction.place(x=7, y=7)

        self.button_log_search = tkinter.Button(
            text='Просмотр логов',
            font=self.font_label,
            state='disabled'
        )
        self.button_log_search.place(x=127, y=7)

        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)

        for person in people:
            self.tree.insert('', tkinter.END, values=person)

    @staticmethod
    def get_user_table():
        """Получение списка пользователей из файла"""
        users_data = []
        for user_id, user_info in User.open_user_file()['user'].items():
            users_data.append([
                user_info['user_name'],
                user_info['password'],
                user_info['priority'],
                user_info['mail'],
                user_info['date_reg'],
                user_id
            ])

        return users_data

    def on_tree_select(self, event=None):
        """Обработка выбора строки в дереве пользователей"""
        global selected_people
        if event is not None:
            selected_items = event.widget.selection()
        else:
            selected_items = self.tree.selection()

        if selected_items:
            selected_item = selected_items[0]
            item = self.tree.item(selected_item)
            selected_people = item['values']

            self.button_redaction.config(state='normal')
        else:
            self.button_redaction.config(state='disabled')

        return selected_people

    def other_window_open_1(self):
        """Открытие окна редактирования пользователя"""
        selected_people = self.on_tree_select(None)
        window_editing = WindowEditing(self, selected_people)

    def other_window_open_edit(self):
        """Переход к окну редактирования"""
        selected_people = self.on_tree_select(None)
        window_editing = WindowEditing(self, selected_people)
        window_editing.grab_set()

    def exit_user(self):
        """Завершение сеанса пользователя"""
        os.remove('current session.log')
        self.other_window_open()

    def open_info(self):
        """Показ информации о текущем пользователе"""
        messagebox.showinfo(
            title="Информация",
            message=f"Пользователь: {self.information[1]}\n"
                    f"Дата сессии: {self.information[0]}\n"
                    f"Приоритет: {self.information[2]}"
        )

    def other_window_open(self):
        """Переход к окну авторизации"""
        self.destroy()
        time.sleep(1)
        window_registration = WindowPassword()
        window_registration.mainloop()




class WindowEditing(tkinter.Toplevel):
    def __init__(self, parent, selected_person):
        super().__init__(parent)

        self.font_size = 10  # Устанавливаем стандартный размер шрифта
        self.set_font()

        self.geometry('370x220')
        self.title('Окно редактирования')
        self.resizable(False, False)

        self.entry_name = tkinter.Entry(self, font=self.font_label)
        self.entry_name.place(x=147, y=20, width=200, height=30)
        self.entry_name.insert(0, selected_person[0])

        self.entry_password = tkinter.Entry(self, font=self.font_label)
        self.entry_password.place(x=147, y=60, width=200, height=30)
        self.entry_password.insert(0, selected_person[1])

        self.entry_email = tkinter.Entry(self, font=self.font_label)
        self.entry_email.place(x=147, y=100, width=200, height=30)
        self.entry_email.insert(0, selected_person[3])

        priority = ['default', 'admin', 'moder']
        combobox_priority = ttk.Combobox(self, values=priority, font=self.font_label)
        combobox_priority.place(x=155, y=140)

        # Установка приоритета
        default_priority = selected_person[2]
        combobox_priority.current(priority.index(default_priority))

        self.button_redaction = tkinter.Button(self,text='Применить', font=self.font_label)
        self.button_redaction.place(x=240, y=170)

        self.button_close = tkinter.Button(self,text='Отменить', font=self.font_label,
                                               command=self.close_window)
        self.button_close.place(x=160,y=170)

    def set_font(self):
        self.font_label = ('JetBrains Mono', self.font_size)

    def close_window(self):
        self.destroy()



if __name__ == '__main__':
    window_main = WindowMain()
    window_main.mainloop()
