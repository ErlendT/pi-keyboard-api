FROM arm32v6/python:3.11-alpine

# Install packages
RUN pip install --no-cache-dir uvicorn starlite

COPY app ./app

CMD ["uvicorn", "app.main:app"]
