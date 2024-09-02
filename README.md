# Ollama Python Chat

Этот проект демонстрирует использование модели `Llama` от Ollama в Python. Включает инструменты для запуска модели, выполнения запросов и генерации текста.

## Описание проекта

Проект включает в себя класс `ModelRunner`, который предоставляет два основных метода для работы с моделью Llama:
- `query`: Выполняет запрос к модели в режиме чата.
- `generate`: Генерирует текст на основе переданного запроса.

Модель `Llama` — это мощная языковая модель, разработанная для обработки естественного языка. Она может использоваться для создания чат-ботов, генерации текста, перевода и других задач, связанных с обработкой текста.

### Основные функции:
- Запуск модели Llama.
- Выполнение запросов в режиме чата.
- Генерация текста на основе заданных промптов.

## Установка

1. Клонируйте репозиторий на локальный компьютер:
   ```bash
   git clone https://github.com/your-username/ollama_python_chat.git
   cd ollama_python_chat
   ```

2. Создайте виртуальное окружение и активируйте его:
   ```bash
   python -m venv .venv
   # Для Windows
   .\.venv\Scripts\activate
   # Для Linux/MacOS
   source .venv/bin/activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Убедитесь, что у вас установлен `ollama` и модель Llama, которую вы хотите использовать. Если модель еще не установлена, запустите:
   ```bash
   python install_model.py
   ```

## Настройка

Перед запуском проекта создайте файл `.env` в корне проекта и укажите имя модели и директорию для хранения моделей:

```env
MODEL_NAME=llama3.1
MODEL_DIR=models
```

## Запуск и тестирование

Для запуска проекта и тестирования функционала используйте скрипт `run.py`:

```bash
python run.py
```

### Пример использования

Скрипт `run.py` демонстрирует два основных метода:
1. **`query`**: Выполняет запрос к модели в режиме чата.
2. **`generate`**: Генерирует текст на основе переданного запроса.

В результате выполнения скрипта вы получите ответы модели на оба запроса, которые будут выведены на экран.

## О модели Llama

Llama — это языковая модель, разработанная для выполнения различных задач обработки естественного языка. Она может использоваться для создания диалоговых систем, генерации текстов, перевода и других задач, связанных с текстом. Модель отличается высокой точностью и способностью понимать контекст, что делает её эффективным инструментом для обработки сложных запросов.

### Официальные источники

- [Официальный сайт Ollama](https://www.ollama.com)
- [Документация по Llama](https://www.ollama.com/llama)

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности смотрите в файле `LICENSE`.

### Пояснение к `README.md`:

- **Описание проекта**: Краткое описание, включая основные функции и возможности модели Llama.
- **Установка**: Инструкции по клонированию репозитория, созданию виртуального окружения и установке зависимостей.
- **Настройка**: Как создать файл `.env` и что в нем указывать.
- **Запуск и тестирование**: Как запустить скрипт `run.py` и протестировать функционал.
- **О модели Llama**: Краткое описание модели и ссылки на официальные источники.
