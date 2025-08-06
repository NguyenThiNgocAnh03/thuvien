def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:        
            break
    array[start], array[high] = array[high], array[start]
    return high
def partition(arr, low, high):
	i = (low-1)		 # chỉ số của phần tử nhỏ hơn
	pivot = arr[high]	 # trục

	for j in range(low, high):

		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)
def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
		# pi là chỉ mục phân vùng, 
                    #arr [pi] hiện ở đúng vị trí
		pi = partition(arr, low, high)
		# Sắp xếp riêng biệt các phần tử trước
                     # phân vùng và sau phân vùng
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

arr = [34,12,65,78,13,23,95]

quickSort(arr, 0, len(arr) - 1)
print("Sorted array using Hoare partition:", arr)