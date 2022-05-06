import os, json
from sys import exit
from time import sleep
from random import randrange
from ssl import create_default_context
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from json.decoder import JSONDecodeError
from gpw_reports import EspiEbiReports

smtp_config_file = os.environ['GPW_REPORTS_SMTP_CONFIG_FILE'] if 'GPW_REPORTS_SMTP_CONFIG_FILE' in os.environ else 'data/smtp-config.json'
mailing_list_file = os.environ['GPW_REPORTS_MAILING_LIST_FILE'] if 'GPW_REPORTS_MAILING_LIST_FILE' in os.environ else 'data/mailing-list.json'
state_file = os.environ['GPW_REPORTS_STATE_FILE'] if 'GPW_REPORTS_STATE_FILE' in os.environ else 'data/state.json'

def readJsonFromFile(filename, default={}):
    try:
        with open(filename, 'r') as f:
            return json.loads(f.read())
    except JSONDecodeError:
        return default
    except FileNotFoundError:
        return default


def writeJsonToFile(filename, jsn):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w+') as f:
        f.write(json.dumps(jsn, indent=4))

def sendMail(reports, recipient):
    smtp_config = readJsonFromFile(smtp_config_file)

    message = MIMEMultipart("alternative")
    message["Subject"] = "GPW Report"
    message["From"] = "AutoSender <%s>" % smtp_config['sender']
    message["To"] = "%s <%s>" % (recipient['name'], recipient['email'])
    message.attach(MIMEText(reports.to_html(), "html"))

    with SMTP_SSL(smtp_config['host'], smtp_config['port'], context=create_default_context()) as server:
        server.login(smtp_config['login'], smtp_config['password'])
        server.sendmail(smtp_config['sender'], recipient['email'], message.as_string())

def main():
    try:
        while True:
            mailing_list = readJsonFromFile(mailing_list_file, [])
            state = readJsonFromFile(state_file)
            reports = EspiEbiReports()

            if 'last_id' not in state or state['last_id'] != reports[0].id:
                state['last_id'] = reports[0].id
                writeJsonToFile(state_file, state)            

            for recipient in mailing_list:
                recipient_reports = reports.filter(keywords=recipient['keywords'], last_id=state['last_id'])

                if len(recipient_reports) > 0:
                    print('Reports send:', len(recipient_reports))
                    sendMail(recipient_reports, recipient)

            sleep(randrange(60) + 30)

    except KeyboardInterrupt:
        exit(0)
