FROM python:3.9.5

WORKDIR ./

COPY ./requirements.txt ./requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean


RUN pip install -r /requirements.txt \
    && rm -rf /root/.cache/pip

COPY ./ ./

CMD uvicorn main:app --proxy-headers --host 0.0.0.0 --port 8000

