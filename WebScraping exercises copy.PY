import requests 
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148#.YbDZzC-l1N0")
soup = BeautifulSoup(page.content, 'html.parser') #parser and download web
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]

'''short_desc = tonight.find(class_='short-desc').get_text()
temp = tonight.find(class_='temp').get_text()
img = tonight.find("img")
desc = img['title']
#print a single day
#celsius = (int(temp) - 32) * 5/9 '''

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(short_descs)
print(temps)
print(descs)

import pandas as pd
weather = pd.DataFrame({
         "short_desc": short_descs,
         "temp": temps,
         "desc": descs
    })
weather

