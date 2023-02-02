import requests
from bs4 import BeautifulSoup
import lxml
from fake_useragent import UserAgent
import datetime
import time
import csv
import json
import random

def discriptions():
    date = datetime.datetime.now()
    with open(f"{date.strftime('%m, %w, %y')} price_iphone.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['model', 'link', 'cost'])


def iphone_page_count(url):
    user = UserAgent()
    headers = {
        'user-aget': user.random
        }
    title_page = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(title_page, 'lxml')
    page = soup.find("ul", class_="page-numbers")
    page = [i for i in page if i != "\n"]
    return int(page[-2].text)

def iphone_param(url):
    user = UserAgent()
    headers = {
        'user-aget': user.random
    }
    title_page = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(title_page, 'lxml')
    src = soup.find("div", class_="columns-4").find_all("div", class_="woocommerce-card__header")


def iphone_price(count):
    for number_page in range(count):
        url = f"https://www.ioutletstore.pt/categoria-produto/iphones/page/{number_page}"
        user = UserAgent()
        headers = {
            'user-aget': user.random
        }
        title_page = requests.get(url=url, headers=headers).text
        soup = BeautifulSoup(title_page, 'lxml')
        src = soup.find("div", class_="columns-4").find_all("div", class_="woocommerce-card__header")
        list_ipone_param = []
        iphone_href = []
        cost = []
        iphone_param_model = []
        iphone_json = []
        for card in src:
            list_ipone_param.append(card.find('a'))
            cost.append(card.find('bdi').text)
        for iphone_card_param in list_ipone_param:
            iphone_href.append(iphone_card_param.get('href'))
            iphone_param_model.append(iphone_card_param.text)
        for index in range(0, len(iphone_href)-1):
            time.sleep(random.randint(2, 5))
            date = datetime.datetime.now()
            iphone_json.append({
                'model' : iphone_param_model[index],
                'iphone_link': iphone_href[index],
                'cost' : cost[index],
            })
            with open(f"{date.strftime('%m, %w, %y')} price_iphone.csv", 'a') as file:
                writer = csv.writer(file)
                writer.writerow([iphone_param_model[index],iphone_href[index],cost[index]])

        with open("price_iphone.json", "a", encoding='utf-8',) as file:
                json.dump(iphone_json, file, indent=4, ensure_ascii=False)



def main():
    discriptions()
    url = 'https://www.ioutletstore.pt/categoria-produto/iphones/'
    count = iphone_page_count(url)
    iphone_price(count)



if __name__=="__main__":
    main()