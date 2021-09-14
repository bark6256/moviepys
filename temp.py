import requests
from bs4 import BeautifulSoup

def gettemp():
    url = '''
        https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A8%EB%8F%84
    '''

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    targer = soup.select_one(".todaytemp")
    temp = targer.text
    return temp