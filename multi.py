num =int(input("enter the number:"))
for x in range(1, num+1):
    print("**********")
    for i in range(1, 11):
        print("%d x %d =%d" %(x, i, x*i))
