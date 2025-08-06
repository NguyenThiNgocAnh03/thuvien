class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self): 
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
# Hàm chèn dữ liệu vào đầu
    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
class sv:
    def __init__(self, maso, hoten, lop, diem):
        self.maso = maso
        self.hoten = hoten
        self.lop=lop
        self.diem = diem
list=SLinkedList()
n= int(input("So luong sinh vien: "))
for i in range (1,n+1):
    print("Nhap du lieu cho sinh vien thu "+str(i)+": ")
    h= input("Ma so: ")
    l= input("Ho ten sinh vien: ")
    m= input("Lop: ")
    i= float(input("Diem: "))
    k=sv(h,l,m,i)
    t=("Sinh vien {} mã số {} lop {} có số điểm {}.".format(k.hoten, k.maso,k.lop, k.diem))
    list.AtBegining(t)
list.listprint()
