import requests

url = 'https://api.github.com/search/repositories?q=python&sort=stars'
r = requests.get(url)
print('status code:',r.status_code)

response_dict = r.json()
print(response_dict.keys())