#bai 1
n = int(input("Nhập số phần tử: "))
arr = []
for i in range(n):
    arr.append(int(input("Nhập số: ")))
sum_even = sum_odd = 0
for x in arr:
    if x % 2 == 0:
        sum_even += x
    else:
        sum_odd += x
print("Tổng chẵn:", sum_even)
print("Tổng lẻ:", sum_odd)
#bai 2
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def is_perfect(x):
    s = 0
    for i in range(1, x):
        if x % i == 0:
            s += i
    return s == x

n = int(input("Nhập số phần tử: "))
arr = []
for i in range(n):
    arr.append(int(input("Nhập số: ")))
result = []
for x in arr:
    if is_prime(x) or is_perfect(x):
        result.append(x)
print("Kết quả:", result)
#bai 3
n = int(input("Nhập số phần tử: "))
arr = []
for i in range(n):
    arr.append(float(input("Nhập số: ")))
max_val = arr[0]
min_val = arr[0]
for x in arr:
    if x > max_val:
        max_val = x
    if x < min_val:
        min_val = x
print("Max:", max_val, "Min:", min_val)
#bai 4
n = int(input("Nhập n: "))
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for i in range(2, n)]
print(fib[:n])
#bài 5
def is_prime(x):
    if x < 2: return False
    for i in range(2, x):
        if x % i == 0: return False
    return True
primes = [x for x in range(2, 100) if is_prime(x)]
print(primes)
#bai 6
n = int(input("Nhập số phần tử: "))
arr = []
for i in range(n):
    arr.append(int(input("Nhập số: ")))
diff = arr[1] - arr[0]
is_ap = True
for i in range(2, n):
    if arr[i] - arr[i-1] != diff:
        is_ap = False
        break
if is_ap:
    print("Là cấp số cộng")
else:
    print("Không là cấp số cộng")
#bai 7
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input(f"Nhập a[{i}][{j}]: ")))
    matrix.append(row)
total = 0
for i in range(m):
    for j in range(n):
        total += matrix[i][j]
print("Tổng ma trận:", total)
#bai 8
m1 = int(input("Ma trận 1 - số hàng: "))
n1 = int(input("Ma trận 1 - số cột: "))
m2 = int(input("Ma trận 2 - số hàng: "))
n2 = int(input("Ma trận 2 - số cột: "))
if n1 != m2:
    print("Không thể nhân ma trận")
else:
    A = []
    for i in range(m1):
        row = []
        for j in range(n1):
            row.append(int(input(f"A[{i}][{j}]: ")))
        A.append(row)
    B = []
    for i in range(m2):
        row = []
        for j in range(n2):
            row.append(int(input(f"B[{i}][{j}]: ")))
        B.append(row)
    C = []
    for i in range(m1):
        row = [0]*n2
        C.append(row)
    for i in range(m1):
        for j in range(n2):
            s = 0
            for k in range(n1):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    print("Ma trận tích:")
    for row in C:
        print(row)
# bai 9
n = int(input("Nhập cấp ma trận: "))
A = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input(f"A[{i}][{j}]: ")))
    A.append(row)
T = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(A[j][i])
    T.append(row)
print("Ma trận chuyển vị:")
for row in T:
    print(row)
symmetric = True
for i in range(n):
    for j in range(n):
        if A[i][j] != T[i][j]:
            symmetric = False
            break
if symmetric:
    print("Ma trận đối xứng")
else:
    print("Ma trận không đối xứng")
#bai 10
def det2x2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]
def inverse2x2(m):
    d = det2x2(m)
    if d == 0:
        return None
    return [[m[1][1]/d, -m[0][1]/d], [-m[1][0]/d, m[0][0]/d]]
n = int(input("Nhập cấp ma trận (chỉ hỗ trợ 2): "))
if n == 2:
    A = []
    for i in range(2):
        row = []
        for j in range(2):
            row.append(float(input(f"A[{i}][{j}]: ")))
        A.append(row)
    inv = inverse2x2(A)
    if inv is None:
        print("Ma trận không khả nghịch")
    else:
        print("Ma trận nghịch đảo:")
        for row in inv:
            print(row)
else:
    print("Chương trình chỉ hỗ trợ ma trận 2x2")