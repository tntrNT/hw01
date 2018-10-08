for i in range(1,10):
    for j in range(1,i):
        print (end="       ")
    for j in range(i,10):
            format='{0:1}*{1:1}={2:<2}' .format(i,j,i*j)
            print(format,end=" ")
    print (" ")
