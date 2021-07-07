import requests
from dotenv import load_dotenv
import os


def get_upload_url(token, file_name):
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    params = {'path': file_name}
    headers = {'Authorization': f'OAuth {token}'}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    data = response.json()
    link = data['href']
    return link


def upload_file(url, path_name):
    with open(path_name, 'rb') as file:
        files = {'file': file}
        response = requests.put(url, files=files)
        response.raise_for_status()
        if response.status_code == 201 and response.ok:
            print('Файл успешно сохранен на яндекс диске!')
        else:
            print(f'Возможно что-то пошло не так! status_code = {response.status_code}')


if __name__ == '__main__':
    load_dotenv()
    path_name = input('Напишите абсолютный путь к файлу ')
    file_name = path_name.split('\\')[-1]
    yandex_disk_token = os.getenv('YANDEX_DISK_TOKEN')
    upload_url = get_upload_url(yandex_disk_token, file_name)
    upload_file(upload_url, 'image.jpg')
