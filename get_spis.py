# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
def get_html(url):
    try:
        result=requests.get(url)
        result.encoding = 'utf-8'
        result.raise_for_status()
        return result.text
    except(requests.RequestException,ValueError):
        return False

def find_all_name(html):
    soup=BeautifulSoup(html,'html.parser')
    #tags=soup.find('h1',itemprop='name')[0].text.strip()
    Name_book_tag = soup.select('h1.bc__book-title')[0].text.strip()
    #Name_athor_tag = soup.select('a.bc-author__link')
    Name_athor_tag = soup.find_all('a',class_='bc-author__link')
    mean_number = soup.find('span', {'itemprop': 'ratingValue'}).get_text()
    #recendent_number = soup.find_all('span', {'class': 'lenta-card__mymark'})
    #mean_number = soup.find_all('span', {'itemprop': 'ratingValue'})[0]
    #name_recendent = soup.find_all('a.header-card-user__name')[0].text.strip()
    name_recendent = soup.find_all('a',class_='header-card-user__name')

    recendent_number = soup.find_all('span',class_='lenta-card__mymark')
    athor_name=[]
    athor_recendent=[]
    athor_recendent_nummber=[]
    for Na in Name_athor_tag:
        tetle=Na.text
        athor_name.append(tetle)

    for Na in name_recendent:
        tetle2=Na.text
        athor_recendent.append(tetle2)

        #print((tetle))
    for Na in recendent_number:
        tetle3=Na.text
        athor_recendent_nummber.append(tetle3)

        return Name_book_tag, athor_name,mean_number,athor_recendent,athor_recendent_nummber




if __name__ =='__main__':
    #html=get_html('https://www.livelib.ru/book/1002455336-kod-da-vinchi-den-braun')
    html=get_html('https://www.livelib.ru/book/1002455336-kod-da-vinchi-den-braun')
    if html:
        with open('test.html','w',encoding='utf8') as f:
            f.write(html)
        name_book,athor_name,mean_number,athor_recendent,athor_recendent_nummber =find_all_name(html)
        print(f'{name_book} , {athor_name}, {mean_number}')
