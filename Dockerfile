FROM python:3.11.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py migrate
RUN python manage.py loaddata house_data.json
RUN python manage.py loaddata resident_data.json

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
