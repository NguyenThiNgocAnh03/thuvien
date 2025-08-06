# 




# h=int(input('mhap vao h:'))
# tn=h-1
# tt=1
# for i in range(h):
#     if i==0:
#         print(' '*tn+'*')
#     elif i<h-1:
#         # print(' '*tn,end='')
#         # print('*',end='')
#         # print(' '*tt,end='')
#         # print('*')
#         # tn=tn-1
#         print(' '*tn+'*'+' '*tt+'*')
#         tt=tt+2
#     else:
#         print((h*2-1)*'*')
#     tn=tn-1




# h=int(input('nhap h:'))
# tn=h
# tt=0
# for i in range(h):
#     if i==0:
#         print(tn*' '+'*')
#     elif i<h-1:
#         print(' '*tn+'*'+' '*tt+'*')
#         tt=tt+1
#         # tn=tn-1
#     else:
#         print(' '*tn+h*'*')
#     tn=tn-1



# h=int(input('nhap h:'))
# tn=h*2-2
# tt=1
# for i in range(h):
#     if i==0:
#         print(' '*tn+'*')
#     elif i<h-1:
#         print(' '*tn+'*'+' '*tt+'*')
#         tt=tt+2
#     else:
#         print(h*'* ')
#     tn=tn-2





# # import math
# n=int(input('nhsp n'))
# a=abs(n)
# print(f'tri tuyet doi cua {n} la {a}')




# a=input('nhap chuoi:')
# b= input('nhap ki tu muon tim:')
# # # c=a.find(b)
# # # if b in a:
# # #     print(f'ki tu {b} co trong chuoi {a} ở vị trí {c}')
# # # else:
        
# # #     print(f'ki tu {b} khong co trong chuoi {a}')
# list=[]
# c=''
# for i in range(len(a)):
#     list.append(i)
#     list.append(list)
#     if a[i]==b:
#         c=c+str(i)+ ','
#         if c.endswith(','):
#            d=c[:-1]
#            print (b, 'có trong chuỗi ở vị trí',d)
#     else:
#         if c=='':
#             print(f'{b} khong co trong chuoi')a
    



    




# n=int(input('nhap  n:'))
# for i in range(n):
#     if i==0:
#         print('*')
#     elif i<n-1:
#         print((i+1)*'*')
#     else:
#         print(n*'*')


# n=input('nhap chuoi')
# print('tong so luong ki tu la ', len(n))





# def trituyetdoi(number):
#     if number<0:
#         number=number*(-1)
#     else:
#         number=number*1
#     return number

# a=int(input('nhap a:'))
# b=trituyetdoi(a)
# print(f'trị tuyệt đối của {a} là {b}')
# print(a,b)


# a=int(input('nhap a:'))
# b=a
# if a<0:
#     b=a*(-1)
# elif a>0:
#     b=a*1
# else:
#     b=b
# print(f'gia tri tuyet doi của {a} la {b}')

# a=int(input('nhap a:'))
# b=abs(a)
# print(f'trị tuyệt đối của {a} là {b} ')



# chuoi=input('nhap chuoi:')
# tim=input('nhap kí tự cần tìm:')
# vitri=-1
# i=0
# while i<len(chuoi):
#     if chuoi[i]==tim:
#         vitri=i
#         print( f'ki tụ {tim} có trong chuoi{chuoi} ở vị trí{vitri}')
#         break
#     else:
#         i=i+1
#         if vitri==-1:
#             print(f'ki tu {tim } khong co trong chuoi')
# for i in range(len(chuoi)):
#     if i <len(chuoi):
#         if chuoi[i]==tim:
#             vitri=i 
#             print(f'ki tu{tim} co trong chuỗi{chuoi} ở vị trí{vitri}')
#             break
#         else:
#             if vitri==-1:
#                 i=i+1
# print('khong co')
            



# a='hello pnv26'
# b=''
# for i in a:
#     b=b+i
# print(b)

# s1='hello'
# s2='PNV27'
# s3=s1
# s4='hello'
# print ( s3 is s1, s4 is s3)
# print(s3==s1,s4 is s1)

# def myFunc ():
#     x=300
#     return(x)
# print(myFunc())
# myFunc()

# a=input('nhap chuoi')
# tim=input('ki tự can tìm')
# dem=0
# for i in range(len(a)):
#     ds.append(i)
#     for i in ds:
#        if ds[i]==tim:
#         print(f'ki tự{tim} có trong chuỗi ở vị trí{len(i)}')
#        else:
#         print(f'ki tự{tim} không có trong chuỗi ở vị trí')


# def timKiTu(chuoi,kiTu):
#     dem=0
#     for i in chuoi:
#         if i==kiTu:
#             dem=dem+1
#     return dem
# print(timKiTu('hello','l'))





# def print_name():
#     # Dòng này để lấy họ và tên, hàm strip() dùng để loại bỏ khoảng trắng đầu tiên và cuối cùng
#     full_name = input("Nhập họ và tên: ").strip()
    
#     # Dòng này dùng để chia họ và tên thành 1 mảng các String
#     name_parts = full_name.split()
    
#     # Kiểm tra nếu tên không đủ định dạng
#     if len(name_parts) < 2:
#         print("Vui lòng nhập đầy đủ họ và tên!")
#         return
    
#     # Tách họ và tên đệm (trừ từ cuối cùng)
#     ho_va_ten_dem = " ".join(name_parts[:-1]).title()
    
#     # Lấy tên (từ cuối cùng)
#     ten = name_parts[-1].title()
    
#     # Viết hoa ký tự đầu của toàn bộ họ và tên
#     full_name_capitalized = full_name.title()
    
#     # In kết quả
#     print(f"Họ và tên đệm: {ho_va_ten_dem}")
#     print(f"Tên của bạn là: {ten}")
#     print(f"Tên đầy đủ của bạn là: {full_name_capitalized}")

# print_name()


# def sum(n):
#     S=0
#     if n==0:
#         S=0
#     else:
#        S=n+sum(n-1)
#     return S
# print(sum(3))

# def Giaithua(n):
#     gt=1
#     if n==1:
#         gt=1
#     else:
#         gt=n*Giaithua(n-1)
#     return gt

# # a=int(input("nhập a: "))
# # print(Giaithua(a))

# def sum(n):
#     S=0
#     if n%2==0:
#         if n==2:
#             S=2
#         else:
#             S=n+sum(n-2)
#     return S
# print(sum(6))

# def sum(n):
#     S=0
#     if n%2!=0:
#         if n==1:
#             S=1
#         else:
#             S=n+sum(n-2)
#     return S
# print(sum(4))

# def sum(n):
#     S=0
#     if n==1:
#         S=1
#     else:

#         S=sum(n-1)+(2*n-1)
#     return S
# print(sum(5))

# def sum(n):
#     if n==2:
#         S=2
#     else:
#         S=sum(n-1)+(2*n)
#     return S
# print(sum(4))

# import array as arr
# so=arr.array('b',[])
# print(so)
# for i in range(5):
#     t=int(input('nhap so thư tư',))




import array as arr 
numbers = arr.array('i',[])
print(numbers)
#Nhập dữ liệu cho mảng
n=int(input('nhap so'))
for j in range(n):
#    t = int(input('nhap so thu %d: ' %(j+1)))
    numbers.append(int(input('nhap so thu %d: ' %(j+1))))
print(numbers)
#Xuất dữ liệu mảng
for i in range(len(numbers)): 
    print(numbers[i])
numbersSum = sum(numbers) 
print('Tổng là',numbersSum)





import array as arr
number=arr.array('i',[])
dem=0
n=int(input('nhập số lượng phần tử:'))
for i in range(n):
    so=int(input('nhập số phần tử:'))
    number.append(so)
print(number)
for j in number:
    if j%1==0 and j%j==0 and j%2!=0 and j!=1:
        print(f'{j} là số nguyên tố')
        dem=dem+1
print (f'trong day so nguyen có {dem} số nguyên tố')





# import array as arr
# A=arr.array('B',[])
# m=int(input('nhập số lượng phần tử:'))
# for i in range(m):
#     soo=int(input('nhập số phần tử:'))
#     A.append(soo)
# B=arr.array('b',[])
# f=int(input('nhập số lượng phần tử:'))
# for i in ran(ge(f):
#     s=int(input('nhập số phần tử:'))
#     B.append(s)
# C=str(A)+str(B)
# print(C)
# import array as arr
# number = arr.array("i",[1,2,3]) 
# number.extend([5,7,9,11,13,15]) 
# number.insert(4,50) 
# print(number)
# # Kết quả: array('i',[1,2,3,5,50,7,9,11,13,15])



# import array as arr
# A=arr.array('i',[])
# n=int(input('nhập số:'))
# for i in range(n):
#     so=int(input('nhap pahn tư:'))
#     A.append(so)
# for j in A:
#     for i in range(len(A)/2):
        
