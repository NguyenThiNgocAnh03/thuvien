def tim_so_khong_trung_lap(number):
    ds = []
    for x in number:
        if number.count(x) == 1:
            ds.append(x)
    return ds
print(tim_so_khong_trung_lap([3,4,5,4,3]))