FROM python:3.9-alpine
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./src /code/src
COPY ./main.py /code/main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
