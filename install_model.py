import os
from dotenv import load_dotenv
import subprocess

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем имя модели из переменных окружения
model_name = os.getenv('MODEL_NAME')

# Команда для установки модели
command = f"ollama pull {model_name}"

# Выполнение команды для установки модели
subprocess.run(command, shell=True, check=True)

print(f"Model '{model_name}' has been successfully installed.")
