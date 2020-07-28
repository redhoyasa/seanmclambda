import requests

BASE_URL = "http://seanmcapp.herokuapp.com/broadcast"


def broadcast_photo(secret_key, chat_id, photo_file, caption=None):
    with open(photo_file.name, "rb") as f:
        headers = {"secretKey": secret_key}
        files = {"photo": f}
        values = {"caption": caption, "chat_id": chat_id}

        requests.post(BASE_URL, files=files, data=values, headers=headers)
        return None
