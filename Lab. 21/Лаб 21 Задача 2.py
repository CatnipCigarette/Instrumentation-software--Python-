import requests

def answer():
    if res:
        print('Запрос выполнен')
    else:
        print('Ошибка запроса')

def error_code():
    if res.status_code == 102:
    	print('Идёт обработка')
    elif res.status_code == 200:
        print('Всё хорошо')
    elif res.status_code == 204:
        print('Нет содержимого')
    elif res.status_code == 400:
        print('Невернный запрос')
    elif res.status_code == 404:
        print('Не найдено')
    elif res.status_code == 408:
        print('Истекло время ожидания')
    elif res.status_code == 410:
        print('Удалён')
    elif res.status_code == 500:
        print('Внутренняя ошибка сервера')
    elif res.status_code == 521:
        print('Веб-сервер не работает')
    elif res.status_code == 522:
        print('Соединение не отвечает')
    elif res.status_code == 524:
        print('Время ожидания истекло')
    else:
        print('Каод ошибки не указан в реестре!')

res = requests.get('https://yandex.by/news?mlid=')
print(res)
answer()
error_code()
    
res = requests.get('https://50.by/catalog/sadovaya-te')
print(res)
answer()
error_code()

res = requests.get('https://vk.com/dev')
print(res)
answer()
error_code()

res = requests.get('http://docs.google.com/spreadshe/')
print(res)
answer()
error_code()

res = requests.get('http://www.pageranker.ru/articles/troubleshooting/167--403-forbidden.htm')
print(res)
answer()
error_code()
