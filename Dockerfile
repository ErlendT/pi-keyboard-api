FROM arm32v6/python:3.11-alpine

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools uvicorn starlite

COPY app ./app

CMD ["uvicorn", "app.main:app"]
