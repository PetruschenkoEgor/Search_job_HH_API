from unittest import TestCase
from unittest.mock import patch

from src.api_vacancy import HeadHunterAPI


@patch("src.api_vacancy.requests.get")
def test_api_vacancy_requests_get(mock_get, get_json):
    """ Тест гет запроса """
    api1 = HeadHunterAPI()
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = get_json
    assert api1.connect_to_api == get_json


@patch("src.api_vacancy.requests.get")
def test_api_vacancy_requests_get_status_code(mock_get):
    """ Тест гет запроса, если статус код не 200 """
    api1 = HeadHunterAPI()
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = 404

    assert api1.connect_to_api == 404
