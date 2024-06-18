import streamlit as st 
import requests
import uuid
import json

from get_image import get_file_id
from requests.auth import HTTPBasicAuth

CLIENT_ID = st.secrets["CLIENT_ID"]
SECRET = st.secrets["SECRET"]


def get_access_token() -> str:
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': str(uuid.uuid4()),
    }
    payload = {"scope": "GIGACHAT_API_PERS", "function_call": "auto"}
    res = requests.post(
        url=url, 
        headers=headers, 
        auth=HTTPBasicAuth(CLIENT_ID, SECRET), 
        data=payload,
        verify=False)
    access_token = res.json()["access_token"]
    return access_token


# Images
def get_image(access_token: str, file_id: str):
    url = f"https://gigachat.devices.sberbank.ru/api/v1/files/{file_id}/content"

    payload={}
    headers = {
    'Accept': 'image/jpg',
    'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers, data=payload, verify=False)
    return response.content


def send_prompt(msg: str, access_token: str):

    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps({
    "model": "GigaChat",
    "messages": [
        {
        "role": "user",
        "content": msg
        }
    ],
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {access_token}'
    }

    response = requests.post(url, headers=headers, data=payload, verify=False)

    return response.json()["choices"][0]["message"]["content"]


def sent_prompt_check(msg: str, access_token: str):
    res = send_prompt(msg, access_token)
    data, is_image = get_file_id(res)
    if is_image:
        data = get_image(file_id=data, access_token=access_token)
    return data, is_image