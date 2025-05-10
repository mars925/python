import random

# random.randrange設定範圍的方式跟range一樣，特性也一樣不包含最後一個數字
# random.randrange的功能是隨機取得一個數字，range是產生一組數字
print(random.randrange(10))  # 從0到9中隨機取得一個數字
print(random.randrange(1, 10))  # 從1到9中隨機取得一個數字
print(random.randrange(1, 10, 2))  # 從[1，3，5，7，9，]中隨機取得一個數字

# random.randint設定範圍的上必須要有開始跟結束，包含最後一個數字
# 不能跳數字抽籤
print(random.randint(1, 10))  # 從1到10中隨機取得一個數字


import random

# 隨機生成 1 到 100 之間的整數
target = random.randint(1, 100)

while True:
    try:
        guess = int(input("請猜一個 1 到 100 的數字："))
        if guess < target:
            print("再大一點")
        elif guess > target:
            print("再小一點")
        else:
            print("猜中了！")
            break
    except ValueError:
        print("請輸入數字")
        continue

# List 清單
# List 可以存入很多資料，每筆資料用','分隔
# List 可以存入不同型態的資料
# List 最外層使用[]符號
L = [1, 2, 3, 4, 5]
print(L)
# 不同型態混和的List
L = [1, 2, 3, 4, 5, "Hello", ["world", 6]]  # 數字，字串，List
print(L)

# List 取值
# List 取值的方式和字串一樣, 使用[]符號
# List 取值的方式和字串一樣, 也可以使用[:]符號
# List 當中的資料編號(index)以0為開頭
L = [1, 2, 3, 4, 5]
print(L[0])  # 取值的方式和字串一樣
print(L[1])  # 取值的方式和字串一樣
print(L[2])  # 取值的方式和字串一樣
print(L[3])  # 取值的方式和字串一樣
print(L[4])  # 取值的方式和字串一樣

L = [1, 2, 3, 4, 5]
print(L[0:2])  # 取值的方式和字串一樣
print(L[1:3])  # 取值的方式和字串一樣
print(L[2:4])  # 取值的方式和字串一樣

print(len(L))  # 取得list的長度，也就是list當中

juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]
juices_list.append("西瓜汁")  # 新增西瓜汁
print(juices_list)
["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉", "西瓜汁"]
while True:
    print("請選擇果汁：")
    for i, juice in enumerate(juices_list, 1):
        print(f"{i}. {juice}")
    choice = input("輸入選項編號（或輸入 '0' 退出）：")
    if choice == "0":
        print("系統關閉")
        break
    elif choice.isdigit() and 1 <= int(choice) <= len(juices_list) - 1:
        print(f"您選擇了 {juices_list[int(choice) - 1]}")
    else:
        print("無效的選項，請重新選擇。")
