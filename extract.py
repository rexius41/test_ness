import requests

def rest_request(method, url, json=None):
    _resp = requests.request(
        method,
        url,
        json=json,
        headers= {"Authorization": "token " + "e65d18715e4659bec90b929e3ac6456e226dc6b3", "Accept": "application/vnd.github.v3+json"},
        timeout=30)
    _status = _resp.headers["status"]
    if "200" in _status or "201" in _status:
        return _resp.json()
    elif "204" in _status:
        return _resp
    else:
        raise ValueError(_resp.json()["message"])



response = rest_request("GET", "https://api.github.com/repos/rexius41/test_ness/commits")
print(response[0]['sha'])