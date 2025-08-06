# numList = ['1','2','3']
# str=','
# print(numList)
# print(str.join(numList))
# a='PNV27A is number one'
# b=a.split()
# print(b)
# print(' '.join(b))
# a='      tôi yêu bạn    '
# b=a.strip()
# print(b)

# def tinhDiem(solungmonhoc):
#     ds=[]
#     S=0
#     soluongmonhoc=int(input('Nhập số lượng môn học cần tính DTB:'))
#     for i in range(1,soluongmonhoc):
#         a=int(input(f'Nhập điểm môn học {i}:'))
#         b=float(input(f'Nhập điểm hệ số{i}'))
#         ds.append(a)
#         ds.append(b)
#     if a>10 or a<0:
#         print('vui lòng nhập lại')
#     for j in ds:
#         S=(S+j)/len(ds)
#     return S
# print(tinhDiem(2))
# def xemLuong(luong):
#     i=1
#     ds=[]
#     while i<=luong:
#         dsluong=int(input(f'nhập lương của người thứ {i}:'))
#         ds.append(dsluong)
#         i=i+1
#     for k in range(len(ds)):
#         for j in range(len(ds)):
#             if ds[k]>ds[j]:
#                 ds[k],ds[j]=ds[j],ds[k]
#     return ds
# print(xemLuong(3))
# def tinhdtb(dsdiem,dsheso,so):
#     j=0
#     tongdiem=0
#     dtb=0.0
#     for i in range (len(dsdiem)):
#             while j<len(dsheso):
#                 tongdiem=tongdiem+(dsdiem[i]*dsheso[j])
#                 j=j+1
#                 break
#     dtb=dtb+(tongdiem/so)
#     return dtb
#         sl=int(input("Hãy nhập số lượng môn học:"))
#         dsdiem=[]
#         dsheso=[]
#         i=1    
#         so=0.0
#         while i<=sl:
#             mon=float(input(f"Nhập điểm của môn học {i}:"))
#             heso=float(input(f"Nhập hệ số của môn học {i}:"))
#             so=so+heso
#             dsdiem.append(mon)
#             dsheso.append(heso)
#             i=i+1
#         dtb=Functions.tinhdtb(dsdiem,dsheso,so) 
#         print(f"Số môn học là:{sl}")   
#         print(f"Tổng hệ số môn học là:{so}")
#         print(f"Điểm trung bình của học sinh là:{dtb:.2f}")
# def tinhDiemHocSinh(slmonhoc):
#     dsdiem=[]
#     dsheso=[]
#     so=0.0
#     tongdiemheso=0
#     tongheso=0
#     for i in range (1,slmonhoc+1):    
#         diem=float(input(f"Nhập điểm của môn học {i} (0-10):"))
#         while (diem<0)or(diem>10):
#             print("Bạn đã nhập sai yêu cầu! Hãy nhập lại")
#             diem=float(input(f"Nhập điểm của môn học {i} (0-10):"))            
#         heso=float(input(f"Nhập hệ số của môn học {i}:"))
#         while (heso not in (1,1.5,2,2.5,3)):
#             print("Bạn đã nhập sai yêu cầu! Hãy nhập lại")
#             heso=float(input(f"Nhập hệ số của môn học {i}:"))
#         so=so+heso 
#         dsheso.append(heso)                
#         dsdiem.append(diem)
#         tongdiemheso += diem * heso
#         tongheso += heso
#     diemTrungBinh = tongdiemheso / tongheso
#     return diemTrungBinh



# soluong=int(input('nhâp số lượng số nguyên:'))
# ds=[]
# songuyento=[]
# for i in range(1,soluong+1):
#     so=int(input(f'nhập số thứ {i}:'))
#     ds.append(so)
# for i in range(len(ds)-1):
#     for j in range(len(ds)-i-1):
#         if ds[j] > ds[j + 1]:  
#                 temp = ds[j]
#                 ds[j] = ds[j + 1]
#                 ds[j + 1] = temp
# print(ds)
# for k in ds:
#     if k%k==0 and k%1==0 and k%2!=0 and k != 1:
#         print(f'{k} là số nguyên tố ')







          

    
    
        
