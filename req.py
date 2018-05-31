import requests
class GithubRequester:

    def rest_request(self, method, url, token, json=None):
        self.method = method
        self.url = url
        self.token = token
        self.json = json
        _resp = requests.request(
            self.method,
            self.url,
            json=self.json,
            headers={"Authorization": "token " + self.token, "Accept": "application/vnd.github.v3+json"},
            timeout=30)
        _status = _resp.headers["status"]
        if "200" in _status or "201" in _status:
            return _resp.json()
        elif "204" in _status:
            return _resp
        else:
            raise ValueError(_resp.json()["message"])