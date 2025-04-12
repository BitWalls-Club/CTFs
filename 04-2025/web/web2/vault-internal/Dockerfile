FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install python-dotenv
EXPOSE 8000
CMD ["python", "vault_server.py"]
