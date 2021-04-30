a=int(input("請輸入階層值M:"))
total=i=1
while (total<=a):
    total=total*i
    i=i+1
print("超過M為"+str(a)+"的最小階層N值為:"+str(i-1))