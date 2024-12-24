import requests
from bs4 import BeautifulSoup as bs

github_user = input("Input GitHub User: ")
url = 'https://github.com/' + github_user