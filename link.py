class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def dao_nguoc_danh_sach(head):
    truoc = None
    hien_tai = head

    while hien_tai is not None:
        ke_tiep = hien_tai.next       # Lưu node kế tiếp
        hien_tai.next = truoc         # Đảo chiều liên kết
        truoc = hien_tai              # Di chuyển con trỏ 'truoc'
        hien_tai = ke_tiep            # Di chuyển con trỏ 'hien_tai'

    return truoc  # 'truoc' chính là head mới sau khi đảo ngược
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c

# Hàm in danh sách
def in_danh_sach(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

print("Trước khi đảo:")
in_danh_sach(a)

# Đảo ngược
head_moi = dao_nguoc_danh_sach(a)

print("Sau khi đảo:")
in_danh_sach(head_moi)