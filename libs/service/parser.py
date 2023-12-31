import requests
from requests import Response
from icecream import ic
from libs.helpers.writer import Writer
from libs.utils.log import Logs
from fake_useragent import FakeUserAgent

class Parser:
    def __init__(self) -> None:
        self.__writer = Writer()
        self.__log = Logs()
        self.__user_agent = FakeUserAgent()

        self.__api_key = 'UZ8GOpIh0q5umvfA6Xkm6d3t3NUBlUSn'
        self.__proxies = {
            "http": "154.6.96.156:3128"
        }
        self.__headers = {
            "accept": "application/json",
            "User-Agent": self.__user_agent.random
        }
        

    def fetch_data(self, location: str) -> Response:
        response = requests.get(url=f"https://api.tomorrow.io/v4/weather/forecast?location={location}&apikey={self.__api_key}", proxies=self.__proxies, headers=self.__headers)
        
        responseJson = response.json()
        if responseJson.get('code') == 400001:
            self.__log.err(response=responseJson, requests=location)
            return 404
        
        return response


        
