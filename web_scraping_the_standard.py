from bs4 import BeautifulSoup
import requests

def get_thestandard_news():
    #REQUEST FROM THE STANDARD WEBSITE
    r = requests.get('https://thestandard.co/homepage/')
    soup = BeautifulSoup(r.text, 'html.parser')
    
    #SCRAPING TRENDING NEWS : LARGEBOX AND SMALLBOX
    news = soup.find('div',{'class':'col-sm-9 fix-sticky'})
    largebox_news = news.find('div',{'class':'newsbox-large'})
    smallbox_news = news.find_all('div',{'class':'newsbox-small'})
    smallbox_news = smallbox_news[1].find_all('div',{'class':'col-sm-6 col-md-4'}) 
    
    #DISPLAY INFORMATION
    category = []
    heading = []
    link = []
    
    #LARGEBOX NEWS
    largecat = largebox_news.find('div',{'class':'caption'}).find('div',{'class':'cat'}).get_text().strip()
    category.append('-' if largecat == '' else largecat)
    heading.append(largebox_news
                    .find('div',{'class':'caption'})
                    .find('h2',{'class':'news-title'})
                    .get_text().strip())
    link.append(largebox_news
                    .find('div',{'class':'caption'})
                    .find('h2',{'class':'news-title'})
                    .find('a').get('href'))
    
    #SMALLBOX NEWS
    for news in smallbox_news:
        smallcat = news.find('div',{'class':'caption'}).find('div',{'class':'cat'}).get_text().strip()
        category.append('-' if smallcat == '' else smallcat)
        heading.append(news.find('div',{'class':'caption'}).find('h2',{'class':'news-title'}).get_text().strip())
        link.append(news.find('div',{'class':'caption'}).find('h2',{'class':'news-title'}).find('a').get('href'))

    #DISPLAY   
    text = ''
    for i in range(0,7):
        text = text + '{} \ncategory: {} \n{} \n\n'.format(heading[i], category[i], link[i])
    
    return text
