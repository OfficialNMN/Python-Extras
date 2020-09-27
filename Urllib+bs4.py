import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count=int(input('Enter Count: '))
position=int(input('Enter position: '))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

names=[]
for _ in range(count):
	# Retrieve all of the anchor tags
    tags = soup('a')
    html = urllib.request.urlopen(tags[position-1].get('href', None), context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    names.append(tags[position-1].get_text())
print(names[-1])

