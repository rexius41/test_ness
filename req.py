import requests
def rest_request(method, url, token, json=None):
    _resp = requests.request(
        method,
        url,
        json=json,
        headers= {"Authorization": "token " + token, "Accept": "application/vnd.github.v3+json"},
        timeout=30)
    _status = _resp.headers["status"]
    if "200" in _status or "201" in _status:
        return _resp.json()
    elif "204" in _status:
        return _resp
    else:
        raise ValueError(_resp.json()["message"])