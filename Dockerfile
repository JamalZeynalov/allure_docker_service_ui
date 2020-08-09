FROM python:3.8.2-slim
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

RUN apt-get update && apt-get dist-upgrade -y && apt-get install apt-utils -y && apt-get install curl -y && apt-get install vim -y

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]