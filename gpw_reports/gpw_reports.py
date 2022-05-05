import os, json
from sys import exit
from time import sleep
from random import randrange
from ssl import create_default_context
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from gpw_reports import EspiEbiReports

config_file = os.environ['GPW_REPORTS_CONFIG_FILE'] if 'GPW_REPORTS_CONFIG_FILE' in os.environ else os.path.expanduser('config.json')
keywords_file = os.environ['GPW_REPORTS_KEYWORDS_FILE'] if 'GPW_REPORTS_KEYWORDS_FILE' in os.environ else os.path.expanduser('~/.gpw_reports/keywords.json')
state_file = os.environ['GPW_REPORTS_STATE_FILE'] if 'GPW_REPORTS_STATE_FILE' in os.environ else os.path.expanduser('~/.gpw_reports/state.json')

def readJsonFromFile(filename, default={}):
    try:
        with open(filename, 'r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return default


def writeJsonToFile(filename, jsn):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w+') as f:
        f.write(json.dumps(jsn, indent=4))

def sendEmail(reports):
    config = readJsonFromFile(config_file)

    message = MIMEMultipart("alternative")
    message["Subject"] = "GPW Report"
    message["From"] = "AutoSender <%s>" % config['sender']
    message["To"] = config['receiver']
    message.attach(MIMEText(reports.to_html(), "html"))

    with SMTP_SSL(config['smtp']['host'], config['smtp']['port'], context=create_default_context()) as server:
        server.login(config['smtp']['login'], config['smtp']['password'])
        server.sendmail(config['sender'], config['receiver'], message.as_string())

def main():
    try:
        while True:
            keywords = readJsonFromFile(keywords_file, [])
            state = readJsonFromFile(state_file)

            if 'id' not in state:
                state['id'] = 0

            reports = EspiEbiReports()
            reports = reports.filter(keywords=keywords, last_id=state['id'])

            if len(reports) == 0:
                print('No new reports')

            else:
                print('New reports:', len(reports))
                sendEmail(reports)
                
                state['id'] = reports[0].id
                writeJsonToFile(state_file, state)

            sleep(randrange(60) + 30)

    except KeyboardInterrupt:
        exit(0)
