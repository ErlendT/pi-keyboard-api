FROM arm32v6/python:3.11-alpine

# Install binaries
RUN apk update && apk add python3-dev \
                        gcc \
                        libc-dev \
                        libffi-dev
                        
# Install packages
RUN pip install --no-cache-dir setuptools uvicorn starlite

COPY app ./app

CMD ["uvicorn", "app.main:app"]
