from bs4 import BeautifulSoup
import requests
url = "https://www.reddit.com/r/Python"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all('h3')
for post in posts:
    print(post.text.strip())
