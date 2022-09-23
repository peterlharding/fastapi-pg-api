
FROM python AS local-build

RUN apt update && \
    apt upgrade -y && \
    apt install -y gcc python3-dev libpq-dev postgresql-server-dev-all libffi-dev file make net-tools vim iputils-ping procps lsof

WORKDIR /opt/api

COPY requirements.txt /tmp

RUN python -m pip install -q pip --upgrade && \
    python -m pip install -r /tmp/requirements.txt

ADD   app     ./app
COPY start.sh run.py .env  ./
COPY PASSWORD.py ./app

RUN mkdir /var/log/api ; touch api.log

EXPOSE 8000

CMD ["./start.sh"]
# CMD sleep 120

