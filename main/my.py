import requests
from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from requests.compat import quote_plus
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
import time
import sys

# Create your views here.

BASE_MENTORS_LIST_URL = 'https://oc.kg/#/catalog/'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'
HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    }

CHROME_DRIVER_PATH = "/Users/elemanz/Downloads/chromedriver"

def main(request):
    return render(request, 'index.html')


def new_search(request):
    search = request.POST.get('search')
    # final_url = BASE_MENTORS_LIST_URL.format(quote_plus(search))
    print(BASE_MENTORS_LIST_URL)
    url = BASE_MENTORS_LIST_URL

    chrome_option = Options()
    chrome_option.add_argument("--headless")

    webdriver = webdriver.Chrome(
        executable_path=CHROME_DRIVER_PATH,
        options=chrome_option,
    )

    # default search query
    search_query = "life"

    with webdriver as driver:
        wait = WebDriverWait(driver, 10)

        # retrieve data
        driver.get(url)

        # find search box
        search = driver.f


    # response = requests.get(url)
    # data = response.content
    # soup = BeautifulSoup(data, 'html.parser')
    # post_listings = soup.find_all('div', id='catalog')
    # print(post_listings)
    #
    # final_postings = []

    # for post in post_listings:
    #     post_title = post.find(class_='result-title').text
    #     post_url = post.find('a').get('href')
    #
    #     if post.find(class_='result_price'):
    #         post_price = post.find(class_='result-price').text
    #     else:
    #         post_price = 'N/A'
    #     if post.find(class_='result-image').get('data-ids'):
    #         post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
    #         post_image_url = BASE_IMAGE_URL.format(post_image_id)
    #         print(post_image_url)
    #     else:
    #         post_image_url = 'https://cutt.ly/sz8uqnZ'
    #     final_postings.append((post_title, post_url, post_price, post_image_url))

    # for post in post_listings:
    #     post_title = post.find(class_='result-title').text
    #     post_url = post.find('a').get('href')
    #
    #     if post.find(class_='result_price'):
    #         post_price = post.find(class_='result-price').text
    #     else:
    #         post_price = 'N/A'
    #     if post.find(class_='result-image').get('data-ids'):
    #         post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
    #         post_image_url = BASE_IMAGE_URL.format(post_image_id)
    #         print(post_image_url)
    #     else:
    #         post_image_url = 'https://cutt.ly/sz8uqnZ'
    #     final_postings.append((post_title, post_url, post_price, post_image_url))

    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings,
    }
    return render(request, 'search/new-search.html', stuff_for_frontend)
