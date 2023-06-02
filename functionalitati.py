import requests


def coordonatele() -> dict:
    respone = requests.get(url='http://api.open-notify.org/iss-now.json')
    respone.raise_for_status()
    data = respone.json()
    return {
        'x': round(float(data['iss_position']['longitude']), 2),
        'y': round(float(data['iss_position']['latitude']), 2)
    }

print(coordonatele())