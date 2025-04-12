FROM python:3.12-slim
RUN useradd -m app
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    chromium \
    chromium-driver \
    fonts-liberation \
    libnss3 \
    libxss1 \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libgbm1 \
    libgtk-3-0 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /home/app/app
COPY . .
RUN chown -R app:app /home/app
USER app
ENV PATH="/home/app/.local/bin:$PATH"
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/lib/chromium/chromedriver
RUN pip install --no-cache-dir --user -r requirements.txt
EXPOSE 1337
CMD bash -c "python manage.py migrate && \
             nohup daphne devnoms.asgi:application -b 0.0.0.0 -p 1337 & \
             echo 'Waiting for server to be ready...' && \
             until curl -s http://127.0.0.1:1337/signup/ > /dev/null; do sleep 1; done && \
             echo 'Server is ready.' && \
             python automate/register_users.py && \
             python automate/admin_bot.py"

