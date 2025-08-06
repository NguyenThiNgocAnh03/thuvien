def sumBinhPhuong(so):
    if so==0:
        summ=0
    else:
        summ=so**2+sumBinhPhuong(so-1)
    return summ
a=int(input("moi nhap so: "))
print( "tong : ", sumBinhPhuong(a))
