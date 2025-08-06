class Node:
    def __init__(self, data=None):
        self.data = data  # Lưu đối tượng SinhVien
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        """In danh sách sinh viên"""
        temp = self.head
        if not temp:
            print("Danh sách trống.")
            return
        while temp:
            print(temp.data)  # In trực tiếp đối tượng SinhVien
            temp = temp.next

    def append(self, new_data):
        """Thêm sinh viên vào cuối danh sách"""
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def removeZeroScoreStudents(self):
        """Xóa sinh viên có điểm bằng 0"""
        while self.head and self.head.data.diem == 0.0:
            self.head = self.head.next  # Xóa nếu sinh viên đầu danh sách có điểm 0

        temp = self.head
        prev = None

        while temp:
            if temp.data.diem == 0.0:
                prev.next = temp.next  # Bỏ qua node có điểm 0
            else:
                prev = temp
            temp = temp.next

class SinhVien:
    def __init__(self, maso, hoten, lop, diem):
        self.maso = maso
        self.hoten = hoten
        self.lop = lop
        self.diem = diem

    def __str__(self):
        return f"Sinh viên {self.hoten} mã số {self.maso} lớp {self.lop} có số điểm {self.diem}."

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
    danh_sach.append(sv)  # Lưu trực tiếp đối tượng SinhVien

# In danh sách trước khi cập nhật
print("\nDanh sách sinh viên ban đầu:")
danh_sach.listprint()

# Xóa sinh viên có điểm bằng 0
print("\nXóa sinh viên có điểm bằng 0...")
danh_sach.removeZeroScoreStudents()

# In danh sách sau khi xóa
print("\nDanh sách sinh viên sau khi xóa sinh viên có điểm 0:")
danh_sach.listprint()
        