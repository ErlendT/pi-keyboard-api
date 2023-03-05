FROM arm32v6/python:3.7-alpine

RUN pip install uvicorn starlite

COPY app ./app

CMD ["uvicorn", "app.main:app"]