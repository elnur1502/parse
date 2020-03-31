import vk_api
import random
import requests
import Gamebot.Steps as steps
import Gamebot.Market as Market
from bs4 import BeautifulSoup
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

token = "e615070ecbd0a9642205948dbe49728785555494f701852aabe742313bc7eee4dbdd7447ffeca14003479" #token


vk = vk_api.VkApi(token=token)


botlongpoll = VkLongPoll(vk)

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


def main():

    url = 'https://www.microsoft.com/ru-ru/search/shop/games?q=gta'
    all_links = get_all_links(get_html(url))
    for i in all_links:
       print(i)
        

if __name__ == '__main__':
    main()
