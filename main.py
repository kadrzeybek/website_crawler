import requests
from bs4 import BeautifulSoup


founded = []
urls = "https://atilsamancioglu.com"

def request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def crawler(url):
    links = request(url)
    for link in links.find_all('a'):
        found = link.get('href')
        if found:
            if urls in found and found not in founded:
                founded.append(found)
                print(found)
                crawler(found)


crawler(urls)


