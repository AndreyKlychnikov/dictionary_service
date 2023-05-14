FROM python:3.11-slim

WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt
COPY ./src /code/src
ENV PYTHONPATH=/code
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]