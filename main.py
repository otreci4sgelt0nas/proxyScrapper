import requests
from bs4 import BeautifulSoup
import time

def test_proxy(proxy):
    url = 'http://google.com'
    proxies = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
    }
    
    start_time = time.time()
    
    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        if response.status_code == 200:
            elapsed_time = time.time() - start_time
            print(f"Proxy: {proxy}\tResponse Time: {elapsed_time:.2f} seconds")
        else:
            print(f"Proxy: {proxy}\tResponse: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Proxy: {proxy}\tError: {e}")

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
url = 'https://www.sslproxies.org'
proxies = scrape_proxies(url)

for proxy in proxies:
    test_proxy(proxy)
