S=[]
a=int(input("nhập số: "))
x=int(input("so can tim:"))
for i in range(a):
    b=int(input("nhap phan tử:"))
    S.append(b)
find=False
for j in range(len(S)):
    for k in range(j+1,len(S)):
        if S[j]+S[k]==x:
            print (f"trong danh sach ",S[j],"+",S[k],"=",x,"tại vị trí ",j,k )
            find=True
if find==False:
    print("danh sach không có 2 số có tổng bằng",x)
        
        
        
     
