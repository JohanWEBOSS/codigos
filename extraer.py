from  bs4 import BeautifulSoup
import requests

website = 'https://www.soriana.com/?msclkid=211da0ebcf8618c8af0ac50dc8405dc8&utm_source=bing&utm_medium=cpc&utm_campaign=bing_performance_web_search_conversion_nacional_brand&utm_term=www+soriana+com&utm_content=Brand_General_.com'
results = requests.get(website)
content = results.text

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())
