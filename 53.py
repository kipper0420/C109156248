a= float(input("請輸入路程公里數(km)"))
if( a <= 1.5):
    print("所需車資：75元")
elif( a >1.5 ):
    b = ((a-1.5)/0.25)
    c = (b)*5
    d = 75+c
    d = ('%.0f'%d)
    print("所需車資：%s元"%(d))
