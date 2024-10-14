from decouple import config
import requests


API = config("API_KEY")
URL = config("URL")


async def resp(content):
    params = {
        "q": content + ",RU",
        "appid": API,
        "units": "metric",
        "type": "like",
        "lang": "ru"
    }
    try:
        response = requests.get(URL, params=params)
        data = response.json()
        print(data)
        temp = data["list"][0]["main"]["temp"]
        hum = data["list"][0]["main"]["humidity"]
        desc = data["list"][0]["weather"][0]["description"]
        return {
            "temp": temp,
            "hum": hum,
            "desc": desc
        }
    except Exception:
        return "Город не найден"
