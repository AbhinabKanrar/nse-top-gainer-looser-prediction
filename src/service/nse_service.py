import requests


class NseService:

    def get_gainers(self):
        return requests.get('https://www1.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json').json()

    def get_loosers(self):
        return requests.get('https://www1.nseindia.com/live_market/dynaContent/live_analysis/losers/niftyLosers1.json').json()
