# intall all requirements


import requests
from bs4 import BeautifulSoup
from csv import writer
url= "https://opentender.eu/"
page =requests.get(url)
htmlcontent = page.content
# creating the soup
soup = BeautifulSoup(htmlcontent, 'html.parser')

lists= soup.find_all('li', class_="portal-link")

with open('tanders.csv','w',encoding='utf8',newline='') as f:
    thewriter = writer(f)
    header = ['COUNTRY','NO. OF TANDERS']
    thewriter.writerow(header)
    for list in lists:
         country = list.find('a').text
         no_of_tanders = list.find('div').text
         info = [country, no_of_tanders]
         thewriter.writerow(info)

    




