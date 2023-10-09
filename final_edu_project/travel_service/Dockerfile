FROM python:3.10

# Означает, что Python не будет пытаться создавать файлы .pyc, которые мы также не желаем.
ENV PYTHONDONTWRITEBYTECODE 1
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y upgrade
RUN apt-get install netcat-traditional
RUN apt-get install -y wkhtmltopdf xvfb

RUN pip install --upgrade pip

# рабочая директория
WORKDIR /my_app_directory

COPY ./requirements.txt .

RUN pip install -r requirements.txt

# Открываем порт
EXPOSE 8000
EXPOSE 8080
EXPOSE 6379
EXPOSE 6378


# copy entrypoint.sh
COPY ./entrypoint.sh .
# copy project
COPY . .
# run entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]