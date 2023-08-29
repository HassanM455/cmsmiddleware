FROM python:3.9

WORKDIR /usr/app

COPY ./app/ /usr/app/

RUN pip install --no-cache-dir --upgrade -r /usr/app/requirements.txt

RUN apt-get update && apt-get install -y vim nano

EXPOSE 4001

WORKDIR /usr/app/src

ENTRYPOINT ["uvicorn", "main:app", "--host",  "0.0.0.0", "--port", "4001"]

