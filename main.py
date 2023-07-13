import requests
from bs4 import BeautifulSoup
import time

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def test_proxy(proxy):
    url = 'http://www.google.com'  
    proxies = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
    }

    start_time = time.time()

    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        if response.status_code == 200:
            elapsed_time = time.time() - start_time
            print(f"{GREEN}Proxy: {proxy}\tResponse Time: {elapsed_time:.2f} seconds{RESET}")
        else:
            print(f"{RED}Proxy: {proxy}\tResponse: {response.status_code}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}Proxy: {proxy}\tError: {e}{RESET}")

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

urls = [
    'https://www.sslproxies.org',
    'https://www.proxy-list.download',
    'https://free-proxy-list.net'
    
]

for url in urls:
    proxies = scrape_proxies(url)
    
    for proxy in proxies:
        test_proxy(proxy)
