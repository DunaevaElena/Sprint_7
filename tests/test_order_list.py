import allure
import requests
from data import URL


class TestOrdersList:
    @allure.title('Проверка получения списка заказов')
    def test_get_order_list(self):
        response = requests.get(URL.ORDER)
        assert response.status_code == 200 and type(response.json()['orders']) is list