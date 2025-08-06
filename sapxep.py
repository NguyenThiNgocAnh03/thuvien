# import sys
# A=[]
# a=int(input("nhập số:"))
# for b in range (a):
#     num=int(input("nhập phần tử:"))
#     A.append(num)
# for i in range(len(A)):
#     min=i
#     for j in range(i+1,len(A)):
#         if A[min]>A[j]:
#             min=j
#             A[i],A[min]=A[min],A[i]
# print(A)


# def insertSoft(num):
#     for i in range(1,len(num)):
#         tam=num[i]
#         j=i-1
#         while j >= 0 and tam < num[j]:
#             num[j+1] = num[j]
#             j-=1
#         num[j+1] = tam
#     return num
# A=[]
# a=int(input("nhập số:"))
# for b in range (a):
#     num=int(input("nhập phần tử:"))
#     A.append(num)
# print(insertSoft(A))


# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr 
# A=[]
# a=int(input("nhập số:"))
# for b in range (a):
#     num=int(input("nhập phần tử:"))
#     A.append(num)
# print(bubbleSort(A))




# cách 2
# import array as arr
# arr = arr.array('i',[])
# n=int(input(' so luong phan tu  :   '))
# for j in range(n):
#     arr.append(int(input('nhap so thu %d: ' %(j+1))))
# print(arr)
# def bubbleSort(arr): 
#     n = len(arr) 
#     for i in range(n): 
#         for j in range(0, n-i-1): 
#             if arr[j] > arr[j+1] : 
#                 arr[j], arr[j+1] = arr[j+1], arr[j] 

# bubbleSort(arr)
# print("xuất mảng ",arr)

import sys
A=[]
a=int(input("nhập số:"))
for b in range (a):
    num=int(input("nhập phần tử:"))
    A.append(num)
for i in range(len(A)):
    max=i
    for j in range(i+1,len(A)):
        if A[max]<A[j]:
            max=j
            A[i],A[max]=A[max],A[i]
print(A)


def insertSoft(num):
    for i in range(1,len(num)):
        tam=num[i]
        j=i-1
        while j >= 0 and tam > num[j]:
            num[j+1] = num[j]
            j-=1
        num[j+1] = tam
    return num
A=[]
a=int(input("nhập số:"))
for b in range (a):
    num=int(input("nhập phần tử:"))
    A.append(num)
print(insertSoft(A))


def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr 
A=[]
a=int(input("nhập số:"))
for b in range (a):
    num=int(input("nhập phần tử:"))
    A.append(num)
print(bubbleSort(A))


