try:
    file_test = open("test.txt","w+")
except:
    print ("error while opening/creating file")
x = int(input(">>nuber of inputs"))
for i in range(x):
    print (i)
    file_test.write(input())
    file_test.write(" ")
file_test.close()
