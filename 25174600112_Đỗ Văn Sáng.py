#bai 1
def tinh_luy_thua():
    a = int(input("Nhập co số a:"))
    b = int(input("Nhập co số b:"))
    ket_qua = 1
    for i in range(b):
        ket_qua *= a
    print(f"{a}^{b} = {ket_qua}")
tinh_luy_thua()

#bai 2
def in_fibonacci():
    a, b = 0, 1
    for i in range(10):
        print(a, end=" ")
        a, b = b, a + b
in_fibonacci()

#bai 3
#a
def nhap_so():
    n = int(input("Nhập số nguyên dương n: "))
    return n
def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n = nhap_so()
if so_nguyen_to(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố")

#b
def nhap_so():
    n = int(input("Nhập số nguyên dương n: "))
    return n
def so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong = tong + i
    if tong == n:
        return True
    else:
        return False
n = nhap_so()
if so_hoan_hao(n):
    print(n, "là số hoàn hảo")
else:
    print(n, "không phải số hoàn hảo")

#c
def doi_xung(n):
    tam = n
    dao = 0  
    for i in range(len(str(n))):
        so_du = n % 10
        dao = dao * 10 + so_du
        n = n // 10
    if tam == dao:
        return True
    else:
        return False
dem = 0
for i in range(1, 1000):
    if doi_xung(i):
        print(f"{i:5}", end="")
        dem = dem + 1
        if dem % 15 == 0:
            print()

#bai 4
#a
def tinh_P(n):
    tich = 1
    for i in range(n + 1):
        tich = tich * (2 * i + 1)
    return tich
n = int(input("Nhập n: "))
print("P(n) =", tinh_P(n))

#b
def tinh_S(n):
    tong = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            tong = tong + i
        else:
            tong = tong - i
    
    return tong
n = int(input("Nhập n: "))
print("S(n) =", tinh_S(n))

#c
def tinh_S(n):
    tong = 0
    for i in range(1, n + 1):
        tong_con = 0
        for j in range(1, i + 1):
            tong_con = tong_con + j       
        tong = tong + tong_con 
    return tong
n = int(input("Nhập n: "))
print("S(n) =", tinh_S(n))

#d
def tinh_P(x, y):
    tich = 1    
    for i in range(y):
        tich = tich * x    
    return tich
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
print("P(x,y) =", tinh_P(x, y))

#bai 5
def nhap_ky_tu():
    ky_tu = input("Nhập ký tự (ESC để thoát): ")
    return ky_tu
while True:
    kt = nhap_ky_tu()
    if kt == "ESC":
        break
    if len(kt) == 1:
        print("Mã ASCII của", kt, "là", ord(kt))
    else:
        print("Chỉ nhập 1 ký tự")
print("Kết thúc chương trình")