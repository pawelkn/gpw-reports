FROM python:3.8.13-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY gpw_reports/*.py ./gpw_reports/
RUN python -m compileall gpw_reports

COPY tests/*.py ./tests/
RUN python -m compileall tests

VOLUME /app/data

CMD ["python", "-u", "-m", "gpw_reports"]