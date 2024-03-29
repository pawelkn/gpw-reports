FROM python:3.12-rc-alpine

WORKDIR /app

RUN addgroup --gid 1000 -S python  && adduser --uid 1000 -S python -G python

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY gpw_reports/*.py ./gpw_reports/
RUN python -m compileall gpw_reports

COPY tests/*.py ./tests/
RUN python -m compileall tests

VOLUME /app/data

CMD ["python", "-u", "-m", "gpw_reports"]