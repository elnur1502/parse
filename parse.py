import requests

from bs4 import BeautifulSoup

search_link = "https://www.microsoft.com/ru-ru/search?q="

def get_html(url):
    response = requests.get(url)
    return response.text


def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find('div', class_='c-group f-wrap-items context-list-page').find_all('div', class_='m-channel-placement-item')
    links = []
    for div in divs:
        a = div.find('a').get('href')
        link = 'https://microsoft.com' + a
        links.append(link)
    return links

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        name = soup.find('h1', id='DynamicHeading_productTitle').text.strip()
    except:
        name = ''
    try:
        price = soup.find('div', id='ProductPrice_productPrice_PriceContainer').text.strip()
    except:
        price = ''
    data = {'name': name, 'price': price}
    return data


def main():

    url = 'https://www.microsoft.com/ru-ru/search/shop/games?q=gta'
    all_links = get_all_links(get_html(url))
    for i in all_links:
       print(i)
        

if __name__ == '__main__':
    main()
