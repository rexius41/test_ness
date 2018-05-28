import requests
import committer
import Counter
import sorter
import extr
from committer import test
from Counter import big_list
from sorter import list_sorted
token = input ('enter aut. token>>>')
def rest_request(method, url, json=None):
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
reposlist = []
responses = rest_request("GET", "https://api.github.com/users/rexius41/repos")
for i in range (len(responses)):
    reposlist.append(responses[i]['name'])
print (reposlist)
for i in range (len(reposlist)):
    response = rest_request("GET", "https://api.github.com/repos/rexius41/{}/commits".format(reposlist[i]))
    committer.commit_er(response)
Counter.counter(test)
sorter.sort(big_list)
extr.export_excel(list_sorted)