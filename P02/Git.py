import requests


def getfromgit(url: str):
    value = ""

    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        req = req.json()
        value = "".join(req["payload"]["blob"]["rawLines"][1:])
    else:
        value = None

    return value
