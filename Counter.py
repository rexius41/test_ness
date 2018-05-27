from collections import Counter
def counter(value):
    index_uni = Counter(value).keys()
    index_cou = Counter(value).values()
    for i in range(len(index_uni)):
        print(list(index_uni)[i])
        print(list(index_cou)[i])
