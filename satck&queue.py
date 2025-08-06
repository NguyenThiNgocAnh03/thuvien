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
#         list = SLinkedList()
#         list.headval = Node("Mon")
#         e2 = Node("Tue")
#         e3 = Node("Wed")
#         list.headval.nextval = e2
#         e2.nextval = e3
#         list.AtBegining("Sun")
#         list.listprint()

class Node:
    def __init__(self, data=None):
        self.data = data  # Lưu dữ liệu sinh viên (mã số, họ tên, điểm, lớp)
        self.next = None  # Con trỏ trỏ đến phần tử tiếp theo

class LinkedList:
    def __init__(self):
        self.head = None  # Con trỏ đầu danh sách

    def append(self, new_data):
        """Thêm sinh viên vào cuối danh sách liên kết"""
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def Print(self):
        """In danh sách sinh viên"""
        temp = self.head
        if temp is None:
            print("Danh sách trống!")
            return
        
        print("\nDanh sách sinh viên:")
        print(f"{'MSSV':<10} {'Họ tên':<15} {'Điểm':<5} {'Lớp':<10}")
        print("-" * 40)
        while temp:
            print(f"{temp.data[0]:<10} {temp.data[1]:<15} {temp.data[2]:<5} {temp.data[3]:<10}")
            temp = temp.next

# Chương trình chính
if __name__ == "__main__":
    sv = LinkedList()

    # Thêm dữ liệu cứng vào danh sách
    sv.append(['1A', 'Tuong', 9.0, '12/12'])
    sv.append(['1B', 'Bao', 8.0, '10/12'])
    sv.append(['1C', 'Gia Huy', 7.0, '11/12'])

    # Hiển thị danh sách sinh viên ban đầu
    sv.Print()

    # Thêm sinh viên nhập từ bàn phím
    for i in range(2):  # Nhập 2 sinh viên mới (bạn có thể thay đổi số này)
        print(f"\nNhập thông tin sinh viên thứ {i+1}:")
        ms = input("Mã số: ")
        hoten = input("Họ tên: ")
        diemso = float(input("Điểm: "))
        lop = input("Lớp: ")
        sv.append([ms, hoten, diemso, lop])

    # Hiển thị danh sách sinh viên sau khi nhập thêm
    sv.Print()

#bài 1
class Node:
    
    def __init__(self, data=None):
        self.data = data  # Dữ liệu của node
        self.next = None  # Con trỏ trỏ đến node tiếp theo

class Stack:
    def __init__(self):
        self.top = None  # Node đỉnh của stack

    def push(self, value):
        """Thêm phần tử vào stack"""
        new_node = Node(value)
        new_node.next = self.top  # Liên kết node mới với node hiện tại
        self.top = new_node  # Cập nhật đỉnh stack

    def pop(self):
        """Lấy phần tử ra khỏi stack"""
        if self.is_empty():
            return None
        popped_value = self.top.data
        self.top = self.top.next  # Di chuyển con trỏ top xuống node kế tiếp
        return popped_value

    def is_empty(self):
        """Kiểm tra stack có rỗng không"""
        return self.top is None

    def print_stack(self):
        """In toàn bộ stack theo thứ tự từ đỉnh xuống"""
        temp = self.top
        if temp is None:
            print("Stack rỗng!")
            return

        print("\nDãy số theo thứ tự ngược (LIFO):")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Chương trình chính
if __name__ == "__main__":
    stack = Stack()

    # Nhập số lượng phần tử
    n = int(input("Nhập số lượng phần tử: "))

    # Nhập dãy số và đẩy vào stack
    for i in range(n):
        num = int(input(f"Nhập số thứ {i+1}: "))
        stack.push(num)

    # Xuất dãy số theo thứ tự ngược
    stack.print_stack()
