from bs4 import BeautifulSoup
import requests

#TODO Format text output in file
#Create try expect block to prevent script from breaking if missing info

url = "https://www.khon2.com/"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="lxml")
title_list = soup.find_all("h3", class_="article-list__article-title")

khon2_news_file = open("khon2_titles.txt", 'w')
for t in title_list:
    khon2_news_file.write(t.a.text)
khon2_news_file.close()