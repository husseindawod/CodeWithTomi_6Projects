import requests
from bs4 import BeautifulSoup as bs

github_user = input("Input GitHub User: ")
url = 'https://github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_img = soup.find('img', {'class': 'avatar-user'})['src']
print(profile_img)