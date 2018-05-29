token=[]
import committer
import Counter
import sorter
import extr
import req
import allrep
from committer import test
from Counter import big_list
from sorter import list_sorted
from allrep import repolist
token = input ('enter aut. token>>>')
allrep.getallrepo(token)
y = 1
for x in range (len(repolist)):
    while req.rest_request("GET", "https://api.github.com/repos/performgroup/{}/commits?page={}&per_page=100".format(repolist[x],y), token) != []:
        response= req.rest_request("GET","https://api.github.com/repos/performgroup/{}/commits?page={}&per_page=100".format(repolist[x],y), token)
        committer.commit_er(response)
        y=y+1
Counter.counter(test)
sorter.sort(big_list)
extr.export_excel(list_sorted)
