# GPW Reports

[![Test gpw-reports](https://github.com/pawelkn/gpw-reports/actions/workflows/test-gpw-reports.yml/badge.svg)](https://github.com/pawelkn/gpw-reports/actions/workflows/test-gpw-reports.yml)

GPW Reports is a keyword scanner of GPW (Warsaw Stock Exchange) ESPI/EBI Company reports. Periodically scraps the <https://www.gpw.pl/espi-ebi-reports> site,  searching for keywords in reports. When matching report is found, sends a notification email.

## Configuration

Mail host configuration. To deliver a notification mails an external SMTP service is used. 

To configure SMTP, you will have to create a configuration file *data/smtp-config.json* and enter your sender account settings.

Example (**data/smtp-config.json**):

```json
{
    "sender": "sender@gmail.com",
    "host": "smtp.gmail.com",
    "port": 465,
    "login": "username",
    "password": "password"
}
```

Mailing list. The mailing list is kept in *data/mailing-list.json* file. It contains mail addresses and attached keywords. Keywords are case insensitive. If an empty keywords list is set, all reports are mailed.

Example (**data/mailing-list.json**):

```json
[
    {
        "name": "Recipient Name 1",
        "email": "recipient_1@gmail.com",
        "keywords": [
            "KGHM",
            "CD Projekt",
            "transakcj"
        ]
    },
    {
        "name": "Recipient Name 2",
        "email": "recipient_2@gmail.com",
        "keywords": []
    }
]
```

Location of configuration and state files can be configured using environment variables.

Example:

```sh
export GPW_REPORTS_SMTP_CONFIG_FILE=data/smtp-config.json
export GPW_REPORTS_MAILING_LIST_FILE=data/mailing-list.json
export GPW_REPORTS_STATE_FILE=data/state.json
```

## Run

> ***Note:*** Before run create valid [configuration](##Configuration) files: *data/smtp-config.json* and *data/mailing-list.json*

Install dependencies

```sh
pip3 install -r requirements.txt
```

Application start

```sh
python3 -m gpw_reports
```

## Docker

> ***Note:*** Before run create valid [configuration](##Configuration) files: *data/smtp-config.json* and *data/mailing-list.json*

To avoid python version conflict and/or dependencies installation run application in docker container

```sh
docker-compose up --build
```

## Unit tests

```sh
python3 -m unittest discover tests
```
