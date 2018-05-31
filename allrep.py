repolist = []
from req import GithubRequester
def getallrepo(token):
    x = 1
    rep = GithubRequester()
    while rep.rest_request("GET", "https://api.github.com/orgs/performgroup/repos?page={}&per_page=50".format(x), token) != []:
        responses = rep.rest_request("GET", "https://api.github.com/orgs/performgroup/repos?page={}&per_page=50".format(x), token)
        for i in range (len(responses)):
            if (responses[i]['size']) == 0:
                print("empty repo")
                print (responses[i]['name'])
            else:
                repolist.append(responses[i]['name'])
        x=x+1
    print(repolist)
    print(len(repolist))

