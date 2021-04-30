a=input("請輸入水果:")
c={"蘋果":"紅色","香蕉":"黃色","葡萄":"紫色","藍莓":"藍色","橘子":"橘色"}
if (a in dict1):
    print(a+"是"+dict1[a])
else:
    b=input("請輸入顏色:")
    dict1[a]=b
    print(a+"是"+dict1[b])