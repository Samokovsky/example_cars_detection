# Базовый образ с Python
FROM python:3.12.0

# Установка зависимостей
RUN apt-get update; apt-get install -y libgl1
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
# Копирование приложения в контейнер
COPY . /app

# Установка рабочей директории
WORKDIR /app

# Запуск мок-сервиса
CMD python main.py
