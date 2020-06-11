import json

import requests


class Country:
    def __init__(self, input):
        self.input = input
        self.cov()
        self.flag_url = f"https://www.countryflags.io/{self.CountryCode.lower()}/flat/64.png"

    def cov(self):
        url = "https://api.covid19api.com/summary"
        country = self.input.lower().capitalize().strip()
        code = self.input.upper()
        response = requests.get(url)
        response = json.loads(response.text)
        countryList = response["Countries"]
        for data in countryList:
            if data["Country"] == country or data["CountryCode"] == code:
                # print(data)
                self.TotalConfirmed = data['TotalConfirmed']
                self.TotalDeaths = data['TotalDeaths']
                self.TotalRecovered = data['TotalRecovered']
                self.NewConfirmed = data['NewConfirmed']
                self.NewDeaths = data['NewDeaths']
                self.NewRecovered = data['NewRecovered']
                self.CountryCode = data['CountryCode']
                self.CountryName = data['Country']

    @staticmethod
    def CountryList():
        url = "https://api.covid19api.com/summary"
        response = requests.get(url)
        response = json.loads(response.text)
        countryList = response["Countries"]
        liste = []
        for data in countryList:
            Country = data["Country"]
            liste.append(Country)
        return liste