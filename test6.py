# import tkinter as tk
# window = tk.Tk()
# window.geometry("800x600")
# window.resizable(False,False)
# window.update_idletasks()
# window.mainloop()
# window = tk.Tk()
# button = tk.Button(master = window, text="Đăng Nhập", font=("Arial Bold",12))
# button.pack()
# window.mainloop()

# import tkinter as tk
# window = tk.Tk()
# width = 800
# height = 600
# window.resizable(False,False)
# x = ( window.winfo_screenwidth()-width//2)
# y= ( window.winfo_screenheight()-height//2)
# window.geometry(f"{width}x{height}+{x}+{y}")
# window.update_idletasks()
# window.title("Demo Frame")
# frm_1= tk.Frame(master=window, width=400,background="royalblue")
# frm_1.pack(side="left",fill="y")
# frm_2=tk.Frame(master=window,width=400,background="#2E2E2E")
# frm_2.pack(side="left ", fill="y")





# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class Stack:
#     def __init__(self):
#         self.root = None
    
#     def empty(self):
#         if self.root is None:
#             return True
    
#     def push(self, data):
#         new = Node(data)
#         new.next = self.root
#         self.root = new
#     def pop(self):
#         if (self.empty()):
#             return 'Stack rong'
#         temp = self.root
#         self.root = self.root.next
#         return temp.data
# # Giải phóng bộ nhớ
    
# stack = Stack()
# for i in range(3):
#     temp = input("Nhập phần tử:")
#     stack.push(temp)
# for i in range(3):
#     print(stack.pop(), end=' ')
# class Queue:  
#     def __init__(self): 
#         self.s1 = [] 
#         self.s2 = [] 
  
#     def enQueue(self, x):  
#         while len(self.s1) != 0:  
#             self.s2.append(self.s1[-1])  
#             self.s1.pop()  
#         self.s1.append(x)   
#         while len(self.s2) != 0:  
#             self.s1.append(self.s2[-1])  
#             self.s2.pop()  
#     def deQueue(self):  
#         if len(self.s1) == 0:  
#             print("Q rỗng")   
#         x = self.s1[-1]  
#         self.s1.pop() 





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def is_empty(self):
        return self.top is None
stack = Stack()
a=int(input("nhập số:"))
for i in range(a):
    numbers = int(input(f"nhập số nguyên{i+1}:"))
    stack.push(numbers)
total = 0
while not stack.is_empty():
    total += stack.pop()

print("Tổng:", total)



# #queue
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Queue:
#     def __init__(self):
#         self.front = self.rear = None

#     def enqueue(self, data):
#         new_node = Node(data)
#         if self.rear is None:
#             self.front = self.rear = new_node
#             return
#         self.rear.next = new_node
#         self.rear = new_node

#     def dequeue(self):
#         if self.front is None:
#             return None
#         dequeued_node = self.front
#         self.front = self.front.next
#         if self.front is None:
#             self.rear = None
#         return dequeued_node.data

#     def is_empty(self):
#         return self.front is None

# # Khởi tạo Queue và thêm các số
# queue = Queue()
# for num in numbers:
#     queue.enqueue(num)

# # Tính tổng bằng cách dequeue các phần tử
# total = 0
# while not queue.is_empty():
#     total += queue.dequeue()

# print("Tổng:", total)