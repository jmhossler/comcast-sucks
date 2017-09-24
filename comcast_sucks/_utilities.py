import requests


def internetUp():
    try:
        response = requests.get("http://www.google.com")
	return True
    except requests.ConnectionError:
	pass
    return False
