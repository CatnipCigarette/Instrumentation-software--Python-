import requests
from urllib.parse import urlparse       

def error_code(link):
    res = requests.get(link)
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
                   503: 'По техническим причинам сервер временно не имеет возможности обрабатывать запросы',
                   521: 'Веб-сервер не работает',
                   522: 'Соединение не отвечает',
                   524: 'Время ожидания истекло'}
    
    print('\n', 'Статус запроса:', status_code[code], '\n', 
          'Код запроса:', code, '\n')


def urlparse_info(link):
    no_element = 'Элемент отсутствует'
    analysis = urlparse(link)
    print("Протокол: ", analysis.scheme or no_element)
    print("Домен: ", analysis.netloc or no_element)
    print("Номер порта: ", analysis.port or no_element)
    print("Путь: ", analysis.path or no_element)
    print("Параметры: ", analysis.params or no_element)
    print("Строка запроса: ", analysis.query or no_element)
    print("Якорь: ", analysis.fragment or no_element)


def byte_text(link):
    url_byte = requests.get(link).content
    url_text = requests.get(link).text
    print(url_byte, url_text, '\n'*2)


links = ['https://mangalib.me/?section=all-updates',
        'https://www.pinterest.com/',
        'https://www.ratatype.ua/ru/',
        'https://paimon.moe/achievement/',
        'https://translate.google.com/?hl=ru']

for link in links:
    urlparse_info(link)
    error_code(link)
    byte_text(link)


