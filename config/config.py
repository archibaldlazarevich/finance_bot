import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не найдены, т.к. отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_HOST = os.getenv('API_HOST')

DEFAULT_COMMANDS = (
    ('start', 'asdfasf')
)