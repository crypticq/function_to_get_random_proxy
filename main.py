import socket
import requests


def random_proxy():
    proxy_list = requests.get('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt').text.splitlines()
    random_proxy = random.choice(proxy_list)
    rip = random_proxy.rsplit(':', 1)[0] #random proxy ip
    rpp = random_proxy.rsplit(':', 1)[1] #random proxy port
    proxies = {
        'http': random_proxy,
        'https': random_proxy,
    }
    try:
        s = socks.socksocket()
        s.set_proxy(socks.HTTP, rip, rpp)
        socket.socket = socks.socksocket
        urllib.request.urlopen
    except (IndexError, IndentationError):
        print('Not Working')
        
    return proxies
