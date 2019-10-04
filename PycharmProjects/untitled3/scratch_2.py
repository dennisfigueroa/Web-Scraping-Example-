import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://champion.gg/statistics/#?sortBy=general.winPercent&order=descend&roleSort=ADC'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
example = soup.find_all('script')
print(example)
if '<script src="https://solomid-net.videoplayerhub.com/videoloader.js"></script>' in example:
   print('Its there')
else:
   print('Nope')

