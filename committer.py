def commit_er(size_array):
    s_array = len(size_array)
    for i in range(s_array):
        x =(size_array[i]['commit'])
        y=(x['committer'])
        print(y['name'])
