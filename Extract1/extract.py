# Import necessary libraries
import requests
import re
from bs4 import BeautifulSoup
import urllib.request

#Requesting response from the webpage
html = requests.get('http://www.knockhardy.org.uk/sci.htm')

#Converting the webpage into beautiful soup object
soup = BeautifulSoup(html.content,'lxml')

#Creating an empty list to store links

links = []

#Finding and adding links in the list
for link in soup.find_all('a', attrs = {'href': re.compile('.pdf$')}):
    links.append(link.get('href'))
   
#Since there are many links of the pdf files, I will loop over only first 10 links

for i in range(10):
    urllib.request.urlretrieve('http://www.knockhardy.org.uk/'+links[i], '/home/roshan/Desktop/files/'+links[i].split('/')[-1])
    
