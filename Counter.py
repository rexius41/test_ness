from collections import Counter
big_list = []
def counter(value):
    index_uni = Counter(value).keys()
    index_cou = Counter(value).values()
    for i in range(len(index_uni)):
        big_list.append((list(index_uni)[i], list(index_cou)[i]))

