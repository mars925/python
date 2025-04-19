# import turtle

# # 設定畫筆顏色
# turtle.color("yellow")

# # 隱藏畫筆的箭頭
# turtle.hideturtle()

# # 開始填充顏色
# turtle.begin_fill()

# # 繪製五角星
# for i in range(5):
#     turtle.forward(100)  # 前進 100 單位
#     turtle.right(144)  # 右轉 144 度

# # 結束填充顏色
# turtle.end_fill()

# # 完成繪圖
# turtle.done()

# 顯示圖片
# turtle.home()#回到原點
print("輸入無效，請確保您輸入的是一個有效的整數")
for i in range(1, 10):  # 外層迴圈：1 到 9
    for j in range(1, 10):  # 內層迴圈：1 到 9
        print(f"{i} x {j} = {i * j}", end="\t")  # 使用 \t 對齊
    print()  # 每列印完一行換行

for i in range(1, 10):  # 外層迴圈：1 到 9
    for j in range(1, 10):  # 內層迴圈：1 到 9
        print(f"{i} x {j} = {i * j}", end="\t")  # 使用 \t 對齊
    print()  # 每列印完一行換行

import turtle as t

a = 0
for i in range(12):
    t.speed(0)
    t.penup()
    t.forward(100)
    t.stamp()
    t.home()
    a = a + 1
    t.right(30 * a)
t.done()


import turtle as t
import time

a = 0
t.speed(0)
t.left(90)
for i in range(12):
    t.forward(100)
    t.home()
    time.sleep(1)
    t.clear()
    a = int(a + 1)
    b = int(6 * a)
    t.left(90 - b)

t.done()
a = int(input("請輸入正整數:"))

for i in range(1, a + 1):
    if i % 3 == 0:
        print(i)
    elif i % 7 == 0:
        print(i)
        a = int(input("請輸入要印出的箭頭大小:"))  # 輸入箭頭大小

for i in range(a):  # 迴圈
    b = " " * (a - i - 1)  # 算出「 」（空格）要有幾個
    c = "*" * (2 * i + 1)  # 算出「＊」（星星）要有幾個
    print(b + c)  # 把星星和空格一起印出來

for i in range(a):  # 迴圈
    B = " " * (a - 1)  # 算出「 」（空格）要有幾個
    print(B + "*")  # 把星星和空格印出來
