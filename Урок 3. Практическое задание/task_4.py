"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from uuid import uuid4
from hashlib import sha256


class UrlStorage:
    def __init__(self):
        self.url_dict = dict()
        self.salt = uuid4().hex

    def url_add(self, url):
        if self.url_dict.get(url):
            print(f'{url} уже есть в списке')
        else:
            self.url_dict[url] = sha256(url.encode() + self.salt.encode()).hexdigest()
            print('Сайт добавлен')

    def __str__(self):
        return 'Добавленные адреса:\n' + '\n'.join(self.url_dict.keys())


test = UrlStorage()
test.url_add('vk.com')
test.url_add('vk.com')
test.url_add('mail.ru')
test.url_add('geekbrains.ru')
test.url_add('mail.ru')
print(test)
