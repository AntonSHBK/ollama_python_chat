import os
from dotenv import load_dotenv
import ollama

class ModelRunner:
    """
    Класс для работы с моделью Ollama.
    
    Поддерживает как генерацию текста, так и ведение чата с историей сообщений.
    """

    def __init__(self):
        """
        Инициализация объекта ModelRunner.

        Загружает переменные окружения из файла .env и устанавливает имя модели и директорию сохранения моделей.
        """
        # Загружаем переменные окружения из файла .env
        load_dotenv()

        # Получаем имя модели и путь для сохранения моделей из переменных окружения
        self.model_name = os.getenv('MODEL_NAME')
        self.model_dir = os.getenv('OLLAMA_MODELS')

        # Устанавливаем переменную OLLAMA_MODELS в системные переменные среды
        if self.model_dir:
            os.environ['OLLAMA_MODELS'] = self.model_dir
            print(f"Model directory set to: {self.model_dir}")

        self.chat_history = []  # Хранение истории чата
        print(f"Model '{self.model_name}' is ready to use.")

    def add_message(self, role: str, content: str):
        """
        Добавление сообщения в историю чата.

        Args:
            role (str): Роль участника ('user' или 'assistant').
            content (str): Текст сообщения.
        """
        self.chat_history.append({'role': role, 'content': content})

    def send_message(self, prompt: str) -> str:
        """
        Отправка сообщения модели Ollama в режиме чата и получение ответа.

        Args:
            prompt (str): Текст запроса, который будет передан модели.

        Returns:
            str: Ответ модели на запрос.
        """
        # Добавляем сообщение пользователя в историю чата
        self.add_message('user', prompt)

        # Отправляем запрос к модели Ollama с историей переписки
        response = ollama.chat(model=self.model_name, messages=self.chat_history)

        # Получаем ответ от модели и добавляем его в историю
        assistant_reply = response['message']['content']
        self.add_message('assistant', assistant_reply)

        return assistant_reply

    def generate(self, prompt: str) -> str:
        """
        Генерация текста на основе переданного запроса с использованием Ollama.

        Args:
            prompt (str): Текст запроса, на основе которого будет сгенерирован ответ.

        Returns:
            str: Сгенерированный моделью текст.
        """
        response = ollama.generate(model=self.model_name, prompt=prompt)
        return response['response']

# Пример использования класса ModelRunner
if __name__ == "__main__":
    runner = ModelRunner()

    while True:
        mode = input("Выберите режим (chat/generate/exit): ").lower()

        if mode == "exit":
            print("Программа завершена.")
            break

        prompt = input("Введите запрос: ")

        if mode == "chat":
            reply = runner.send_message(prompt)
            print(f"Модель (чат): {reply}")
        elif mode == "generate":
            generated_text = runner.generate(prompt)
            print(f"Модель (генерация): {generated_text}")
        else:
            print("Неверный режим. Попробуйте снова.")
