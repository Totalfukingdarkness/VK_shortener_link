import os
import requests
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


class ApiExceptionError(Exception):
    def __init__(self, message, error_msg):
        message = f'Api error: {error_msg}'
        super().__init__(message)


def shorten_link(token, url):
    api_short_link = 'https://api.vk.ru/method/utils.getShortLink'

    payload = {
        'access_token': token,
        'url': url,
        'private': 0,
        'v': '5.199',
        }
    response = requests.get(api_short_link, params=payload, timeout=10)
    response.raise_for_status()
    short_link = response.json()
    if 'error' in short_link:
        raise ApiExceptionError(
            'Api error: ', short_link['error']['error_msg']
        )
    return short_link['response']['short_url']


def count_clicks(token, url):
    api_count_clicks = 'https://api.vk.ru/method/utils.getLinkStats'

    payload = {
        'access_token': token,
        'key': url,
        'source': 'vk_cc',
        'interval': 'forever',
        'intervals_count': 1,
        'extended': 0,
        'v': '5.199',
    }
    response = requests.get(api_count_clicks, params=payload, timeout=10)
    response.raise_for_status()
    count_clicks = response.json()
    if 'error' in count_clicks:
        raise ApiExceptionError(
            'Api error: ', count_clicks['error']['error_msg']
        )
    return count_clicks["response"]["stats"][0]["views"]


def is_shorten_link(token, url):
    parameters = {
        'key': url,
        'interval': 'forever',
        'access_token': token,
        'v': '5.199'
    }
    response = requests.get(
        'https://api.vk.com/method/utils.getLinkStats', params=parameters
    )
    response.raise_for_status()
    return 'error' not in response.json()


def main():
    parser = argparse.ArgumentParser(
        description='Ввод ссылки'
    )
    parser.add_argument('link', help='Введите ссылку', type=str)
    args = parser.parse_args()
    url = args.link
    parsed_url = urlparse(url).path[1:]
    load_dotenv('.env')
    token = os.environ['VK_API_TOKEN']

    try:
        if is_shorten_link(token, parsed_url):
            number_of_view = count_clicks(token, parsed_url)
            print('Количество переходов по ссылке: ', number_of_view)
        else:
            short_link = shorten_link(token, url)
            print(short_link)
    except ApiExceptionError as error:
        print(error)


if __name__ == '__main__':
    main()