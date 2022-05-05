import re
import requests
from typing import List
from dataclasses import dataclass
from bs4 import BeautifulSoup


@dataclass
class EspiEbiReport:
    id: int
    date: str
    type: str
    category: str
    number: str
    company: str
    title: str
    url: str    


class EspiEbiReports(list):
    HOST = 'https://www.gpw.pl'    

    def __init__(self, reports: List[EspiEbiReport] = None):
        if reports is not None:
            self.__reports = reports
        else:
            self.__reports = self._parse(self._download())

    def __len__(self):
        return len(self.__reports)

    def __getitem__(self, index):
        return self.__reports.__getitem__(index)

    def filter(self, keywords: List[str] = [], last_id: int = 0):
        filtered = []

        for report in self.__reports:
            if report.id <= last_id:
                continue

            if len(keywords) == 0:
                filtered.append(report)
                continue

            for keyword in keywords:
                if keyword.lower() in report.type.lower() or \
                   keyword.lower() in report.category.lower() or \
                   keyword.lower() in report.number.lower() or \
                   keyword.lower() in report.company.lower() or \
                   keyword.lower() in report.title.lower():
                    filtered.append(report)
                    continue

        return EspiEbiReports(filtered)

    def to_html(self):
        html = '<html><table><thead><th>ID</th><th>Date</th><th>Type</th><th>Category</th><th>Number</th><th>Company</th><th>Title</th></thead><tbody>'

        for report in self.__reports:
            html = html + '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td><a href="{}">{}</a></td><td>{}</td></tr>' \
                .format(report.id, report.date, report.type, report.category, report.number, report.url, report.company, report.title)

        html = html + '</tbody></table></html>'
        
        html = html.replace('<table>', '<table style="border-collapse:collapse; width: 100%";>')
        html = html.replace('<th>', '<th style="font-size: 12px; font-family: system-ui; text-align: center; border: none; padding: 5px; font-weight: bold; color: #777; background-color: #f7f7f9; ">')
        html = html.replace('<tr>', '<tr style="border-top: solid 1px #ccc;">')
        html = html.replace('<td>', '<td style="font-size: 12px; font-family: system-ui; text-align: center; border: none; padding: 5px;">')
        return html

    def _download(self, offset: int = 0, limit: int = 30):
        url = self.HOST + "/ajaxindex.php" \
            "?action=GPWEspiReportUnion" \
            "&start=ajaxSearch" \
            "&page=espi-ebi-reports" \
            "&format=html" \
            "&lang=EN" \
            "&letter=" \
            "&offset=" + str(offset) + \
            "&limit=" + str(limit) + \
            "&categoryRaports%5B%5D=EBI" \
            "&categoryRaports%5B%5D=ESPI" \
            "&typeRaports%5B%5D=RB" \
            "&typeRaports%5B%5D=P" \
            "&typeRaports%5B%5D=Q" \
            "&typeRaports%5B%5D=O" \
            "&typeRaports%5B%5D=R" \
            "&search-xs=" \
            "&searchText=" \
            "&date="

        r = requests.get(url)
        if r.status_code != 200:
            raise Exception('Failed to download data form' + self.host)

        return r.text

    def _parse(self, text: str):
        reports = []

        soup = BeautifulSoup(text, 'html.parser')
        for li in soup.find_all('li'):
            a = li.find('a', attrs={'href': re.compile(r'^espi-ebi-report')})
            s = li.find('span', attrs={'class': 'date'})
            p = li.find('p')

            if a is not None and s is not None and p is not None:
                geru_id = re.findall(r'geru_id=(\d+)', a.get('href'))
                if len(geru_id) == 1:
                    id = int(geru_id[0])
                else:
                    continue

                parts = s.text.split('|')
                if len(parts) == 4:
                    date = parts[0].strip()
                    type = parts[1].strip()
                    category = parts[2].strip()
                    number = parts[3].strip()
                elif len(parts) == 3:
                    date = parts[0].strip()
                    type = None
                    category = parts[1].strip()
                    number = parts[2].strip()
                else:
                    continue

                company = a.text.strip()
                title = p.text.strip()
                url = self.HOST + '/' + a.get('href')

                report = EspiEbiReport(id, date, type, category, number, company, title, url)
                reports.append(report)

        return reports
