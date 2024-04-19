import requests
import py7zr


def d_f():
    with requests.Session() as s:
        payload = {
            "login": "VETROOGK",
            "password": "!Kdc2024"
        }
        url = 'https://rg.green-e-track.ru/api/documents/v1/file/91e3d0d4-8986-4160-8b08-433ddd0826f7'
        url2 = 'https://rg.green-e-track.ru/api/documents/v1/file/984e181e-ec93-4de2-b88d-2a06dd9cbb6e'
        url3 = 'https://rg.green-e-track.ru/api/documents/v1/file/c2e71c1b-ede7-44a7-afc0-63fe356d0450'
        login_url = 'https://rg.green-e-track.ru/api/auth/v1/login'

        response = s.post(login_url, json=payload)
        print(response, response.status_code)
        if response.status_code == 400:
            return 0
        token = response.json()['access_token']
        # print(wget.download(s, url))

        response = s.get(
            url2, headers={'Authorization': f'Bearer {token}'}, stream=True)

        print(response, response.status_code)

        file_Path = 'archive.7z'
        if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
            with py7zr.SevenZipFile("archive.7z", "r") as archive:
                archive.extractall("./t")
            print('File downloaded successfully')
        else:
            print('Failed to download file')


d_f()
