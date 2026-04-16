import requests

def extract_data():
    url = "https://remoteok.com/api"
    response = requests.get(url)
    data = response.json()
    return data