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

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)

smtp_config_file = os.environ['GPW_REPORTS_SMTP_CONFIG_FILE'] if 'GPW_REPORTS_SMTP_CONFIG_FILE' in os.environ else 'data/smtp-config.json'
mailing_list_file = os.environ['GPW_REPORTS_MAILING_LIST_FILE'] if 'GPW_REPORTS_MAILING_LIST_FILE' in os.environ else 'data/mailing-list.json'
state_file = os.environ['GPW_REPORTS_STATE_FILE'] if 'GPW_REPORTS_STATE_FILE' in os.environ else 'data/state.json'

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
    smtp_config = readJsonFromFile(smtp_config_file)

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

    state = readJsonFromFile(state_file)
    if 'last_id' in state and state['last_id'] != reports[0].id:

        mailing_list = readJsonFromFile(mailing_list_file, [])
        for recipient in mailing_list:
            filtered_reports = reports.filter(keywords=recipient['keywords'], last_id=state['last_id'])

            if len(filtered_reports) > 0:                
                sendMail(recipient, filtered_reports)
                logger.info({'reports_send': len(filtered_reports)})

    state['last_id'] = reports[0].id          
    writeJsonToFile(state_file, state)
    logger.info({'state': state})

def main():
    while True:
        scrapReportsAndNotifyRecipients()

        # sleep from 30 to 90 secs. (around 60 secs.)
        sleep(randrange(60) + 30)