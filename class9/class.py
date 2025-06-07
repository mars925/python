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
print(L[1:3])  # 取值的方式和字串一樣，取值的方式和字串一樣
print(L[2:4])  # 取值的方式和字串一樣

print(len(L))  # 取得list的長度，也就是list當中

juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]
print(juices_list)
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


juice = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]

while True:
    for i in range(len(juice)):
        print(f"{i+1}.{juice[i]}")
    choice = input("請選擇果汁：")
    if choice.isdigit() and 1 <= int(choice) <= len(juice):
        print(f"您選擇了 {juice[int(choice) - 1]}")
    else:
        print("無效的選項，請重新選擇。")
        continue

新訊息
12:20
import random  # 這是隨機模組

# random.randrange 設定範圍的方式跟 range一樣, 特性也一樣不包含最後一個數字
# random.randrange 的功能是隨機取得一個數字, range是產生一組數字
print(random.randrange(10))  # 從0~9中隨機取得一個數字
print(random.randrange(1, 10))  # 從1~9中隨機取得一個數字
print(random.randrange(1, 10, 2))  # 從[1, 3, 5, 7, 9]中隨機取得一個數字

# random.randint 設定範圍的方式必須要有開始跟結束, 且包含最後一個數字
# 不能跳數字抽籤
print(random.randint(1, 10))  # 從1~10中隨機取得一個數字


# List 清單 (List)
# List 可以存入很多資料，每筆資料用`，`隔開
# List 可以存入不同型態的資料
# List 最外層用`[]`包起來
L = [1, 2, 3, 4, 5]  # 數字
print(L)
# 不同型態混合
L = [1, 2, 3, 4, 5, "Hello", ["World", 6]]  # 數字, 字串, List
print(L)

# List 取值
# List 取值方式跟字串一樣, 用`[]`取值
# List 取值方式跟字串一樣, 也可以用`[:]`取值
# List 當中資料的編號(index)都從0開始
L = [1, 2, 3, 4, 5]
print(L[0])  # 取得第一個值
print(L[1])  # 取得第二個值
print(L[2])  # 取得第三個值

# List 取值的方式跟字串一樣, 也可以用`[:]`取值
# 設定範圍的方式跟range很像, 不包含最後一個數字
print(L[1:4:2])  # 取出第二個到第四個值, 且間隔為2
print(L[0:3])  # 取出第一個到第三個值
print(L[:3])  # 取得第一個到第三個值
print(L[3:])  # 取得第四個到最後一個值
print(L[:])  # 取得全部值

# list len 列表長度
L = [1, 2, 3, 4, 5]
print(len(L))  # 取得List長度, 也就是List當中有幾筆資料

# 務必不要跟index混淆, index是資料的編號, len是資料的數量

# len 可以搭配 for 迴圈使用來取得List當中的所有資料
for i in range(len(L)):  # 這邊的i是index
    print(L[i])

for i in L:  # 這邊的i是資料
    print(i)

# 要使用哪一種方式讀取List當中的資料, 要看使用的情境當中會不會需要index

回應

回覆












訊息 小酩老師









按下 Shift + Enter 以新增一行




透過 Slack 行動應用程式隨時隨地掌握最新消息

import random  # 這是隨機模組

# random.randrange 設定範圍的方式跟 range一樣, 特性也一樣不包含最後一個數字
# random.randrange 的功能是隨機取得一個數字, range是產生一組數字
print(random.randrange(10))  # 從0~9中隨機取得一個數字
print(random.randrange(1, 10))  # 從1~9中隨機取得一個數字
print(random.randrange(1, 10, 2))  # 從[1, 3, 5, 7, 9]中隨機取得一個數字

# random.randint 設定範圍的方式必須要有開始跟結束, 且包含最後一個數字
# 不能跳數字抽籤
print(random.randint(1, 10))  # 從1~10中隨機取得一個數字


# List 清單 (List)
# List 可以存入很多資料，每筆資料用`，`隔開
# List 可以存入不同型態的資料
# List 最外層用`[]`包起來
L = [1, 2, 3, 4, 5]  # 數字
print(L)
# 不同型態混合
L = [1, 2, 3, 4, 5, "Hello", ["World", 6]]  # 數字, 字串, List
print(L)

# List 取值
# List 取值方式跟字串一樣, 用`[]`取值
# List 取值方式跟字串一樣, 也可以用`[:]`取值
# List 當中資料的編號(index)都從0開始
L = [1, 2, 3, 4, 5]
print(L[0])  # 取得第一個值
print(L[1])  # 取得第二個值
print(L[2])  # 取得第三個值

# List 取值的方式跟字串一樣, 也可以用`[:]`取值
# 設定範圍的方式跟range很像, 不包含最後一個數字
print(L[1:4:2])  # 取出第二個到第四個值, 且間隔為2
print(L[0:3])  # 取出第一個到第三個值
print(L[:3])  # 取得第一個到第三個值
print(L[3:])  # 取得第四個到最後一個值
print(L[:])  # 取得全部值

# list len 列表長度
L = [1, 2, 3, 4, 5]
print(len(L))  # 取得List長度, 也就是List當中有幾筆資料

# 務必不要跟index混淆, index是資料的編號, len是資料的數量

# len 可以搭配 for 迴圈使用來取得List當中的所有資料
for i in range(len(L)):  # 這邊的i是index
    print(L[i])

for i in L:  # 這邊的i是資料
    print(i)

# 要使用哪一種方式讀取List當中的資料, 要看使用的情境當中會不會需要index