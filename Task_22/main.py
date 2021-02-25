import requests
from pprint import pprint
from ya_token import ya_token


def make_a_folder(tttoken):
    HEADERS = {"Authorization": f"OAuth {tttoken}"}

    response_folder = requests.put("https://cloud-api.yandex.net/v1/disk/resources",
                                   params={"path": f"/New_folder15"},
                                   headers=HEADERS)
    # response_folder.raise_for_status()
    # print(response_folder.status_code) #код ответа
    result_folder = response_folder.json()
    # print(result_folder) # сам ответ
    # href_ya = result_folder['href']
    # print(href_ya)
    # print('Folder on Yandex disk was created')
    return response_folder.status_code, result_folder


if __name__ == '__main__':
    make_a_folder(ya_token)

