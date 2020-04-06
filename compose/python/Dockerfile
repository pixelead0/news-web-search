FROM python:3.8
RUN mkdir /code
WORKDIR /code

COPY ./src/entrypoint.sh /code/entrypoint.sh
COPY ./src/requirements.txt /code/requirements.txt

RUN pip install --upgrade pip

CMD ["sh entrypoint.sh"]
