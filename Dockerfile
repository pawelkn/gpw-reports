FROM python:3.8.13-alpine

RUN apk add --no-cache tini

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY gpw_reports/*.py ./gpw_reports/
RUN python -m compileall gpw_reports

COPY tests/*.py ./tests/
RUN python -m compileall tests

VOLUME /root/.gpw_reports

CMD ["/sbin/tini", "python", "-u", "-m", "gpw_reports"]