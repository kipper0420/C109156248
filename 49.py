a=set(["John","Mary","Tina","Fiona","Claire","Eva","Ben","Bill","Bert"])
b=set(["John","Mary","Fiona","Claire","Ben","Bill"])
c=set(["Mary","Fiona","Claire","Eva","Ben"])
print("英文與數學都及格",b&c)
print("數學不及格",a-b)
print("英文及格且數學不及格",c&a-b)