FROM python:3.11

RUN pip install uvicorn starlite

COPY app ./app

CMD ["uvicorn", "app.main:app"]