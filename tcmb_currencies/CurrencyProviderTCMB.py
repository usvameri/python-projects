import requests

class CurrencyProviderTCMB:
    def __init__(self):
        self.url = "https://www.tcmb.gov.tr/kurlar/today.xml"
        self.data = self.get_data()
        self.date = self.get_currency_data()

    
    def get_data(self):
        import requests
        response = requests.get(self.url)
        return response.text


    def get_currency_data(self):
        import xml.etree.ElementTree as ET
        root = ET.fromstring(self.data)
        currency_data = []
        for child in root:
            currency_data.append(
                {child.attrib['CurrencyCode']: [{grand_child.tag: grand_child.text} for grand_child in child]}
            )
                # currency_data[grand_child.tag] = grand_child.text
        return currency_data

   