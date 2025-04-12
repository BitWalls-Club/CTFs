FROM python:3.12-slim

WORKDIR /app

COPY master.py .
COPY .env .

RUN pip install --no-cache-dir python-dotenv pyjwt

EXPOSE 1234

CMD ["python", "master.py"]
