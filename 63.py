b=0
a=int(input("請輸入正整數n:"))
for i in range(1,n):
    if a % i ==0:
        b=b+i
if b == a :
    print("perfect")
elif b > a :
    print("abundant")
elif b < a:
    print("deficient")