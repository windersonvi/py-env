FROM python:3.11.1

WORKDIR /app
COPY requirements.txt /app/requeriments.txt

RUN pip install -r /app/requeriments.txt

COPY .  /app

CMD ["fastapi", "run", "main.py", "--port", "80"]