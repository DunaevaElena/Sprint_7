import requests
import random
import string
from data import URL


def register_new_courier_and_return_login_password():
    login_pass = []
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(URL.COURIER, data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    return login_pass

def generate_unregistered_courier():
    courier_data = []
    while len(courier_data) != 3:
        courier_data.append(generate_random_string(8))
    return courier_data

def generate_random_string(length):
    random_string = ''.join(random.choices(string.ascii_lowercase, k=length))
    return random_string





