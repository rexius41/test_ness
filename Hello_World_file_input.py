try:
    file_test = open("test.txt","w+")
except:
    print ("error while opening/creating file")
for i in range(10):
    print (i)
    file_test.write(input())
    file_test.write(" ")
file_test.close()
