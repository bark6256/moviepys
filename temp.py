import requests
from bs4 import BeautifulSoup

class Temp:
    def __init__(self, temp):
        self.temp = temp

def gettemp():
    url = '''
        https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A8%EB%8F%84
    '''

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    targer = soup.select_one(".todaytemp")
    temp = Temp(targer.text).__dict__
    return temp