import requests
from bs4 import BeautifulSoup
import random
import concurrent.futures
import csv
import requests



#get the list of free proxies
def getProxies():
    r = requests.get('https://free-proxy-list.net/')
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('tbody')
    proxies = []
    for row in table:
        if row.find_all('td')[4].text =='elite proxy':
            proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
            proxies.append(proxy)
        else:
            pass
    return proxies


# def extract(proxy):
#     #this was for when we took a list into the function, without conc futures.
#     #proxy = random.choice(proxylist)
#     headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
#     try:
#         #change the url to https://httpbin.org/ip that doesnt block anything
#         r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=1)
#         print(r.json(), r.status_code)
#     except requests.ConnectionError as err:
#         print(repr(err))
#     return proxy


#print(len(proxylist))

#check them all with futures super quick
# with concurrent.futures.ThreadPoolExecutor() as executor:
#         executor.map(extract, proxylist)
        


def test_proxy(proxy):
    try:
        response = requests.get('http://httpbin.org/ip', proxies={"http": proxy, "https": proxy}, timeout=5)
        return response.json()  # Returns the IP address seen by the server
    except Exception as e:
        return None  # Return None if the proxy fails


      
def main():
    proxylist = getProxies()
    
    working_proxies = []

    for proxy in proxylist:
        result = test_proxy(proxy)
        if result:
            working_proxies.append(proxy)
        else:
            pass

    print("Working proxies:", working_proxies)
    
    with open('proxies.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Proxy'])  # Write the header
        for proxy in working_proxies:
            writer.writerow([proxy])  # Write each proxy in a new row

if __name__ == '__main__':
    main()