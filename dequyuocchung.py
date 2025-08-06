


def ucln(a,b):
    r=a%b
    if r==0:
        return b
    else:
        return ucln(b,r)
print(ucln(1260,198))