import os
import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru/'

    def get_api_key(self, email: str, password: str) -> json:
        """Метод отправляет запрос к API; возвращает статус и результата в установленных переменных
        в формате json с уникальным ключом пользователя, найденным по отправленным email и password"""

        headers = {
            'accept': 'application/json',
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result
        pass
    def get_list_of_pest(self, auth_key: json, filter: str) -> json:
        """Метод отправляет завпрос к API с ключом пользователя и возварщает спсиок питомцев с учётом
        параметров filter"""
        header = {
            'accept': 'application/json',
            'auth_key': auth_key['key']
        }
        filter = {
            'filter': filter
        }
        res = requests.get(self.base_url+'api/pets', headers=header, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result
    def post_newPet(self, auth_key: json, name: str, pet_type: str, age: str, pet_photo: str) -> json:
        ''''Добавляет питомца через отправку запроса к API;
        вводим строковые данные: имя, статус и фото_урл'''

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': pet_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'accept': 'application/json',
                   'auth_key': auth_key['key'],
                   'Content-Type': data.content_type}

        res = requests.post(self.base_url+'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result
    def delete_pet(self, auth_key: json, pet_ID: str) -> json:
        '''Метод удаляет питомца. Принмает ID, также нужен уникальный API_key'''
        header = {
            'accept' : 'application/json',
            'auth_key': auth_key['key']
        }
        res = requests.delete(self.base_url + f'api/pets/{pet_ID}', headers=header)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result
    def create_simple_pet(self, auth_key: json, name: str, pet_type:str, age:str):
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': pet_type,
                'age': age
            })
        header = {
            'accept': 'application/json',
            'auth_key': auth_key['key'],
            'Content-Type': data.content_type
        }

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=header, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result
    def upload_photo(self, auth_key: json, pet_ID: int, pet_photo: str) -> json:

        data = MultipartEncoder(
            fields = {
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        header = {'accept': 'application/json',
                   'auth_key': auth_key['key'],
                   'Content-Type': data.content_type
                  }
        res = requests.post(self.base_url + f'api/pets/set_photo/{pet_ID}',
                            headers=header, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result
