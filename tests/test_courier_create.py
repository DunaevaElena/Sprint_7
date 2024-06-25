import allure
import helpers
import requests
import pytest
from data import URL, Answers


class TestCreateCourier:

    @allure.title('Проверка успешного создания курьера')
    def test_create_courier(self, unregistered_courier):
        payload = unregistered_courier
        response = requests.post(URL.COURIER, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверка создания двух одинаковых курьеров')
    def test_create_clone_courier(self, unregistered_courier):
        payload = unregistered_courier
        requests.post(URL.COURIER, data=payload)
        response = requests.post(URL.COURIER, data=payload)
        assert response.status_code == 409 and response.json().get('message') \
               == Answers.SAME_LOGIN

    @allure.title('Проверка обязательных полей при создании курьера')
    @pytest.mark.parametrize('empty_field', ['login', 'password'])
    def test_missed_fields(self, empty_field):
        login, password, first_name = helpers.generate_unregistered_courier()
        payload = {
            'login': login,
            'password': password,
            'firstName': first_name
        }
        del payload[empty_field]
        response = requests.post(URL.COURIER, data=payload)
        assert response.status_code == 400 and response.json().get('message') == Answers.NOT_DATA_FOR_CREATE