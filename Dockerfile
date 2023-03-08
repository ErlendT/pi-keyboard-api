FROM arm32v6/python:3.11-alpine

# Install packages
RUN pip install --no-cache-dir setuptools uvicorn starlite

COPY app ./app

CMD ["uvicorn", "app.main:app"]
