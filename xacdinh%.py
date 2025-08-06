# # def tinh_ty_le(diem):
# #     tong = sum(diem)
# #     trung_binh = tong / len(diem)
# #     dem = sum(1 for d in diem if d > trung_binh)
# #     ty_le = (dem / len(diem)) * 100
# #     return ty_le

# # # Ví dụ nhập điểm cho 50 sinh viên
# # for i in range(50):
# #     diem = float(input(f"Nhập điểm sinh viên {i+1}: "))

# # ty_le = tinh_ty_le(diem)
# # print(f"Tỷ lệ sinh viên có điểm trên trung bình: {ty_le:.2f}%")

# class Node:
#     def __init__(self, diem):
#         self.diem = diem
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def them_cuoi(self, diem):
#         new_node = Node(diem)
#         if not self.head:
#             self.head = new_node
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new_node

#     def tinh_ty_le_tren_trung_binh(self):
#         # Tính tổng và đếm số node
#         tong = 0
#         count = 0
#         temp = self.head
#         while temp:
#             tong += temp.diem
#             count += 1
#             temp = temp.next

#         if count == 0:
#             print("Danh sách rỗng.")
#             return

#         trung_binh = tong / count

#         # Đếm số sinh viên có điểm > trung bình
#         dem_tren_tb = 0
#         temp = self.head
#         while temp:
#             if temp.diem > trung_binh:
#                 dem_tren_tb += 1
#             temp = temp.next

#         ty_le = (dem_tren_tb / count) * 100
#         print(f"Trung bình điểm: {trung_binh:.2f}")
#         print(f"Tỷ lệ sinh viên có điểm trên trung bình: {ty_le:.2f}%")

# # --- Chương trình chính ---

# ds = LinkedList()

# print("Nhập điểm cho 50 sinh viên:")
# for i in range(10):
#     diem = float(input(f"Sinh viên {i+1}: "))
#     ds.them_cuoi(diem)

# ds.tinh_ty_le_tren_trung_binh()



list=[]
class sinhvien:
    def __init__(self,MS,Hoten,diem):
        self.MS=MS
        self.Hoten=Hoten
        self.diem=diem
n=int(input('nhap so luong sinh vien: '))
for i in range(1,n+1):
    print('nhap sinh vien thu : ',i)
    ms=int(input('nhap ma so sinh vien: '))
    ten=input('nhap ten sinh vien: ')
    diem=float(input('nhap diem sinh vien: '))
    SV=sinhvien(ms,ten,diem)
    list.append(SV)
dem=0
tong_diem=0
for SV in list:
    tong_diem = tong_diem+SV.diem
trung_binh = tong_diem / n

# Đếm số sinh viên có điểm > trung bình
for SV in list:
    if SV.diem>trung_binh:
        dem = dem+1
# Tính tỷ lệ
ty_le = (dem / n) * 100

print(f"\nĐiểm trung bình của lớp là: {trung_binh:.2f}")
print(f"Tỷ lệ sinh viên có điểm trên trung bình: {ty_le:.2f}%")