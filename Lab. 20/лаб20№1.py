from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit

http_address = 'https://lpgenerator.ru:80/blog/2011/04/25/url-adresa-i-celevye-stranicy/'
ftp_address = 'ftp://user:123456@mysite.ru'

adress = urlparse(http_address)
print('Разбор:', adress)
adress_1 = tuple(adress)
print('Кортеж:', adress_1)
print('Название протокола:', adress_1[0])
print('Название доменна:', adress_1[1])
print('Номер порта:', adress.port)
print('Путь:', adress_1[2])
print('Параметры:', adress_1[3])
print('Строка запроса:', adress_1[4])
print('Якорь:', adress_1[5])
print('URL-адрес:', urlunparse(adress_1))

adress_2 = urlparse(ftp_address)
print('Имя:', adress_2.username, 'Пароль:', adress_2.password)

breakdown = (urlsplit('https://lpgenerator.ru/blog/2011/04/25/url-adresa-i-celevye-stranicy/'))
print('Разбивка:',breakdown )
print('Сборка:', urlunsplit(breakdown))
