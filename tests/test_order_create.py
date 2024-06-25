import allure
import requests
import pytest
from data import URL, ORDER_DATA


class TestCreateOrder:
    @allure.title('Проверки создания заказа')
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_create_order(self, color):
        ORDER_DATA['color'] = color
        response = requests.post(URL.ORDER, json=ORDER_DATA)
        assert response.status_code == 201 and 'track' in response.text