FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app/

RUN pip install poetry
RUN poetry install
RUN pip install uvicorn
RUN python -m pip install fastapi uvicorn[standard]

ENV PATH="$PATH:/usr/local/bin/"

EXPOSE 8000

CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
