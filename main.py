import argparse
import requests

from dotenv import dotenv_values
from urllib.parse import urlparse


BITLY_URL = 'https://api-ssl.bitly.com'


def shorten_link(token, long_url):
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'long_url': long_url}
    url = f'{BITLY_URL}/v4/shorten'

    response = requests.post(url, headers=headers, json=payload)

    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(token, bitlink):
    headers = {'Authorization': f'Bearer {token}'}
    url = f'{BITLY_URL}/v4/bitlinks/{bitlink}/clicks/summary'
    params = {'unit': 'day', 'units': -1}

    response = requests.get(url, headers=headers, params=params)

    response.raise_for_status()
    total_clicks = response.json()['total_clicks']
    return total_clicks


def is_bitlink(token, bitlink):
    headers = {'Authorization': f'Bearer {token}'}
    url = f'{BITLY_URL}/v4/bitlinks/{bitlink}'

    response = requests.get(url, headers=headers)

    return response.ok


def create_parser():
    """Функция производит синтаксический анализ командной строки
    """
    parser = argparse.ArgumentParser(
        description='Программа показывает количество переходов по короткой ссылке'
    )
    parser.add_argument(
        'user_url',
        help="ссылка для подсчета переходов",
        default="bit.ly/3VNuchW",
        type=str
    )
    return parser


def main():
    bitly_token = dotenv_values(".env")['BITLY_TOKEN']
    args = create_parser().parse_args()
    user_url = args.user_url

    url_components = urlparse(user_url)
    bitlink = f'{url_components.netloc}{url_components.path}'

    try:
        if is_bitlink(bitly_token, bitlink):
            clicks_count = count_clicks(bitly_token, bitlink)
            print('Переходов по ссылке', clicks_count)
        else:
            bitlink = shorten_link(bitly_token, user_url)
            print('Битлинк', bitlink)
    except requests.exceptions.HTTPError:
        print("Вы ввели неправильную ссылку или неверный токен.")


if __name__ == '__main__':
    main()
