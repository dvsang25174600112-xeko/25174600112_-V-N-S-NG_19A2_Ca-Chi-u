#bai 1
n = int(input("Nhập số nguyên dương: "))
binary = ""
if n == 0:
    binary = "0"
else:
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
print("Dạng nhị phân:", binary)
#bai 2
str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")
common = ""
for ch in str1:
    if ch in str2 and ch not in common:
        common += ch
print("Ký tự chung:", common)
#bai 3
text = input("Nhập văn bản: ").split()
keyword = input("Nhập từ khóa: ")
positions = []
for i in range(len(text)):
    if text[i] == keyword:
        positions.append(i + 1)
print("Vị trí xuất hiện của từ khóa:", positions)
freq = {}
for word in text:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
max_word = ""
max_count = 0
for word, count in freq.items():
    if count > max_count:
        max_count = count
        max_word = word
print("Từ xuất hiện nhiều nhất:", max_word, "với", max_count, "lần")
#bai 4
s = input("Nhập xâu: ")
digits = ""
for ch in s:
    if ch.isdigit():
        digits += ch
if digits == "":
    print("Không có chữ số nào")
else:
    num = int(digits)
    if num < 2:
        print(num, "không là số nguyên tố")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, "là số nguyên tố")
        else:
            print(num, "không là số nguyên tố")
#bai 5
s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
result = ""
i = 0
while i < len(s1) or i < len(s2):
    if i < len(s1):
        result += s1[i]
    result += "-"
    if i < len(s2):
        result += s2[i]
    result += "-"
    i += 1
result = result[:-1] 
print("Kết quả trộn:", result)
#bai 6
s = input("Nhập xâu: ")
total = len(s)
special = {}
for ch in s:
    if not ch.isalnum():
        if ch in special:
            special[ch] += 1
        else:
            special[ch] = 1
for ch, count in special.items():
    percent = (count / total) * 100
    print(f"'{ch}' xuất hiện {count} lần, chiếm {percent:.2f}%")
#bai 7
s = input("Nhập xâu: ")
lower = upper = digit = special = 0
for ch in s:
    if ch.islower():
        lower += 1
    elif ch.isupper():
        upper += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1
print("In thường:", lower)
print("In hoa:", upper)
print("Chữ số:", digit)
print("Ký tự đặc biệt:", special)
#bai 8
s = input("Nhập xâu (>10 ký tự): ")
if len(s) > 10:
    print("Từ vị trí 2 đến 8:", s[1:8])
    print("5 ký tự từ vị trí 5:", s[4:9])
    print("3 ký tự cuối:", s[-3:])
    print("Chữ hoa:", s.upper())
    print("Chữ thường:", s.lower())
    print("Đảo ngược:", s[::-1])
#bai 9
def min_edit_distance(a, b):
    m, n = len(a), len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

s1 = input("Nhập chuỗi gốc: ")
s2 = input("Nhập chuỗi đích: ")
print("Số bước biến đổi tối thiểu:", min_edit_distance(s1, s2))
#bai 10
s = input("Nhập xâu: ")
result = ""
for ch in s:
    if ch != " ":
        result += ch
print("Xâu không khoảng trắng:", result)