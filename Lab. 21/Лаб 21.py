import requests

def answer():
    if res:
        print('Запрос выполнен')
    else:
        print('Ошибка запроса')


def error_code():
    status_code = dict()
    code = res.status_code
    status_code = {102: 'Идёт обработка',
                   200: 'Всё хорошо',
                   204: 'Нет содержимого',
                   400: 'Неверный запрос',
                   404: 'Не найдено',
                   408: 'Истекло время ожидания',
                   410: 'Удалён',
                   500: 'Внутреняя ошибка сервера',
                   521: 'Веб-сервер не работает',
                   522: 'Соединение не отвечает',
                   524: 'Время ожидания истекло'}
    
    print(status_code[code])


def complete_assignment():
    print(res)
    answer()
    error_code()
    print(res.content)
    print(res.text)
    print(res.headers)
    print(' ')
    

res = requests.get('https://yandex.by/news?mlid=')
complete_assignment()
    
res = requests.get('https://50.by/catalog/sadovaya-te')
complete_assignment()

res = requests.get('https://vk.com/dev')
complete_assignment()

res = requests.get('http://docs.google.com/spreadshe/')
complete_assignment()

res = requests.get('http://www.pageranker.ru/articles/troubleshooting/167--403-forbidden.htm')
complete_assignment()
