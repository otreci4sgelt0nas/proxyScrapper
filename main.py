import requests
from bs4 import BeautifulSoup

def scrape_proxies(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    proxy_list = []
    
    table = soup.find('table')
    rows = table.find_all('tr')
    
    for row in rows[1:]:
        columns = row.find_all('td')
        ip = columns[0].text
        port = columns[1].text
        proxy = f"{ip}:{port}"
        proxy_list.append(proxy)
    
    return proxy_list

# Example usage:
url = 'import requests
from bs4 import BeautifulSoup

def scrape_proxies(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    proxy_list = []
    
    table = soup.find('table')
    rows = table.find_all('tr')
    
    for row in rows[1:]:
        columns = row.find_all('td')
        ip = columns[0].text
        port = columns[1].text
        proxy = f"{ip}:{port}"
        proxy_list.append(proxy)
    
    return proxy_list
  
# feel free to replace with own proxy sources, for this instance I decided to use sslproxies.org
url = 'https://www.sslproxies.org'
proxies = scrape_proxies(url)

for proxy in proxies:
    print(proxy)
'
proxies = scrape_proxies(url)

for proxy in proxies:
    print(proxy)
