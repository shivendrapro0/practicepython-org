# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
#
# from bs4 import BeautifulSoup
#
# soap = BeautifulSoup(html_doc,'html.parser')
#
# # print(soap.prettify())
# print(soap.title)
# print(soap.title.name)
# print(soap.p['class'])
#
# for i in soap.find_all('a'):
#     print(i.get('href'))


# import requests
# from bs4 import BeautifulSoup
#
# r = requests.get('https://www.nytimes.com/')
# soap = BeautifulSoup(r.text,'html.parser')
# # print(soap.prettify())
#
# for story_heading in soap.find_all(class_='story-heading'):
#     if story_heading.a:
#         print(story_heading.a.text)
#     # if 'New York' in i.get('content'):
#     #     print(i.get('content'))

import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.practicepython.org')
soap = BeautifulSoup(r.text,'html.parser')
# print(soap.prettify())

for story_heading in soap.find_all('li'):
    if story_heading.a:
        print(story_heading.a.text)
        #print(story_heading.a.text, ' ' , story_heading.a['href'])