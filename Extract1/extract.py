import requests
import re
from bs4 import BeautifulSoup
import urllib.request

html = requests.get('http://www.knockhardy.org.uk/sci.htm')
soup = BeautifulSoup(html.content,'lxml')

links = []
for link in soup.find_all('a', attrs = {'href': re.compile('.pdf$')}):
    links.append(link.get('href'))

for i in range(10):
    urllib.request.urlretrieve('http://www.knockhardy.org.uk/'+links[i], '/home/roshan/Desktop/files/'+links[i].split('/')[-1])
    
