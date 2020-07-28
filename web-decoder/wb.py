from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, features="lxml")
list1 = soup.find_all("span", class_="balancedHeadline")
soup.select("")