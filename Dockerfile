FROM python:3.8

COPY . /app

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python"]

CMD ["app.py"]