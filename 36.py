n = int(input("輸入n"))
while n != 1:
    if(n%2==1):
        n = n*3+1
    else:
        n = n/2
    print(int(n))