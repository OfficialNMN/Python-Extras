import requests
from bs4 import BeautifulSoup as bs
# import pandas as pd

url='https://keithgalli.github.io/web-scraping/webpage.html'
r=requests.get(url)
webpage=bs(r.content,'html.parser')
#print(webpage.prettify())

#Getting Social Links
ulist=webpage.find('ul',attrs={'class':'socials'})
links=ulist.find_all('a')
link=[l['href'] for l in links]
print(link)

#Getting Table
table=webpage.select('table.hockey-stats')[0]
columns=table.find('thead').find_all('th')
cnames=[c.string for c in columns]

table_rows=table.find('tbody').find_all('tr')
l=[]
for tr in table_rows:
	td=tr.find_all('td')
	row=[str(tr.get_text()).strip() for tr in td]
	l.append(row)

df=pd.DataFrame(l,columns=cnames)
print(df.head())

#Dowlnoad an image
iurl = "https://keithgalli.github.io/web-scraping/"
r = requests.get(url+"webpage.html")
webpage = bs(r.content)

images = webpage.select("div.row div.column img")
image_url = images[0]['src']
full_url = iurl + image_url

img_data = requests.get(full_url).content
with open('lake_como.jpg', 'wb') as handler:
    handler.write(img_data)