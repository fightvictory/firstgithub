import requests
from bs4 import BeautifulSoup
import time

t1 = time.time()
r = requests.get('https://car.autohome.com.cn/price/list-0-3-0-0-0-0-0-0-0-0-0-0-0-0-0-1.html')

c = r.text

soup = BeautifulSoup(c, 'html.parser')
# content = soup.find_all('div', {'class': 'list-cont'})
page_div = soup.find('div', {'class': 'page'})
page = page_div.find_all('a')[-2].text
cars = []
for i in range(1, int(page)+1):
    url = 'https://car.autohome.com.cn/price/list-0-3-0-0-0-0-0-0-0-0-0-0-0-0-0-' + str(i) +'.html'
    p_r = requests.get(url)
    p_c = p_r.text
    p_soup = BeautifulSoup(p_c, 'html.parser')
    p_content = p_soup.find_all('div', {'class': 'list-cont'})

    for car in p_content:
        carDic = {}
        carDic['picUrl'] = car.find('div', {'class': 'list-cont-img'}).find('img')['src']
        carDic['name'] = car.find('div', {'class': 'list-cont-main'}).find('a').text
        try:
            carDic['score'] = car.find('span', {'class': 'score-number'}).text
        except Exception as e:
            carDic['score'] = ''
        cars.append(carDic)

# pip3 install pandas
'''from pandas import DataFrame
df = DataFrame(cars)
df.to_csv('cars.csv')
'''
t2 = time.time()
print(t2-t1)
