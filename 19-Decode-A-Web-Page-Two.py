from bs4 import BeautifulSoup
import requests

# It works but not complete Artical is there
# html_url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
html_url = 'https://en.wikipedia.org/wiki/Salman_Khan'

def download_html(url):
    r = requests.get(url)
    return r

def prase_html(html):
    soap = BeautifulSoup(html.text,'html.parser')

    for story_heading in soap.find_all(['p']):
        print(story_heading.text)

prase_html(download_html(html_url))