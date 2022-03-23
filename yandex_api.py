import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = 'AQ'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}


def create_folder(path):
    """Создание папки. \n path: Путь к создаваемой папке."""
    result = requests.put(f'{URL}?path={path}', headers=headers)
    return result.status_code

def get_folder_info(path):
    """Проверка наличия папки на яндекс диске """
    result = requests.get(f'{URL}?path={path}', headers=headers)
    return result.status_code

