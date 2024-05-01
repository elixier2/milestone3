import requests
from bs4 import BeautifulSoup
import pandas as pd

mobile_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0'}

response = requests.get("https://www.seatemperature.org/north-america/united-states/", headers=mobile_headers)

soup = BeautifulSoup(response.text, 'html.parser')
pretty_html = soup.prettify()
data = soup.find('ul', id="location-list")
data =data.find_all('li')
list_of_links = []
for row in data:
  list_of_links.append(row.find('a',href=True)['href'])
print(list_of_links)
list_of_links2 = list_of_links[:2]
parent_url = "https://www.seatemperature.org"
final_data = []
for link in list_of_links:
  test_url = parent_url + link
  response = requests.get(test_url, headers=mobile_headers)
  soup = BeautifulSoup(response.text, 'html.parser')
  pretty_html = soup.prettify()
  #data is present in table rows

  data = soup.find('ul',id='right-stats')
  if data is not None:
    data = data.find_all('li')

    list_F = []
    list_C = []
    for row in data:
      value = row.text
      value = value.split(":")
      value = value[1].split("/")
      list_F.append(value[1])
      list_C.append(value[0])
    maxf,avgf,minf = list_F
    maxC,avgC,minC = list_C
    city = link.split("/")
    city = city[-1]
    city = city.split(".")
    city = city[0]
    dict1 = dict()
    dict1["city"] = city
    dict1["max water temperature F "] = maxf
    dict1["average water temperature F"] = avgf
    dict1["min water temperature F"] = minf
    dict1["max water temperature C "] = maxC
    dict1["average water temperature C"] = avgC
    dict1["min water temperature C"] = minC
    final_data.append(dict1)
    print(f"city:{city} max:{maxf} avg:{avgf} min:{minf}")
len(final_data)
df = pd.DataFrame(final_data)
df.to_excel('city_water_body_temp.xlsx',index=False)





