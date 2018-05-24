import requests
import committer
def rest_request(method, url, json=None):
    _resp = requests.request(
        method,
        url,
        json=json,
        headers= {"Authorization": "token " + "cdcd1328a5a90004ba6d5773c7d7a3cb2a0f0c60", "Accept": "application/vnd.github.v3+json"},
        timeout=30)
    _status = _resp.headers["status"]
    if "200" in _status or "201" in _status:
        return _resp.json()
    elif "204" in _status:
        return _resp
    else:
        raise ValueError(_resp.json()["message"])



response = rest_request("GET", "https://api.github.com/repos/rexius41/test_ness/commits")
committer.commit_er(response)

