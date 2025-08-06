class Node:
    def __init__(self, data=None):
        self.data = data  
        self.next = None
class SLinkedList:
    def __init__(self):
        self.head = None
class sv:
    def __init__(self, so):
        self.so=so
list=SLinkedList()
a=int(input("nhap so:"))
arr=[]
low=0
for i in range(a):
	so=int(input("nhap phan tu:"))
	arr.append(so)
x=int(input("nhap so can tim:"))
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
            print(current.data)
            current = current.next

def sort(self):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            index = current.next
            while index is not None:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
                current = current.next

def binary_search(arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return binary_search(arr, low, mid - 1, x)
            else:
                return binary_search(arr, mid + 1, high, x)
        else:
            return -1


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
            print(current.data, end=" ")
            current = current.next
        print()

    def sort(self):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            index = current.next
            while index is not None:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next

    def to_array(self):
        arr = []
        current = self.head
        while current is not None:
            arr.append(current.data)
            current = current.next
        return arr

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

# ======= MAIN PROGRAM =======
list_sv = SLinkedList()
n = int(input("Nhap so luong phan tu: "))
for i in range(n):
    so = int(input(f"Nhap phan tu thu {i+1}: "))
    list_sv.append(so)

print("Danh sach da nhap:")
list_sv.listprint()

print("Dang sap xep danh sach...")
list_sv.sort()

print("Danh sach sau khi sap xep:")
list_sv.listprint()

x = int(input("Nhap gia tri can tim: "))
arr = list_sv.to_array()
index = binary_search(arr, 0, len(arr)-1, x)

if index != -1:
    print(f"Tim thay {x} tai vi tri index {index} trong danh sach sap xep.")
else:
    print(f"Khong tim thay {x} trong danh sach.")