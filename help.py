import logging

# Создаем основной логгер для всей программы
logger = logging.getLogger('main_logger')
logger.setLevel(logging.DEBUG)

# Создаем обработчик для записи логов в файл
file_handler = logging.FileHandler('log.log', mode='w')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# Добавляем обработчик к основному логгеру
logger.addHandler(file_handler)

# Создаем отдельные логгеры для системы, админа и пользователя
system_logger = logging.getLogger('SYSTEM')
admin_logger = logging.getLogger('ADMIN')
user_logger = logging.getLogger('USER')

# Настраиваем уровень каждого логгера
system_logger.setLevel(logging.WARNING)
admin_logger.setLevel(logging.INFO)
user_logger.setLevel(logging.DEBUG)

# Добавляем основной логгер к каждому из них
system_logger.addHandler(logger.handlers[0])
admin_logger.addHandler(logger.handlers[0])
user_logger.addHandler(logger.handlers[0])

def log_system(message):
    system_logger.warning(f'{message}')

def log_admin(message):
    admin_logger.info(f'{message}')

def log_user(message):
    user_logger.debug(f'{message}')