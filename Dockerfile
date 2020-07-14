FROM python:3.8.2-slim
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]