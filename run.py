import os
from dotenv import load_dotenv
import ollama

class ModelRunner:
    """
    Класс для работы с моделью Ollama.

    Этот класс предоставляет методы для выполнения запросов к модели
    и генерации текста на основе переданного запроса.
    """

    def __init__(self):
        """
        Инициализация объекта ModelRunner.

        Загружает переменные окружения из файла .env и устанавливает имя модели.
        """
        # Загружаем переменные окружения из файла .env
        load_dotenv()

        # Получаем имя модели из переменной окружения
        self.model_name = os.getenv('MODEL_NAME')
        print(f"Model '{self.model_name}' is ready to use.")

    def query(self, prompt: str) -> str:
        """
        Выполнение запроса к модели Ollama в режиме чата.

        Args:
            prompt (str): Текст запроса, который будет передан модели.

        Returns:
            str: Ответ модели на запрос.
        """
        response = ollama.chat(model=self.model_name, messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
        return response['message']['content']

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

    # Пример использования метода query (чат)
    prompt = """
        Есть текст. Напиши адресс если он есть в тексте. Формате -  для поиска в поисковой системы Яндекс.
        А фотка то хорошая на улице ленина валдбериз как всегда. Шебекинский вайб просто супер.
    """
    # chat_response = runner.query(prompt)
    # print(f"Chat Response: {chat_response}")

    # Пример использования метода generate (генерация текста)
    generate_response = runner.generate(prompt)
    print(f"Generate Response: {generate_response}")
