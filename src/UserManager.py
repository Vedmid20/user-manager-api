import requests
from .User import User
from colorama import Fore


class UserManager:
    def __init__(self):
        self.URL = 'https://jsonplaceholder.typicode.com/users'

    def fetch_users(self):
        self.response = requests.get(self.URL)
        self.status = self.response.status_code
        self.users = self.response.json()
        return self.users

    def parse_users(self):
        return [User(user['id'], user['name'], user['username'], user['email']) for user in self.fetch_users()]

    def more_info(self, user_id):
        self.user = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
        self.detail = (f'{Fore.LIGHTBLUE_EX + f'\nUser: {self.user.json()["id"]}. {self.user.json()["name"]}\n' + Fore.RESET}'
                       f'\tAddress: {self.user.json()["address"]["street"]}, {self.user.json()["address"]["suite"]}, {self.user.json()["address"]["city"]}, {self.user.json()["address"]["zipcode"]}\n'
                       f'\tPhone: {self.user.json()["phone"]}\n'
                       f'\tWebsite: {self.user.json()["website"]}\n'
                       f'\tCompany: {self.user.json()["company"]["name"]}, {self.user.json()["company"]["catchPhrase"]}, {self.user.json()["company"]["bs"]}')
        return self.detail