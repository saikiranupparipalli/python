import requests

def main():
    url = "https://randomuser.me/api/"
    res = requests.get(url)
    # print(res)
    # print('*' * 40)
    data = res.json()
    first = data['results']
    ls = first[0]
    location = ls['location']['street']
    print(location)

main()