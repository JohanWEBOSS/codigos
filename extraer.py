from  bs4 import BeautifulSoup
import requests

website = 'https://www.homedepot.com.mx/pinturas/acabados-para-superficies?storeId=10351'
results = requests.get(website)
content = results.text

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())
