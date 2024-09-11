import os
from dotenv import load_dotenv
import subprocess

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем имя модели и путь для сохранения моделей из переменных окружения
model_name = os.getenv('MODEL_NAME')
ollama_models_dir = os.getenv('OLLAMA_MODELS')

# Устанавливаем переменную OLLAMA_MODELS в системные переменные среды
os.environ['OLLAMA_MODELS'] = ollama_models_dir

# Команда для установки модели
command = f"ollama pull {model_name}"

# Выполнение команды для установки модели
subprocess.run(command, shell=True, check=True)

print(f"Model '{model_name}' has been successfully installed and saved to '{ollama_models_dir}'.")