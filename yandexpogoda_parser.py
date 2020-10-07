#! python3

import requests
import sys
import bs4
import lxml

weatherday = range(0, 4)
if len(sys.argv) < 3:
    print('Usage: python yandexpogoda_parser.py <city> <today/tomorrow>.')
    sys.exit()
if sys.argv[2] == 'today':
    weatherday = range(0, 4)
if sys.argv[2] == 'tomorrow':
    weatherday = range(4, 8)
res = requests.get('https://yandex.ru/pogoda/' + str(sys.argv[1]) + '/details')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
print('Weather in ' + str(sys.argv[1])+ ' ' + str(sys.argv[2]))
print('', end='-'*40+'\n')
daypart = soup.select('.weather-table__daypart')
temperature = soup.select('.weather-table__temp')
for i in weatherday:
    print('Температура ' + daypart[i].getText() + ' : ' + temperature[i].getText())
print('', end='-'*40+'\n')
air_pressure = soup.select('.weather-table__body-cell_type_air-pressure')
for i in weatherday:
    print('Давление воздуха ' + daypart[i].getText() + ' : '+air_pressure[i].getText())
print('', end='-'*40+'\n')
humidity = soup.select('.weather-table__body-cell_type_humidity')
for i in weatherday:
    print('Влажность воздуха ' + daypart[i].getText() + ' : '+humidity[i].getText())
print('', end='-'*40+'\n')
wind_speed = soup.select('.weather-table__wind')
for i in weatherday:
    print('Скорость ветра, м/c ' + daypart[i].getText() + ' : '+wind_speed[i].getText())
print('', end='-'*40+'\n')
