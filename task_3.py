import requests
import time
from datetime import datetime
from pprint import pprint

unix_datatime_now = time.mktime(datetime.now().timetuple())
todate = unix_datatime_now
fromdate = unix_datatime_now - 86400*2

url = "https://api.stackexchange.com/2.3/questions"

params = {
    'page': None,
    'pagesize': None,
    'fromdate': int(fromdate),
    'todate': int(todate),
    'order': 'desc',
    'sort': 'activity',
    'site': 'stackoverflow',
    'min': None,
    'max': None,
    'tagged': 'Python'
    }

res = requests.get(url, params=params).json()

pprint(res)

for tag in res['items']:
    print(f"Вопрос - {tag['title']}\nТег - {tag['tags']}\n")
