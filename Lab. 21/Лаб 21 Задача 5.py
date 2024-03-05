import requests

res = requests.get('https://yandex.by/news?mlid=')
print(res.headers)

res = requests.get('https://50.by/catalog/sadovaya-te')
print(res.headers)

res = requests.get('https://vk.com/dev')
print(res.headers)

res = requests.get('http://docs.google.com/spreadshe/')
print(res.headers)

res = requests.get('http://www.pageranker.ru/articles/troubleshooting/167--403-forbidden.htm')
print(res.headers)
