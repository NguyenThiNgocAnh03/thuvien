# import array as arr
# arr = arr.array('i',[])
# n = int(input("nhập số phần tử :" ))
# for i in range (n):
#     arr.append(int(input('nhập phần tử thứ %d:' %(i+1))))
# x = 10
# def search(arr, x):
# 	for i in range(len(arr)):
# 		if arr[i] == x:
# 			return i
	
# 	return -1
# print (search(arr, x))

# find bằng nhị phân
def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0
	dem=0
	while low <= high:
		dem=dem+1
		mid = (high + low) // 2
		if arr[mid] < x:
			low = mid + 1
		elif arr[mid] > x:
			high = mid - 1
		else:
			print(f"ds lặp {dem} lần")
			return (f'số {x} được tìm thấy ở vị trí {mid}')
	return -1
a=int(input("nhap so:"))
arr=[]
for i in range(a):
	so=int(input("nhap phan tu:"))
	arr.append(so)
x=int(input("nhap so can tim:"))
print(arr)
print(binary_search(arr,x))
# # find bằng nhị phân đệ quy
# def binary_search(arr, low, high, x):
# 	if high >= low:
# 		mid = (high + low) // 2
# 		if arr[mid] == x:
# 			return mid
# 		elif arr[mid] > x:
# 			return binary_search(arr, low, mid - 1, x)
# 		else:
# 			return binary_search(arr, mid + 1, high, x)
# 	else:
# 		return -1
# a=int(input("nhap so:"))
# arr=[]
# low=0
# dem=0
# for i in range(a):
# 	so=int(input("nhap phan tu:"))
# 	arr.append(so)
# x=int(input("nhap so can tim:"))
# print(arr)
# print(search(arr,x))

