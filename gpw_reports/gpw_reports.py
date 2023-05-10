import os
import sys
import json
import logging

from time import sleep
from random import randrange
from ssl import create_default_context
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from json.decoder import JSONDecodeError
from gpw_reports import EspiEbiReports

logging.basicConfig(level=logging.INFO, format='[%(asctime)s][%(levelname)s] %(message)s')

SMTP_CONFIG_FILE = os.environ.get('GPW_REPORTS_SMTP_CONFIG_FILE', 'smtp-config.json')
MAILING_LIST_FILE = os.environ.get('GPW_REPORTS_MAILING_LIST_FILE', 'mailing-list.json')
STATE_FILE = os.environ.get('GPW_REPORTS_STATE_FILE', 'data/state.json')

def readJsonFromFile(filename: str, default={}):
    try:
        with open(filename, 'r') as f:
            return json.loads(f.read())
    except JSONDecodeError:
        return default
    except FileNotFoundError:
        return default

def writeJsonToFile(filename: str, jsn):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w+') as f:
        f.write(json.dumps(jsn, indent=4))


def sendMail(recipient: str, reports: EspiEbiReports):
    smtp_config = readJsonFromFile(SMTP_CONFIG_FILE)

    message = MIMEMultipart('alternative')
    message['Subject'] = 'GPW ESPI/EBI Reports'

    frm = Header('GPW Reports (AutoSender)', 'utf-8')
    frm.append('<%s>' % smtp_config['sender'], 'ascii')

    to = Header(recipient['name'], 'utf-8')
    to.append('<%s>' % recipient['mail'], 'ascii')

    message['From'] = frm
    message['To'] = to

    html = reports.to_html()
    message.attach(MIMEText(html, 'html'))

    with SMTP_SSL(smtp_config['host'], smtp_config['port'], context=create_default_context()) as server:
        server.login(smtp_config['login'], smtp_config['password'])
        server.sendmail(smtp_config['sender'], recipient['mail'], message.as_string())


def scrapReportsAndNotifyRecipients():
    reports = EspiEbiReports()
    if len(reports) == 0:
        return

    state = readJsonFromFile(STATE_FILE)
    if 'last_id' not in state or type(state['last_id']) != int:
        state['last_id'] = 0

    last_report = max(reports, key=lambda report: report.id)
    logging.info(f'Current state id: {state["last_id"]}, downloaded reports: {len(reports)}, last report id: {last_report.id}')

    if state['last_id'] >= last_report.id:
        return

    mailing_list = readJsonFromFile(MAILING_LIST_FILE, [])
    for recipient in mailing_list:
        filtered_reports = reports.filter(keywords=recipient['keywords'], last_id=state['last_id'])
        if len(filtered_reports) == 0:
            continue

        sendMail(recipient, filtered_reports)
        logging.info(f'Sending {len(filtered_reports)} reports to {recipient["name"]}')

    state['last_id'] = last_report.id
    writeJsonToFile(STATE_FILE, state)

def main():
    while True:
        scrapReportsAndNotifyRecipients()

        # sleep from 30 to 90 secs. (around 60 secs.)
        sleep(randrange(60) + 30)