FROM 3.10.2-alpine3.15

ENV PYTHONUNBUFFERED 1

RUN curl -sSL https://github.com/kelseyhightower/confd/releases/download/v0.16.0/confd-0.16.0-linux-amd64 -o /usr/local/bin/confd && \
  chmod +x /usr/local/bin/confd

RUN mkdir /python_discord_bot_yunner
COPY requirements.txt /python_discord_bot_yunner/
WORKDIR /python_discord_bot_yunner
RUN pip install -r requirements.txt
COPY . /python_discord_bot_yunner/

EXPOSE 8000

CMD ["uwsgi", "--ini", "shareable/wsgi/uwsgi.ini"]
