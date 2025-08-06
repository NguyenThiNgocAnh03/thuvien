# # # def fibonacci(n):
# # #     if n < 2:
# # #         return 1
# # #     else:
# # #         return fibonacci(n - 1) + fibonacci(n - 2)

# # # def tong_fibonacci(n):
# # #     if n == 0:
# # #         return 0
# # #     else:
# # #         return fibonacci(n - 1) + tong_fibonacci(n - 1)

# # # # Nhập và in kết quả
# # # n = int(input("Nhập n: "))
# # # print("Tổng", n, "số Fibonacci đầu tiên là:", tong_fibonacci(n))

# # def tim_so_khong_trung_lap(number):
# #     ds = []
# #     for x in number:
# #         if number.count(x) == 1:
# #             ds.append(x)
# #     return ds

# # # Ví dụ sử dụng
# # a = [1, 2, 2, 3, 4, 4, 5]
# # print("Các số không trùng lặp là:", tim_so_khong_trung_lap(a))
# # def quicksort(arr):
# #     if len(arr) <= 1:
# #         return arr
# #     else:
# #         pivot = arr[0]  # Chọn phần tử đầu làm pivot
# #         left = [x for x in arr[1:] if x < pivot]
# #         right = [x for x in arr[1:] if x >= pivot]
# #         return quicksort(left) + [pivot] + quicksort(right)
# def quickSort(arr, low, high):
# 	if len(arr) == 1:
# 		return arr
# 	if low < high:
# 		# pi là chỉ mục phân vùng, 
#                     #arr [pi] hiện ở đúng vị trí
# 		pi = partition(arr, low, high)
# 		# Sắp xếp riêng biệt các phần tử trước
#                      # phân vùng và sau phân vùng
# 		quickSort(arr, low, pi-1)
# 		quickSort(arr, pi+1, high)

# # Ví dụ sử dụng


# def quicksort(ds):
#     if len(ds) <= 1:
#         return ds

#     chot = ds[0]
#     trai = []
#     phai = []

#     for x in ds[1:]:
#         if x < chot:
#             trai.append(x)
#         else:
#             phai.append(x)

#     return quicksort(trai) + [chot] + quicksort(phai)
# a = [5, 2, 9, 1, 5, 6,34,12,67]
# print("Dãy sau khi sắp xếp:", quicksort(a))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Hàm in danh sách liên kết
def in_danh_sach(head):
    hien_tai = head
    while hien_tai is not None:
        print(hien_tai.data, end=" -> ")
        hien_tai = hien_tai.next
    print("None")

# Hàm đảo ngược danh sách liên kết
def dao_nguoc_danh_sach(head):
    truoc = None
    hien_tai = head

    while hien_tai is not None:
        ke_tiep = hien_tai.next
        hien_tai.next = truoc
        truoc = hien_tai
        hien_tai = ke_tiep

    return truoc  # Đây là head mới sau khi đảo ngược

# Hàm chính
def main():
    # Tạo danh sách: 1 -> 2 -> 3 -> 4 -> None
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    print("Danh sách ban đầu:")
    in_danh_sach(n1)

    # Đảo ngược danh sách
    head_moi = dao_nguoc_danh_sach(n1)

    print("Danh sách sau khi đảo ngược:")
    in_danh_sach(head_moi)

# Gọi hàm main
if __name__ == "__main__":
    main()



# 



# Lượt thứ i	Dãy số qua từng lượt
# 1	09 15 03 12 22 07  → Pivot: 09, chia: [03 07] + 09 + [15 12 22]
# 2	03 07 09 15 12 22  → Sắp [03 07] với pivot 03 → [03 07]
# 3	03 07 09 15 12 22  → Sắp [15 12 22] với pivot 15 → [12 15 22]
# 4	03 07 09 12 15 22  (Kết quả sau ghép các phần)
# Kết quả	03 07 09 12 15 22