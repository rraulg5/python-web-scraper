import requests
from bs4 import BeautifulSoup

url = "https://pixelford.com/blog/"
response = requests.get( url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'} )

html = response.content
soup = BeautifulSoup(html, 'html.parser')
a_tags = soup.find_all('a', class_="entry-title-link")

# for a_tag in a_tags:
#     print(a_tag.get_text())

a_tags_list = list( map(lambda a_tag: a_tag.get_text(), a_tags) )
print(a_tags_list)