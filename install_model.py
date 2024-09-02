import os
from dotenv import load_dotenv
import subprocess

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем имя модели и директорию для сохранения из переменных окружения
model_name = os.getenv('MODEL_NAME')
model_dir = os.getenv('MODEL_DIR')

# Убедимся, что директория для моделей существует, если нет, создаем её
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# Устанавливаем переменную среды для Ollama, чтобы использовать указанную директорию
os.environ['OLLAMA_MODEL_DIR'] = model_dir

# Команда для установки модели
command = f"ollama pull {model_name}"

# Выполнение команды для установки модели
subprocess.run(command, shell=True, check=True)

print(f"Model '{model_name}' has been successfully installed in '{model_dir}' directory.")
