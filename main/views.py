import requests
from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from requests.compat import quote_plus

# Create your views here.

BASE_MENTORS_LIST_URL = 'https://oc.kg/#/catalog/'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


def main(request):
    return render(request, 'index.html')


def new_search(request):
    search = request.POST.get('search')
    # final_url = BASE_MENTORS_LIST_URL.format(quote_plus(search))
    url = BASE_MENTORS_LIST_URL
    print(url)

    response = requests.get(url)
    data = response.content
    soup = BeautifulSoup(data, 'html.parser')
    post_listings = soup.find_all('div', id='catalog')
    print(post_listings)

    final_postings = []

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


def about(request):
    return render(request, 'about.html')