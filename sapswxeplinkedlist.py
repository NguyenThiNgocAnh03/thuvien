# class Node:
#     def __init__(self, data=None):
#         self.data = data  
#         self.next = None
# class SLinkedList:
#     def __init__(self):
#         self.head = None
# class sv:
#     def __init__(self, maso, hoten, lop, diem):
#         self.maso = maso
#         self.hoten = hoten
#         self.lop=lop
#         self.diem = diem
# list=SLinkedList()
# n= int(input("So luong sinh vien: "))
# for i in range (1,n+1):
#     print("Nhap du lieu cho sinh vien thu "+str(i)+": ")
#     h= input("Ma so: ")
#     l= input("Ho ten sinh vien: ")
#     m= input("Lop: ")
#     i= float(input("Diem: "))
#     k=sv(h,l,m,i)
#     t=("Sinh vien {} mã số {} lop {} có số điểm {}.".format(k.hoten, k.maso,k.lop, k.diem))
#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node

#     def listprint(self): 
#         current = self.head
#         while current is not None:
#             print(current.data)
#             current = current.next

#     def sort(self):
#         if self.head is None:
#             return
#         current = self.head
#         while current is not None:
#             index = current.next
#             while index is not None:
#                 if current.data > index.data:
#                     current.data, index.data = index.data, current.data
#                 index = index.next
#                 current = current.next

#         print("Trước khi sắp xếp:")
#         danh_sach.listprint()

#         danh_sach.sort()

#         print("\nSau khi sắp xếp:")
#         danh_sach.listprint()


class Node:
    def __init__(self, data=None):
        self.data = data  
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def listprint(self): 
        current = self.head
        while current is not None:
            print("Sinh viên {} mã số {} lớp {} có số điểm {}.".format(
                current.data.hoten,
                current.data.maso,
                current.data.lop,
                current.data.diem
            ))
            current = current.next

    def sort(self):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            index = current.next
            while index is not None:
                if current.data.diem > index.data.diem:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next

class sv:
    def __init__(self, maso, hoten, lop, diem):
        self.maso = maso
        self.hoten = hoten
        self.lop = lop
        self.diem = diem

# --- Chương trình chính ---
danh_sach = SLinkedList()
n = int(input("Số lượng sinh viên: "))

for i in range(1, n + 1):
    print(f"\nNhập thông tin sinh viên thứ {i}:")
    maso = input("Mã số: ")
    hoten = input("Họ tên: ")
    lop = input("Lớp: ")
    diem = float(input("Điểm: "))
    sv_moi = sv(maso, hoten, lop, diem)
    danh_sach.append(sv_moi)

print("\n--- Trước khi sắp xếp ---")
danh_sach.listprint()

danh_sach.sort()

print("\n--- Sau khi sắp xếp theo điểm tăng dần ---")
danh_sach.listprint()