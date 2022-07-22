import requests

class CurrencyProviderTCMB:
    def __init__(self):
        self.url = "https://www.tcmb.gov.tr/kurlar/today.xml"
        self.data = self.get_data()
        self.parsed_data = self.get_currency_data()

    
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


    def get_specific_currency_details(self, currency_code):
        for currency_detail in self.parsed_data:
            if currency_code in currency_detail:
                return currency_detail
    

    def get_specifict_currency_code_and_buy_sell_rates(self, currency_code):
        for currency_elements in self.parsed_data:
            if currency_code in currency_elements:
                for key, value in currency_elements.items():
                    for detail_elements in value:
                        for key, value in detail_elements.items():
                            if key.startswith("ForexBuying"):
                                return [currency_code, value] 

