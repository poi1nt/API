import requests

url = "https://cloud-api.yandex.net/v1/disk/resources/upload"

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_name = file_path.split('\\')[-1]
        files = {'file': open(file_name, 'rb')}
        params = {'path': file_name, 'overwrite': True}
        headers = {'Authorization': self.token}
        href = requests.get(url, headers=headers, params=params).json()['href']
        requests.put(href, files=files)

if __name__ == '__main__':
    path_to_file = input('Ведите путь до передаваемого файла: ')
    token = input('Ведите свой токен: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)  