import requests
import bs4
url= "https://www.amazon.com/"
uclient= requests.get(url)
page_html=uclient
uclient.close()


page=bs4.BeautifulSoup(page_html.text ,'html.parser')

print(page)