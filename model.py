import os

from dotenv import load_dotenv
import ollama

class BaseModelRunner:
    """
    Родительский класс для работы с моделью Ollama.
    
    Описывает базовую модель и методы для взаимодействия с ней, такие как генерация текста.
    """

    def __init__(self, model_name='llama3.1', model_dir=os.getcwd()):
        """
        Инициализация объекта BaseModelRunner.

        Устанавливает имя модели и директорию сохранения моделей.
        """
        # Устанавливаем переменные OLLAMA_MODELS в системные переменные среды
        self.model_name = model_name
        self.model_dir = model_dir

        os.environ['OLLAMA_MODELS'] = self.model_dir
        print(f"Model directory set to: {self.model_dir}")
        print(f"Model '{self.model_name}' is ready to use.")

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


class ChatModelRunner(BaseModelRunner):
    """
    Дочерний класс для ведения чата с моделью Ollama.
    
    Наследует функциональность из BaseModelRunner и добавляет чат с сохранением истории сообщений.
    """

    def __init__(self, model_name='llama3.1', model_dir=os.getcwd()):
        """
        Инициализация объекта ChatModelRunner.
        """
        super().__init__(model_name, model_dir)  # Инициализируем родительский класс
        self.chat_history = []  # Хранение истории чата

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

    def reset_chat(self):
        """
        Сбрасывает историю чата, чтобы начать новый разговор.
        """
        self.chat_history = []
        print("История чата сброшена.")


if __name__ == "__main__":
    load_dotenv()

    model_name = os.getenv('MODEL_NAME', 'llama3.1')
    model_dir = os.getenv('OLLAMA_MODELS', os.getcwd())
    
    base_runner = BaseModelRunner(model_name=model_name, model_dir=model_dir)
    prompt = "Напиши краткое описание модели llama 3.1."
    base_response = base_runner.generate(prompt)
    print(f"Base Model Response: {base_response}")