import requests

def f2():
    url = 'https://github.com/not_found'
    response = requests.get(url)
    response.raise_for_status()

def f1():
    url = 'https://github.com/not_found'
    response = requests.get(url)
    response.raise_for_status()

if __name__ == '__main__':
    # url = 'https://github.com/not_found'
    try:
        f1()
        f2()
    except requests.HTTPError:
        print('error')
    # try:
    #     f2()
    # except requests.HTTPError:
    #     print('error')
    # response = requests.get(url)
    # response.raise_for_status()