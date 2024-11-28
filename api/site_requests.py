import requests
from typing import Union, Dict

def _make_response(method: str, url: str, success=200) -> Union[int,requests]:
    """
    Функция для запроса к API
    :param method: метод запроса
    :param url: url-адрес ресурса
    :param success: характеристики успешного запроса
    :return: responce (dict)
    """
    response = requests.request(
        method,
        url
    )

    status_code = response.status_code

    if status_code == success:
        return response

    return status_code

def dollar(curr: str, method: str=None, url: str=None ,func=_make_response) -> Dict:
    method = 'GET'
    url = f'https://api.nbrb.by/exrates/rates/{curr}'


    response = func(method, url)

    return response.json()

if __name__ == '__main__':
    dollar()