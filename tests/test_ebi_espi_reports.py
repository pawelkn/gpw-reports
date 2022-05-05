import unittest
from unittest.mock import Mock
from gpw_reports import EspiEbiReports

class TestEspiEbiReports(unittest.TestCase):

    def setUp(self):
        EspiEbiReports._download = Mock(return_value=download_output)

    def test_reports(self):
        reports = EspiEbiReports()

        self.assertEqual(len(reports), 30)
        self.assertEqual(reports[0].id, 395960)
        self.assertEqual(reports[0].date, '05-05-2022 12:43:03')
        self.assertEqual(reports[0].type, 'Current')
        self.assertEqual(reports[0].category, 'ESPI')
        self.assertEqual(reports[0].number, '14/2022')
        self.assertEqual(reports[0].company, 'ZAKŁAD BUDOWY MASZYN ZREMB-CHOJNICE SPÓŁKA AKCYJNA (PLZBMZC00019)')
        self.assertEqual(reports[0].title, 'Podpisanie porozumienia w sprawie wspólnej realizacji projektu.')
        self.assertEqual(reports[0].url, 'https://www.gpw.pl/espi-ebi-report?geru_id=395960&title=Podpisanie+porozumienia+w+sprawie+wsp%C3%B3lnej+realizacji+projektu.')

    def test_filter(self):
        reports = EspiEbiReports()

        filtered = reports.filter(keywords=[])
        self.assertEqual(len(filtered), 30)
        self.assertEqual(filtered[0].id, 395960)

        filtered = reports.filter(last_id=395957)
        self.assertEqual(len(filtered), 3)
        self.assertEqual(filtered[0].id, 395960)

        filtered = reports.filter(['ebi'])
        self.assertEqual(len(filtered), 0)

        filtered = reports.filter(['espi'])
        self.assertEqual(len(filtered), 30)

        filtered = reports.filter(['annual'])
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].id, 395932)

        filtered = reports.filter(['budimex'])
        self.assertEqual(len(filtered), 2)
        self.assertEqual(filtered[0].id, 395916)
        self.assertEqual(filtered[1].id, 395915)

        filtered = reports.filter(['transakcje'])
        self.assertEqual(len(filtered), 0)

        filtered = reports.filter(['transakcj'])
        self.assertEqual(len(filtered), 2)

        filtered = reports.filter(['transakcj'], 395957)
        self.assertEqual(len(filtered), 1)

        filtered = reports.filter(['podziału zysku netto'])
        self.assertEqual(len(filtered), 1)

        filtered = reports.filter(['podziału zysku netto'], 395957)
        self.assertEqual(len(filtered), 0)

        filtered = reports.filter(['podziału zysku netto', 'transakcj'])
        self.assertEqual(len(filtered), 3)

    def test_to_html(self):
        reports = EspiEbiReports()
        filtered = reports.filter(last_id=395959)
        html = filtered.to_html()

        self.assertEqual(html, html_reference)


if __name__ == '__main__':
    unittest.main()

download_output = """



<li style="padding: 15px 0;">
	    <span class="date">05-05-2022 12:43:03 | Current | ESPI | 14/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395960&amp;title=Podpisanie+porozumienia+w+sprawie+wsp%C3%B3lnej+realizacji+projektu.">
        	        	ZAKŁAD BUDOWY MASZYN ZREMB-CHOJNICE SPÓŁKA AKCYJNA (PLZBMZC00019)
        </a>
    </strong>
        <span class="loss margin-left-30 pull-right"><small>Change</small> 1,58% <i class="icon-down"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>1,87</span>
        <p>
                				Podpisanie porozumienia w sprawie wspólnej realizacji projektu.
            </p>
        <a href="espi-ebi-report?geru_id=395960&amp;title=Podpisanie+porozumienia+w+sprawie+wsp%C3%B3lnej+realizacji+projektu.">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">05-05-2022 11:26:51 | Current | ESPI | 7/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395959&amp;title=Uzupe%C5%82nienie+do+RB-6_2022+z+dnia+29.04.2022+r.">
        	        	MOJ SPÓŁKA AKCYJNA (PLMOJ0000015)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 0,00% <i class="icon-"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>1,82</span>
        <p>
                				Uzupełnienie do RB-6_2022 z dnia 29.04.2022 r.
            </p>
        <a href="espi-ebi-report?geru_id=395959&amp;title=Uzupe%C5%82nienie+do+RB-6_2022+z+dnia+29.04.2022+r.">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">05-05-2022 11:19:49 | Current | ESPI | 26/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395958&amp;title=Powiadomienie+o+transakcji+na+akcjach+Apator+SA">
        	        	APATOR SPÓŁKA AKCYJNA (PLAPATR00018)
        </a>
    </strong>
        <span class="loss margin-left-30 pull-right"><small>Change</small> 0,23% <i class="icon-down"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>17,00</span>
        <p>
                				Powiadomienie o transakcji na akcjach Apator SA
            </p>
        <a href="espi-ebi-report?geru_id=395958&amp;title=Powiadomienie+o+transakcji+na+akcjach+Apator+SA">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">05-05-2022 11:09:47 | Current | ESPI | 2/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395957&amp;title=Rekomendacja+Zarz%C4%85du+Rawlplug+S.A.+co+do+podzia%C5%82u+zysku+netto+za+rok+obrotowy+2021+i+wyp%C5%82aty+dywidendy">
        	        	RAWLPLUG SPÓŁKA AKCYJNA (PLKLNR000017)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 1,92% <i class="icon-up"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>15,90</span>
        <p>
                				Rekomendacja Zarządu Rawlplug S.A. co do podziału zysku netto za rok obrotowy 2021 i wypłaty dywidendy
            </p>
        <a href="espi-ebi-report?geru_id=395957&amp;title=Rekomendacja+Zarz%C4%85du+Rawlplug+S.A.+co+do+podzia%C5%82u+zysku+netto+za+rok+obrotowy+2021+i+wyp%C5%82aty+dywidendy">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">05-05-2022 10:10:37 | Current | ESPI | 27/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395956&amp;title=Przychody+ze+sprzeda%C5%BCy+netto+Sp%C3%B3%C5%82ki+osi%C4%85gni%C4%99te+w+kwietniu+2022+roku">
        	        	OPONEO.PL SPÓŁKA AKCYJNA (PLOPNPL00013)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 0,00% <i class="icon-"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>45,50</span>
        <p>
                				Przychody ze sprzedaży netto Spółki osiągnięte w kwietniu 2022 roku
            </p>
        <a href="espi-ebi-report?geru_id=395956&amp;title=Przychody+ze+sprzeda%C5%BCy+netto+Sp%C3%B3%C5%82ki+osi%C4%85gni%C4%99te+w+kwietniu+2022+roku">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">05-05-2022 09:44:33 | Current | ESPI | 6/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395955&amp;title=Uprawomocnienie+si%C4%99+postanowienia+o+oddaleniu+wniosku+o+otwarcie+post%C4%99powania+sanacyjnego+oraz+o+og%C5%82oszeniu+upad%C5%82o%C5%9Bci+URSUS+S.A.">
        	        	URSUS SPÓŁKA AKCYJNA W UPADŁOŚCI (PLPMWRM00012)
        </a>
    </strong>
        <span class="loss margin-left-30 pull-right"><small>Change</small> 20,60% <i class="icon-down"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>0,24</span>
        <p>
                				Uprawomocnienie się postanowienia o oddaleniu wniosku o otwarcie postępowania sanacyjnego oraz o ogłoszeniu upadłości URSUS S.A.
            </p>
        <a href="espi-ebi-report?geru_id=395955&amp;title=Uprawomocnienie+si%C4%99+postanowienia+o+oddaleniu+wniosku+o+otwarcie+post%C4%99powania+sanacyjnego+oraz+o+og%C5%82oszeniu+upad%C5%82o%C5%9Bci+URSUS+S.A.">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">05-05-2022 09:37:31 | Current | ESPI | 5/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395954&amp;title=Oddalenie+za%C5%BCalenia+wierzyciela+Emitenta+od+pkt+VI+rozstrzygni%C4%99cia+o+jurysdykcji+s%C4%85d%C3%B3w+polskich+postanowienia+S%C4%85du+Rejonowego+dla+m.st.+Warszawy+w+Warszawie+XVIII+Wydzia%C5%82+Gospodarczy+dla+spraw+upad%C5%82o%C5%9Bciowych+i%C2%A0restrukturyzacyjnych+z+dnia+12+lipca+2021+r">
        	        	URSUS SPÓŁKA AKCYJNA W UPADŁOŚCI (PLPMWRM00012)
        </a>
    </strong>
        <span class="loss margin-left-30 pull-right"><small>Change</small> 20,60% <i class="icon-down"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>0,24</span>
        <p>
                				Oddalenie zażalenia wierzyciela Emitenta od pkt VI (rozstrzygnięcia o jurysdykcji sądów polskich) postanowienia Sądu Rejonowego dla m.st. Warszawy w Warszawie XVIII Wydział Gospodarczy dla spraw upadłościowych i restrukturyzacyjnych z dnia 12 lipca 2021 r
            </p>
        <a href="espi-ebi-report?geru_id=395954&amp;title=Oddalenie+za%C5%BCalenia+wierzyciela+Emitenta+od+pkt+VI+rozstrzygni%C4%99cia+o+jurysdykcji+s%C4%85d%C3%B3w+polskich+postanowienia+S%C4%85du+Rejonowego+dla+m.st.+Warszawy+w+Warszawie+XVIII+Wydzia%C5%82+Gospodarczy+dla+spraw+upad%C5%82o%C5%9Bciowych+i%C2%A0restrukturyzacyjnych+z+dnia+12+lipca+2021+r">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">05-05-2022 09:33:30 | Current | ESPI | 19/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395953&amp;title=Zmiana+daty+publikacji+raportu+okresowego+Sp%C3%B3%C5%82ki+za+I+kwarta%C5%82+2022r.">
        	        	STALPROFIL SPÓŁKA AKCYJNA (PLSTLPF00012)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 2,01% <i class="icon-up"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>12,16</span>
        <p>
                				Zmiana daty publikacji raportu okresowego Spółki za I kwartał 2022r.
            </p>
        <a href="espi-ebi-report?geru_id=395953&amp;title=Zmiana+daty+publikacji+raportu+okresowego+Sp%C3%B3%C5%82ki+za+I+kwarta%C5%82+2022r.">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">05-05-2022 08:16:13 | Current | ESPI | 35/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395950&amp;title=UniCredit+above+MREL+requirements+set+by+Resolution+Authorities">
        	        	UNICREDIT S.P.A. (IT0005239360)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 5,00% <i class="icon-up"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>42,00</span>
        <p>
                				UniCredit above MREL requirements set by Resolution Authorities
            </p>
        <a href="espi-ebi-report?geru_id=395950&amp;title=UniCredit+above+MREL+requirements+set+by+Resolution+Authorities">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">05-05-2022 07:16:55 | Current | ESPI | 34/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395943&amp;title=UniCredit%3A+1Q22+Group+Results.+Record+setting+first+quarter+delivering+UniCredit+Unlocked+targets+across+all+metrics">
        	        	UNICREDIT S.P.A. (IT0005239360)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 5,00% <i class="icon-up"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>42,00</span>
        <p>
                				UniCredit: 1Q22 Group Results. Record setting first quarter delivering UniCredit Unlocked targets across all metrics
            </p>
        <a href="espi-ebi-report?geru_id=395943&amp;title=UniCredit%3A+1Q22+Group+Results.+Record+setting+first+quarter+delivering+UniCredit+Unlocked+targets+across+all+metrics">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">05-05-2022 06:48:50 | Current | ESPI | 5/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395942&amp;title=Szacunkowe+skonsolidowane+wyniki+pierwszego+kwarta%C5%82u+2022+r.">
        	        	SHOPER SPÓŁKA AKCYJNA (PLSHPR000021)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 2,19% <i class="icon-up"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>44,40</span>
        <p>
                				Szacunkowe skonsolidowane wyniki pierwszego kwartału 2022 r.
            </p>
        <a href="espi-ebi-report?geru_id=395942&amp;title=Szacunkowe+skonsolidowane+wyniki+pierwszego+kwarta%C5%82u+2022+r.">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">05-05-2022 00:08:48 | Quarterly | ESPI | /2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395934">
        	        	ASBISC ENTERPRISES PLC (CY1000031710)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 0,75% <i class="icon-up"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>13,49</span>
        <p>
                				
            </p>
        <a href="espi-ebi-report?geru_id=395934">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">04-05-2022 21:13:20 | Current | ESPI | 15/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395933&amp;title=Powiadomienia+dotycz%C4%85ce+transakcji+os%C3%B3b+pe%C5%82ni%C4%85cych+obowi%C4%85zki+zarz%C4%85dcze">
        	        	SERINUS ENERGY PLC (JE00BF4N9R98)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 3,61% <i class="icon-up"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>0,86</span>
        <p>
                				Powiadomienia dotyczące transakcji osób pełniących obowiązki zarządcze
            </p>
        <a href="espi-ebi-report?geru_id=395933&amp;title=Powiadomienia+dotycz%C4%85ce+transakcji+os%C3%B3b+pe%C5%82ni%C4%85cych+obowi%C4%85zki+zarz%C4%85dcze">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">04-05-2022 20:44:58 | Annual | ESPI | /</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395932">
        	        	ENERGOINSTAL SPÓŁKA AKCYJNA (PLERGIN00015)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 0,00% <i class="icon-"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>0,86</span>
        <p>
                				
            </p>
        <a href="espi-ebi-report?geru_id=395932">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">04-05-2022 20:33:54 | Current | ESPI | 20/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395931&amp;title=INFORMACJE+O+OSOBIE+ZARZ%C4%84DZAJ%C4%84CEJ">
        	        	OPEN FINANCE SPÓŁKA AKCYJNA (PLOPNFN00010)
        </a>
    </strong>
        <span class="loss margin-left-30 pull-right"><small>Change</small> 32,43% <i class="icon-down"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>0,15</span>
        <p>
                				INFORMACJE O OSOBIE ZARZĄDZAJĄCEJ
            </p>
        <a href="espi-ebi-report?geru_id=395931&amp;title=INFORMACJE+O+OSOBIE+ZARZ%C4%84DZAJ%C4%84CEJ">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">04-05-2022 20:21:50 | Current | ESPI | 19/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395930&amp;title=WYDANIE+POSTANOWIENIA+O+OG%C5%81OSZENIU+UPAD%C5%81O%C5%9ACI+OPEN+FINANCE+S.A.">
        	        	OPEN FINANCE SPÓŁKA AKCYJNA (PLOPNFN00010)
        </a>
    </strong>
        <span class="loss margin-left-30 pull-right"><small>Change</small> 32,43% <i class="icon-down"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>0,15</span>
        <p>
                				WYDANIE POSTANOWIENIA O OGŁOSZENIU UPADŁOŚCI OPEN FINANCE S.A.
            </p>
        <a href="espi-ebi-report?geru_id=395930&amp;title=WYDANIE+POSTANOWIENIA+O+OG%C5%81OSZENIU+UPAD%C5%81O%C5%9ACI+OPEN+FINANCE+S.A.">more &gt;</a>
</li>
<li style="padding: 15px 0;">
    <span class="date">04-05-2022 20:16:41 | Current | ESPI | /2021</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395929">
        	        	ARTERIA SPÓŁKA AKCYJNA (PLARTER00016)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 0,00% <i class="icon-"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>7,74</span>
        <p>
                				
            </p>
        <a href="espi-ebi-report?geru_id=395929">more &gt;</a>
</li>
<li style="padding: 15px 0;">
    <span class="date">04-05-2022 20:07:36 | Current | ESPI | /2021</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395928">
        	        	ARTERIA SPÓŁKA AKCYJNA (PLARTER00016)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 0,00% <i class="icon-"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>7,74</span>
        <p>
                				
            </p>
        <a href="espi-ebi-report?geru_id=395928">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">04-05-2022 19:36:32 | Current | ESPI | 9/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395927&amp;title=Naruszenie+kowenantu+finansowego+uprawniaj%C4%85ce+do+%C5%BC%C4%85dania+przedterminowego+wykupu+obligacji+serii+B">
        	        	EUROPEJSKIE CENTRUM ODSZKODOWAŃ SPÓŁKA AKCYJNA (PLERPCO00017)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 3,45% <i class="icon-up"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>2,40</span>
        <p>
                				Naruszenie kowenantu finansowego uprawniające do żądania przedterminowego wykupu obligacji serii B
            </p>
        <a href="espi-ebi-report?geru_id=395927&amp;title=Naruszenie+kowenantu+finansowego+uprawniaj%C4%85ce+do+%C5%BC%C4%85dania+przedterminowego+wykupu+obligacji+serii+B">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">04-05-2022 19:25:28 | Current | ESPI | 4/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395926&amp;title=Og%C5%82oszenie+o+zwo%C5%82aniu+Zwyczajnego+Walnego+Zgromadzenia+Shoper+S.A.">
        	        	SHOPER SPÓŁKA AKCYJNA (PLSHPR000021)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 2,19% <i class="icon-up"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>44,40</span>
        <p>
                				Ogłoszenie o zwołaniu Zwyczajnego Walnego Zgromadzenia Shoper S.A.
            </p>
        <a href="espi-ebi-report?geru_id=395926&amp;title=Og%C5%82oszenie+o+zwo%C5%82aniu+Zwyczajnego+Walnego+Zgromadzenia+Shoper+S.A.">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">04-05-2022 19:16:26 | Current | ESPI | 42/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395925&amp;title=Zawarcie+umowy+cesji+wierzytelno%C5%9Bci+na+rynku+hiszpa%C5%84skim">
        	        	KRUK SPÓŁKA AKCYJNA (PLKRK0000010)
        </a>
    </strong>
        <span class="loss margin-left-30 pull-right"><small>Change</small> 0,73% <i class="icon-down"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>246,00</span>
        <p>
                				Zawarcie umowy cesji wierzytelności na rynku hiszpańskim
            </p>
        <a href="espi-ebi-report?geru_id=395925&amp;title=Zawarcie+umowy+cesji+wierzytelno%C5%9Bci+na+rynku+hiszpa%C5%84skim">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">04-05-2022 19:15:25 | Current | ESPI | 41/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395924&amp;title=Rejestracja+zmiany+statutu+KRUK+S.A.">
        	        	KRUK SPÓŁKA AKCYJNA (PLKRK0000010)
        </a>
    </strong>
        <span class="loss margin-left-30 pull-right"><small>Change</small> 0,73% <i class="icon-down"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>246,00</span>
        <p>
                				Rejestracja zmiany statutu KRUK S.A.
            </p>
        <a href="espi-ebi-report?geru_id=395924&amp;title=Rejestracja+zmiany+statutu+KRUK+S.A.">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">04-05-2022 19:11:24 | Current | ESPI | 38/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395923&amp;title=Otrzymanie+decyzji+Polskiego+Funduszu+Rozwoju+w+przedmiocie+zwolnienia+z+obowi%C4%85zku+zwrotu+subwencji+finansowej+w+ramach+programu+Tarcza+Finansowa+PFR+dla+Ma%C5%82ych+i+%C5%9Arednich+Firm">
        	        	MIRACULUM SPÓŁKA AKCYJNA (PLKLSTN00017)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 0,00% <i class="icon-"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>1,27</span>
        <p>
                				Otrzymanie decyzji Polskiego Funduszu Rozwoju w przedmiocie zwolnienia z obowiązku zwrotu subwencji finansowej w ramach programu Tarcza Finansowa PFR dla Małych i Średnich Firm
            </p>
        <a href="espi-ebi-report?geru_id=395923&amp;title=Otrzymanie+decyzji+Polskiego+Funduszu+Rozwoju+w+przedmiocie+zwolnienia+z+obowi%C4%85zku+zwrotu+subwencji+finansowej+w+ramach+programu+Tarcza+Finansowa+PFR+dla+Ma%C5%82ych+i+%C5%9Arednich+Firm">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">04-05-2022 18:47:19 | Current | ESPI | 4/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395922&amp;title=Og%C5%82oszenie+Zarz%C4%85du+Asseco+Business+Solutions+o+zwo%C5%82aniu+Zwyczajnego+Walnego+Zgromadzenia">
        	        	ASSECO BUSINESS SOLUTIONS SPÓŁKA AKCYJNA (PLABS0000018)
        </a>
    </strong>
        <span class="loss margin-left-30 pull-right"><small>Change</small> 0,97% <i class="icon-down"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>40,90</span>
        <p>
                				Ogłoszenie Zarządu Asseco Business Solutions o zwołaniu Zwyczajnego Walnego Zgromadzenia
            </p>
        <a href="espi-ebi-report?geru_id=395922&amp;title=Og%C5%82oszenie+Zarz%C4%85du+Asseco+Business+Solutions+o+zwo%C5%82aniu+Zwyczajnego+Walnego+Zgromadzenia">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">04-05-2022 18:19:14 | Current | ESPI | 5/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395919&amp;title=Protok%C3%B3%C5%82+Nadzwyczajnego+Walnego+Zgromadzenia+Akcjonariuszy+Sp%C3%B3%C5%82ki+Investment+Friends+Capital+SE+z+dnia+04.05.2022+r.+Protocol+of+the+Extraordinary+General+Meeting+of+Shareholders+of+Investment+Friends+Capital+SE+of+4%2F05%2F2022.">
        	        	INVESTMENT FRIENDS CAPITAL SE (EE3100065392)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 0,00% <i class="icon-"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>1,03</span>
        <p>
                				Protokół Nadzwyczajnego Walnego Zgromadzenia Akcjonariuszy Spółki Investment Friends Capital SE z dnia 04.05.2022 r. (Protocol of the Extraordinary General Meeting of Shareholders of Investment Friends Capital SE of 4/05/2022.)
            </p>
        <a href="espi-ebi-report?geru_id=395919&amp;title=Protok%C3%B3%C5%82+Nadzwyczajnego+Walnego+Zgromadzenia+Akcjonariuszy+Sp%C3%B3%C5%82ki+Investment+Friends+Capital+SE+z+dnia+04.05.2022+r.+Protocol+of+the+Extraordinary+General+Meeting+of+Shareholders+of+Investment+Friends+Capital+SE+of+4%2F05%2F2022.">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">04-05-2022 18:15:11 | Current | ESPI | 7/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395918&amp;title=Wst%C4%99pne+wybrane+skonsolidowane+dane+finansowe+Grupy+Kapita%C5%82owej+CCC+za+I+kwarta%C5%82+2022+roku">
        	        	CCC SPÓŁKA AKCYJNA (PLCCC0000016)
        </a>
    </strong>
        <span class="loss margin-left-30 pull-right"><small>Change</small> 0,66% <i class="icon-down"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>51,20</span>
        <p>
                				Wstępne wybrane skonsolidowane dane finansowe Grupy Kapitałowej CCC za I kwartał 2022 roku
            </p>
        <a href="espi-ebi-report?geru_id=395918&amp;title=Wst%C4%99pne+wybrane+skonsolidowane+dane+finansowe+Grupy+Kapita%C5%82owej+CCC+za+I+kwarta%C5%82+2022+roku">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">04-05-2022 18:10:10 | Current | ESPI | 26/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395916&amp;title=%22Budowa+nowej+siedziby+i+zagospodarowanie+terenu+PSE+S.A.+w+Radomiu%22+-+uniewa%C5%BCnienie+czynno%C5%9Bci+wyboru">
        	        	BUDIMEX SPÓŁKA AKCYJNA (PLBUDMX00013)
        </a>
    </strong>
        <span class="loss margin-left-30 pull-right"><small>Change</small> 0,48% <i class="icon-down"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>207,00</span>
        <p>
                				&quot;Budowa nowej siedziby i zagospodarowanie terenu PSE S.A. w Radomiu&quot; - unieważnienie czynności wyboru
            </p>
        <a href="espi-ebi-report?geru_id=395916&amp;title=%22Budowa+nowej+siedziby+i+zagospodarowanie+terenu+PSE+S.A.+w+Radomiu%22+-+uniewa%C5%BCnienie+czynno%C5%9Bci+wyboru">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">04-05-2022 18:09:09 | Current | ESPI | 7/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395914&amp;title=Protok%C3%B3%C5%82+Nadzwyczajnego+Walnego+Zgromadzenia+Akcjonariuszy+Sp%C3%B3%C5%82ki+FON+SE+z+dnia+04.05.2022+r.+Protocol+of+the+Extraordinary+General+Meeting+of+Shareholders+of+FON+SE+of+4%2F05%2F2022.">
        	        	FON SE (EE3100005166)
        </a>
    </strong>
        <span class="loss margin-left-30 pull-right"><small>Change</small> 2,27% <i class="icon-down"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>0,22</span>
        <p>
                				Protokół Nadzwyczajnego Walnego Zgromadzenia Akcjonariuszy Spółki FON SE z dnia 04.05.2022 r. (Protocol of the Extraordinary General Meeting of Shareholders of FON SE of 4/05/2022.)
            </p>
        <a href="espi-ebi-report?geru_id=395914&amp;title=Protok%C3%B3%C5%82+Nadzwyczajnego+Walnego+Zgromadzenia+Akcjonariuszy+Sp%C3%B3%C5%82ki+FON+SE+z+dnia+04.05.2022+r.+Protocol+of+the+Extraordinary+General+Meeting+of+Shareholders+of+FON+SE+of+4%2F05%2F2022.">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">04-05-2022 18:08:08 | Current | ESPI | 25/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395915&amp;title=Projekt+i+rozbudowa+drogi+krajowej+nr+79+na+odcinku+Garbatka+-+Wilczowola+od+km+93%2B030+do+km+100%2B711+-+wyb%C3%B3r+oferty+Budimex+S.A.">
        	        	BUDIMEX SPÓŁKA AKCYJNA (PLBUDMX00013)
        </a>
    </strong>
        <span class="loss margin-left-30 pull-right"><small>Change</small> 0,48% <i class="icon-down"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>207,00</span>
        <p>
                				Projekt i rozbudowa drogi krajowej nr 79 na odcinku Garbatka - Wilczowola od km 93+030 do km 100+711 - wybór oferty Budimex S.A.
            </p>
        <a href="espi-ebi-report?geru_id=395915&amp;title=Projekt+i+rozbudowa+drogi+krajowej+nr+79+na+odcinku+Garbatka+-+Wilczowola+od+km+93%2B030+do+km+100%2B711+-+wyb%C3%B3r+oferty+Budimex+S.A.">more &gt;</a>
</li>
<li style="padding: 15px 0;">
	    <span class="date">04-05-2022 17:34:02 | Current | ESPI | 4/2022</span>
    <strong class="name">
        <a href="espi-ebi-report?geru_id=395911&amp;title=Przyj%C4%99cie+przez+Rad%C4%99+Nadzorcz%C4%85+Sp%C3%B3%C5%82ki+zmian+do+Programu+Motywacyjnego+IV+na+lata+2021+-+2023">
        	        	IMS SPÓŁKA AKCYJNA (PLINTMS00019)
        </a>
    </strong>
        <span class="profit margin-left-30 pull-right"><small>Change</small> 0,39% <i class="icon-up"></i></span>
    <span class="summary margin-left-30 pull-right"><small>FX rate</small>2,59</span>
        <p>
                				Przyjęcie przez Radę Nadzorczą Spółki zmian do Programu Motywacyjnego IV na lata 2021 - 2023
            </p>
        <a href="espi-ebi-report?geru_id=395911&amp;title=Przyj%C4%99cie+przez+Rad%C4%99+Nadzorcz%C4%85+Sp%C3%B3%C5%82ki+zmian+do+Programu+Motywacyjnego+IV+na+lata+2021+-+2023">more &gt;</a>
</li>
"""

html_reference = """\
<html>\
<table style="border-collapse:collapse; width: 100%";>\
<thead>\
<th style="font-size: 12px; font-family: system-ui; text-align: center; border: none; padding: 5px; font-weight: bold; color: #777; background-color: #f7f7f9; ">ID</th>\
<th style="font-size: 12px; font-family: system-ui; text-align: center; border: none; padding: 5px; font-weight: bold; color: #777; background-color: #f7f7f9; ">Date</th>\
<th style="font-size: 12px; font-family: system-ui; text-align: center; border: none; padding: 5px; font-weight: bold; color: #777; background-color: #f7f7f9; ">Type</th>\
<th style="font-size: 12px; font-family: system-ui; text-align: center; border: none; padding: 5px; font-weight: bold; color: #777; background-color: #f7f7f9; ">Category</th>\
<th style="font-size: 12px; font-family: system-ui; text-align: center; border: none; padding: 5px; font-weight: bold; color: #777; background-color: #f7f7f9; ">Number</th>\
<th style="font-size: 12px; font-family: system-ui; text-align: center; border: none; padding: 5px; font-weight: bold; color: #777; background-color: #f7f7f9; ">Company</th>\
<th style="font-size: 12px; font-family: system-ui; text-align: center; border: none; padding: 5px; font-weight: bold; color: #777; background-color: #f7f7f9; ">Title</th>\
</thead>\
<tbody>\
<tr style="border-top: solid 1px #ccc;">\
<td style="font-size: 12px; font-family: system-ui; text-align: center; border: none; padding: 5px;">395960</td>\
<td style="font-size: 12px; font-family: system-ui; text-align: center; border: none; padding: 5px;">05-05-2022 12:43:03</td>\
<td style="font-size: 12px; font-family: system-ui; text-align: center; border: none; padding: 5px;">Current</td>\
<td style="font-size: 12px; font-family: system-ui; text-align: center; border: none; padding: 5px;">ESPI</td>\
<td style="font-size: 12px; font-family: system-ui; text-align: center; border: none; padding: 5px;">14/2022</td>\
<td style="font-size: 12px; font-family: system-ui; text-align: center; border: none; padding: 5px;"><a href="https://www.gpw.pl/espi-ebi-report?geru_id=395960&title=Podpisanie+porozumienia+w+sprawie+wsp%C3%B3lnej+realizacji+projektu.">ZAKŁAD BUDOWY MASZYN ZREMB-CHOJNICE SPÓŁKA AKCYJNA (PLZBMZC00019)</a></td>\
<td style="font-size: 12px; font-family: system-ui; text-align: center; border: none; padding: 5px;">Podpisanie porozumienia w sprawie wspólnej realizacji projektu.</td>\
</tr>\
</tbody>\
</table>\
</html>\
"""