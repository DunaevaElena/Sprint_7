import allure
import helpers
import requests
import pytest
from data import URL, Answers


class TestLoginCourier:
    @allure.title('Проверка, что курьер может авторизоваться')
    def test_courier_login(self, registered_courier):
        payload = registered_courier
        response = requests.post(URL.LOGIN, data=payload)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверка пропуска обязательных полей формы авторизации')
    @pytest.mark.parametrize('empty_field', ['login', 'password'])
    def test_missed_fields(self, registered_courier, empty_field):
        payload = registered_courier.copy()
        payload[empty_field] = ''
        response = requests.post(URL.LOGIN, data=payload)
        assert response.status_code == 400 and response.json().get('message') == Answers.NOT_DATA_FOR_AUTH

    @allure.title('Проверка передачи некорректных данных при авторизации')
    @pytest.mark.parametrize('invalid_data', ['login', 'password'])
    def test_courier_login_with_invalid_data(self, registered_courier, invalid_data):
        payload = registered_courier.copy()
        payload[invalid_data] += '2п='
        response = requests.post(URL.LOGIN, data=payload)
        assert response.status_code == 404 and response.json().get('message') == Answers.ACCOUNT_NOT_FOUND

    @allure.title('Проверка авторизации несуществующим пользователем')
    def test_login_unregistered_courier(self):
        login, password, first_name = helpers.generate_unregistered_courier()
        payload = {
            'login': login,
            'password': password
        }
        response = requests.post(URL.LOGIN, data=payload)
        assert response.status_code == 404 and response.json().get('message') == Answers.ACCOUNT_NOT_FOUND