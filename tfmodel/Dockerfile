FROM python:3.9.12-slim
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY tfmodel/requirements.txt /code/
RUN pip install -r requirements.txt
COPY tfmodel /code/