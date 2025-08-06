a=int(input("nhập số:"))
mode=[]
dem=[]
for i in range(a):
    so=int(input("nhập phần tử:"))
    mode.append(so)
for i in range (len(mode)):
    count=0
    for j in range(len(mode)):
        if mode[i] == mode[j]:
            count+=1
        dem.append(count)
        max=dem[0]
    for g in dem:
        if g>max:
            max=g
    modee=[]
    for i in range(len(mode)):
        if dem[i]==max and mode[i] not in modee:
            modee.append(mode[i])
print("mode của ds là",modee)   



#     for f in freq:
#         if f > max_freq:
#             max_freq = f

#     # Tìm tất cả các phần tử có tần số lớn nhất
#     cac_mode = []
#     for i in range(len(arr)):
#         if freq[i] == max_freq and arr[i] not in cac_mode:
#             cac_mode.append(arr[i])

#     # Kiểm tra điều kiện tồn tại duy nhất 1 mode
#     if len(cac_mode) == 1:
#         print("Mode của tập hợp là:", cac_mode[0])
#     else:
#         print("Tập hợp không có mode")

# # Gọi hàm chính
# tim_mode_khong_dung_thu_vien()