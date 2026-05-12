#bai 1
N = int(input("Nhập N: "))
d = {}
for x in range(1, N+1):
    d[x] = x**3
print(d)

#bai 2
students = {}
n = int(input("Số sinh viên: "))
for i in range(n):
    name = input("Tên: ")
    score = int(input("Điểm: "))
    students[name] = score
grades = {}
for name, score in students.items():
    if score >= 90:
        grades[name] = 'A'
    elif score >= 80:
        grades[name] = 'B'
    elif score >= 70:
        grades[name] = 'C'
    elif score >= 60:
        grades[name] = 'D'
    else:
        grades[name] = 'F'
print(grades)
#bai 3
students = {}
n = int(input("Số sinh viên: "))
for i in range(n):
    name = input("Tên sinh viên: ")
    score = float(input("Điểm: "))
    students[name] = score
grades = {}
for name, score in students.items():
    if score >= 90:
        grades[name] = "A"
    elif score >= 80:
        grades[name] = "B"
    elif score >= 70:
        grades[name] = "C"
    elif score >= 60:
        grades[name] = "D"
    else:
        grades[name] = "F"
count_grade = {}
for g in grades.values():
    if g in count_grade:
        count_grade[g] += 1
    else:
        count_grade[g] = 1

print("Phân loại học lực từng sinh viên:", grades)
print("Số lượng theo từng mức:", count_grade)
#bai 4
text = input("Nhập văn bản: ").lower()
punctuation = ".,!?;:()\"'"
for p in punctuation:
    text = text.replace(p, " ")
words = text.split()
freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
print(freq)

#bai 5
text = input("Nhập đoạn văn bản: ").lower()
cleaned = ""
for ch in text:
    if ch.isalpha() or ch == " ":
        cleaned += ch

words = cleaned.split()

freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
max_word = ""
max_count = 0
min_word = ""
min_count = float("inf")

for w, c in freq.items():
    if c > max_count:
        max_count = c
        max_word = w
    if c < min_count:
        min_count = c
        min_word = w

print("Từ xuất hiện nhiều nhất:", max_word, "với", max_count, "lần")
print("Từ xuất hiện ít nhất:", min_word, "với", min_count, "lần")
#bai 6
inventory = {
    'gold': 500,
    'backpack': ['xà beng', 'súng', 'băng gạc']
}
inventory['pocket'] = ['đá lửa', 'dây thừng']
inventory['gold'] += 50
print(inventory)

#bai 7
#bài 7 và 6 gộp lại để có dữ liệu đầy đủ
inventory = {
    'gold': 500,
    'backpack' :['xà beng', 'súng', 'băng gạc', 'dao', 'đèn pin']
}
print("=== TRƯỚC KHI XỬ LÝ ===")
print("Túi đồ (backpack):", inventory['backpack'])
print("Vàng:", inventory['gold'])
# Bổ sung khóa 'pocket' với danh sách vật phẩm
inventory['pocket'] = ['đá lửa', 'dây thừng', 'la bàn']
print("\n=== SAU KHI THÊM POCKET ===")
print("Túi hông (pocket):", inventory['pocket'])
inventory['gold'] += 50
print("Vàng sau khi cập nhật:", inventory['gold'])
# -------------------- Bài 7.7 --------------------
# Sắp xếp danh sách vật phẩm trong backpack theo thứ tự từ điển
print("\n=== TRƯỚC KHI SẮP XẾP ===")
print("Backpack (chưa sắp xếp):", inventory['backpack'])
# Sắp xếp (dùng thuật toán nổi bọt đơn giản cho sinh viên năm nhất)
backpack_list = inventory['backpack']
n = len(backpack_list)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if backpack_list[j] > backpack_list[j + 1]:
            # Đổi chỗ
            backpack_list[j], backpack_list[j + 1] = backpack_list[j + 1], backpack_list[j]

print("Backpack (sau khi sắp xếp):", inventory['backpack'])
# Loại bỏ một vật phẩm cụ thể
item_to_remove = 'súng'
if item_to_remove in inventory['backpack']:
    inventory['backpack'].remove(item_to_remove)
    print(f"\nĐã loại bỏ '{item_to_remove}' khỏi backpack")
else:
    print(f"\nKhông tìm thấy '{item_to_remove}' trong backpack")
print("\n=== KẾT QUẢ CUỐI CÙNG ===")
print("Từ điển inventory:", inventory)
print("Backpack sau khi xử lý:", inventory['backpack'])
print("Pocket:", inventory['pocket'])
print("Vàng:", inventory['gold'])

# bài 8
stock = {}
price = {}
n = int(input("Số mặt hàng: "))
for i in range(n):
    item = input("Tên hàng: ")
    stock[item] = int(input("Số lượng: "))
    price[item] = int(input("Đơn giá: "))
total = 0
for item in stock:
    total += stock[item] * price[item]
print("Tổng tiền:", total)

#bai 9
# Bài 7.8 + 7.9 gộp lại
# Khởi tạo tồn kho và đơn giá
stock = {}
price = {}

n = int(input("Số mặt hàng trong kho: "))
for i in range(n):
    item = input("Tên mặt hàng: ")
    stock[item] = int(input("Số lượng tồn: "))
    price[item] = int(input("Đơn giá: "))

# Bài 7.8: Tính tổng giá trị kho
total_value = 0
for item in stock:
    total_value += stock[item] * price[item]
print("Tổng giá trị kho:", total_value)

# Bài 7.9: Bán hàng và cập nhật kho
m = int(input("Số mặt hàng khách mua: "))
for i in range(m):
    item = input("Mặt hàng khách mua: ")
    qty = int(input("Số lượng mua: "))
    if item in stock and stock[item] >= qty:
        stock[item] -= qty
        print("Đã bán", qty, item)
    else:
        print("Không đủ hàng hoặc không có mặt hàng:", item)

print("Tồn kho sau khi bán:", stock)

#bai 10
warehouse = set()
customer_bought = set()
n = int(input("Số sản phẩm trong kho: "))
for i in range(n):
    warehouse.add(input("Sản phẩm: "))
m = int(input("Số sản phẩm khách mua: "))
for i in range(m):
    customer_bought.add(input("Khách mua: "))
unsold = warehouse - customer_bought
print("Hàng chưa bán:", unsold)