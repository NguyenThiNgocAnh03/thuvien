# list1=[]
# def __init__(self,ms,hoten,dlt,dth):  
#         self.ms
#         self.hoten = hoten
#         self.dlt = dlt
#         self.dth = dth
# def dtb(self):
#         return (self.dlt + self.dth)/2
# def in_sv(self):
#         print(self.ms,self.hoten,self.dlt,self.dth)
# for sinhvien in list1:
#     #Tham chiếu đến phương thức in_hs
#          sinhvien.in_hs()
#     #Tham chiếu đến phương thức dtb
#          print("Trung bình điểm của",sinhvien.hoten,"là",sinhvien.dtb())

# class SinhVien:
#     def __init__(self, ms, hoten, dlt, dth):  
#         self.ms = ms
#         self.hoten = hoten
#         self.dlt = dlt
#         self.dth = dth

#     def dtb(self):
#         return (self.dlt + self.dth) / 2

#     def in_sv(self):
#         print(self.ms, self.hoten, self.dlt, self.dth)

# # Danh sách sinh viên (ban đầu rỗng)
# list1 = []

# # Thêm sinh viên vào danh sách
# list1.append(SinhVien(1, "Nguyen Van A", 8, 7))
# list1.append(SinhVien(2, "Tran Thi B", 6, 9))

# # Duyệt danh sách và gọi các phương thức
# for sinhvien in list1:
#     sinhvien.in_sv()  # In thông tin sinh viên
#     print("Trung bình điểm của", sinhvien.hoten, "là", sinhvien.dtb())



# class SinhVien:
#     def __init__(self,ms,hoten,dlt,dth):
#         self.ms=ms
#         self.hoten=hoten
#         self.dlt=dlt
#         self.dth=dth
#     def dtb(self):
#         dtb=(self.dlt+self.dth)/2
#         return dtb
#     def sv(self):
#         print(self.ms, self.hoten, self.dlt,self.dth)
# list1=[]
# sl=int(input('nhập số lượng sinh viên:'))
# for i in range (1,sl+1):
#     a=int(input(f'nhập mã số sinh viên thứ {i}:'))
#     b=input('Nhập tên học sinh:')
#     c =float(input('nhập điểm lí thuyết của học sinh:'))
#     d=float(input('nhập điểm thực hành của học sinh:'))
#     list1.append(SinhVien(a,b,c,d))
# for i in list1:
#     i.sv()
#     print (f'điểm trung bình của {i.hoten} là {i.dtb()}')



# class Node: 
#     def __init__(self, data=None): 
#         self.data = data 
#         self.next = None 
# class LinkedList: 
#     def __init__(self): 
#         self.head = None 
#     def Print(self): 
#         temp = self.head 
#         while temp is not None: 
#             print(temp.data) 
#             temp = temp.next 
# sv = LinkedList() 
# Viết hàm tạo Node: 
# sv1, sv2, sv3 = Node(), Node(), Node() 
# sv.head = sv1 
# sv1.next, sv2.next = sv2, sv3 
# sv1.data = ['1A', 'Tuong', 9, '12/12'] 
# sv2.data = ['1B', 'Bao', 8, '10/12'] 
# sv3.data = ['1C', 'Gia Huy', 7, '11/12'] 
# sv.Print()

# class Node:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None
# class SLinkedList:
#     def __init__(self):
#         self.headval = None
#     def listprint(self): 
#         printval = self.headval
#         while printval is not None:
#             print (printval.dataval)
#             printval = printval.nextval
#     def AtBegining(self,newdata):
#         NewNode = Node(newdata)
#         NewNode.nextval = self.headval
#         self.headval = NewNode
#     def AtEnd(self, newdata):
#         NewNode = Node(newdata)
#         if self.headval is None:
#             self.headval = NewNode
#             return
#         last = self.headval
#         while last.nextval:
#             last = last.nextval
#         last.nextval = NewNode
# class sv:
#         def __init__(self, maso, hoten, lop, diem):
#                 self.maso = maso
#                 self.hoten = hoten
#                 self.lop=lop
#         def InsertAfterValue(self, target_val, newdata):
#             new_node = Node(newdata)
#             current = self.headval
#             while current is not None:
#                 if "diem 10" in current.dataval:
#                     new_node.nextval = current.nextval
#                     current.nextval = new_node
#                     return
#                 current = current.nextval
#         print("Không tìm thấy điểm 10 trong danh sách")      
# list=SLinkedList()
# n= int(input("So luong sinh vien: "))
# for i in range (1,n+1):
#         print("Nhap du lieu cho sinh vien thu "+str(i)+": ")
#         h= input("Ma so: ")
#         l= input("Ho ten sinh vien: ")
#         m= input("Lop: ")
#         i= float(input("Diem: "))
#         k=sv(h,l,m,i)
#         t=("Sinh vien {} mã số {} lop {} có số điểm {}.".format(k.hoten, k.maso,k.lop, k.diem))
#         # list.AtBegining(t)
#         list.AtEnd(t)
# list.listprint()
# list.InsertAfterValue()
# list.listprint()


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None  # Danh sách liên kết rỗng

    # Hàm in danh sách sinh viên
    def listprint(self): 
        printval = self.headval
        while printval:
            print(printval.dataval)
            printval = printval.nextval

    # Hàm chèn dữ liệu vào cuối danh sách
    def append(self, newdata):
        NewNode = Node(newdata)
        if not self.headval:  # Nếu danh sách rỗng, thêm node đầu tiên
            self.headval = NewNode
            return
        last = self.headval
        while last.nextval:  # Tìm node cuối danh sách
            last = last.nextval
            last.nextval = NewNode  # Gán node cuối trỏ đến node mới



    # Hàm chèn sinh viên sau sinh viên có điểm 10
    def insertAfter10(self, new_data):
        temp = self.headval
        while temp:
            if "số điểm 10.0" in temp.dataval:  # Tìm sinh viên có điểm 10
                new_node = Node(new_data)
                new_node.nextval = temp.nextval
                temp.nextval = new_node
                return  # Chỉ chèn một lần sau sinh viên đầu tiên có điểm 10
            temp = temp.nextval

# Lớp Sinh viên
class SinhVien:
    def __init__(self, maso, hoten, lop, diem):
        self.maso = maso
        self.hoten = hoten
        self.lop = lop
        self.diem = diem

    def __str__(self):
        return "Sinh viên {} mã số {} lớp {} có số điểm {}.".format(self.hoten, self.maso, self.lop, self.diem)

# Nhập danh sách sinh viên
danh_sach = SLinkedList()
n = int(input("Số lượng sinh viên: "))

for i in range(n):
    print(f"Nhập thông tin sinh viên thứ {i+1}:")
    maso = input("Mã số: ")
    hoten = input("Họ tên: ")
    lop = input("Lớp: ")
    diem = float(input("Điểm: "))
    sv = SinhVien(maso, hoten, lop, diem)
    danh_sach.append(str(sv))

# Nhập sinh viên đặc biệt cần chèn sau sinh viên có điểm 10
print("\nNhập thông tin sinh viên cần thêm sau sinh viên có điểm 10:")
maso = input("Mã số: ")
hoten = input("Họ tên: ")
lop = input("Lớp: ")
diem = float(input("Điểm: "))
sv_dac_biet = SinhVien(maso, hoten, lop, diem)
danh_sach.insertAfter10(str(sv_dac_biet))

# # In danh sách sinh viên sau khi cập nhật
# print("\nDanh sách sinh viên sau khi cập nhật:")
# danh_sach.listprint()















# list.listprint()


# class PhongHoc:
#     def __init__(self,DuLieu= None):
#         self.DuLieu=DuLieu
#         self.nextDuLieu=None
# class LinkLienKet:
#     def __init__(self):
#         self.footer=None
#     def LienKetList(self):
#         printL=self.footer
#         while printL is None:
#             print(printL.DuLieu)
#             DuLieu=DuLieu.nextDuLieu
#     def AtFinishing(self,DuLieuMoi):
#         NewDuLieu=None(DuLieuMoi)
#         NewDuLieu = self.footer
#         self.footer = NewDuLieu.nextDuLieu
# class sv:
#         def __init__(self, maso, hoten, lop, diem):
#             self.maso = maso
#             self.hoten = hoten
#             self.lop=lop
#             self.diem = diem 
# list=LinkLienKet()
# n= int(input("So luong sinh vien: "))
# for i in range (1,n+1):
#         print("Nhap du lieu cho sinh vien thu "+str(i)+": ")
#         h= input("Ma so: ")
#         l= input("Ho ten sinh vien: ")
#         m= input("Lop: ")
#         i= float(input("Diem: "))
#         k=sv(h,l,m,i)
#         t=("Sinh vien {} mã số {} lop {} có số điểm {}.".format(k.hoten, k.maso,k.lop, k.diem))
#         list.AtFinishing(t)
# list.LienKetList() 





