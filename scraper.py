import requests
import datetime
from bs4 import BeautifulSoup

url = "https://pixelford.com/blog/"
response = requests.get( url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'} )

html = response.content
soup = BeautifulSoup(html, 'html.parser')
blogs = soup.find_all('article', class_="type-post")

for blog in blogs:
    title = blog.find('a', class_="entry-title-link").get_text()

    blog_datetime_str = blog.find('time', class_="entry-time").get('datetime')
    blog_datetime = datetime.datetime.fromisoformat(blog_datetime_str)
    pretty_date = blog_datetime.strftime("%d %b %Y")
    
    print(f"{pretty_date} - {title}")