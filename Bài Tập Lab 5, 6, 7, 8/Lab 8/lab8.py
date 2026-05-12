#bai 1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
for i in range(2, 1000):
    if is_prime(i) and is_prime(i+2):
        print(i, "và", i+2)

#bai 2
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
print(factorial(5))

#bai 3
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Bài 8.3: Hoán vị và tổ hợp
def permutation(n, r):
    if r > n or r < 0:
        return 0
    return factorial(n) // factorial(n - r)

def combination(n, r):
    if r > n or r < 0:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

# Chạy thử
n = int(input("Nhập n: "))
r = int(input("Nhập r: "))
print(f"P({n},{r}) =", permutation(n, r))
print(f"C({n},{r}) =", combination(n, r))

#bai 4
def cubesum(n):
    s = 0
    for ch in str(n):
        d = int(ch)
        s += d * d * d
    return s
print(cubesum(123))

#bai 5
def cubesum(n):
    total = 0
    n_abs = abs(n)  # xử lý số âm nếu có
    for ch in str(n_abs):
        digit = int(ch)
        total += digit ** 3
    return total

# Bài 8.5: Kiểm tra số Armstrong
def isArmstrong(n):
    if n < 0:
        return False
    return cubesum(n) == n

# Xuất danh sách số Armstrong < 1000
print("Các số Armstrong nhỏ hơn 1000:")
for i in range(1000):
    if isArmstrong(i):
        print(i, end=" ")
print()

# Kiểm tra một số cụ thể
num = int(input("Nhập số để kiểm tra: "))
if isArmstrong(num):
    print(num, "là số Armstrong")
else:
    print(num, "không là số Armstrong")

#bai 6

def sumPdivisors(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s
print(sumPdivisors(12))

#bai 7
def sumPdivisors(n):
    if n <= 1:
        return 0
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

# Bài 8.7: Kiểm tra cặp số amicable
def isAmicable(a, b):
    return sumPdivisors(a) == b and sumPdivisors(b) == a
print(isAmicable(220, 284))

# Chạy thử
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
if isAmicable(a, b):
    print(f"{a} và {b} là cặp số amicable")
else:
    print(f"{a} và {b} không là cặp số amicable")

# Tìm các cặp amicable nhỏ hơn 1000
print("\nCác cặp amicable nhỏ hơn 1000:")
for i in range(2, 1000):
    j = sumPdivisors(i)
    if j > i and j < 1000 and sumPdivisors(j) == i:
        print(f"({i}, {j})")

#bai 8
def filter_even_odd(arr):
    even = []
    odd = []
    for x in arr:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    return even, odd
arr = [1, 2, 3, 4, 5]
even, odd = filter_even_odd(arr)
print("Chẵn:", even, "Lẻ:", odd)

#bai 9
def map_cube(arr):
    result = []
    for x in arr:
        result.append(x**3)
    return result
print(map_cube([1, 2, 3]))

#bai 10
arr = [1, 2, 3, 4, 5]
even_cubes = []
odd_squares = []
for x in arr:
    if x % 2 == 0:
        even_cubes.append(x**3)
    else:
        odd_squares.append(x**2)
print("Lập phương chẵn:", even_cubes)
print("Bình phương lẻ:", odd_squares)