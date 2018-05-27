def sort (blist):
    for i in range(len(blist)):
        print (sorted(blist, key=lambda list: list[1], reverse=True)[i])
