from bs4 import BeautifulSoup
import requests

def get_rottentomatoes():
    r = requests.get('http://editorial.rottentomatoes.com/news/')
    soup = BeautifulSoup(r.text, 'html.parser')
    block = soup.find('div',{'class':'panel-body'})
    news_rows = block.find_all('div',{'class':'row'})
    news_rows = news_rows[0:3]
    news_info = []
    for news in news_rows:
        article = news.find_all('div',{'class':'col-sm-8 newsItem col-full-xs'})
        for a in article:
            caption = a.find('p',{'class':'noSpacing title'}).get_text().strip()
            date = a.find('p',{'class':'noSpacing publication-date'}).get_text()
            link =a.find('a').get('href')
            news_info.append([caption, date, link])
    text = ''
    for i in range(len(news_info)):
        text = text + '{}\n{}\n{}\n\n'.format(news_info[i][0], news_info[i][1], news_info[i][2])
    return text.strip()

get_rottentomatoes()