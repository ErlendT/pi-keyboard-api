FROM arm32v6/python:3.11-alpine
WORKDIR /code
# Install binaries
RUN apk update && apk add python3-dev \
                        gcc \
                        libc-dev \
                        libffi-dev
                        
# Install packages
RUN pip install --no-cache-dir --upgrade setuptools uvicorn starlite

COPY ./app /code/app

EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
