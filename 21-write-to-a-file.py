import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.nytimes.com/')
soap = BeautifulSoup(r.text,'html.parser')
text = []
headline_text_file = open('tmp_dir/headline_nyc.txt','w')
for story_heading in soap.find_all(class_='story-heading'):
    if story_heading.a:
        headline_text_file.write(story_heading.a.text)
