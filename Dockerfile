FROM python:3.10
# Устанавливаем рабочий каталог внутри контейнера
WORKDIR /app
# копирование файлов проекта
COPY . /app
# обновление pip и установка requirements
RUN pip install -U pip
RUN pip install -r requirements.txt
ENTRYPOINT ["pytest"]
# Создать директорию allure-results внутри контейнера
RUN mkdir /allure-results
