# 數字 = float(input("please input your score:"))
# if 數字 % 2 == 0:
#     print("even")
# else:
#     print("odd")


# import turtle

# turtle.forward(100)
# turtle.left(90)

# turtle.done()  # 讓視窗不要關閉

# #匯入模組
# import turtle # 匯入turtle模組
# import turtle # 匯入turtle模組
# import turtle as t # 匯入turtle模組 並將其命名為t

# from turtle import *  # 匯入所有turtle所有指令
# done() #turtle.done()
for i in range(10):  # range可以產生一組數字，0~9
    print(i)

for i in range(1, 10):  # range可以產生一組數字，1~9
    print(i)

for i in range(0, 10, 2):  # range=1,3,5,7,9
    print(i)

import turtle

turtle.speed(0)  # 設定速度
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

turtle.done()  # 讓視窗不要關閉
import turtle

turtle.color("red")  # 設定顏色
turtle.shape("turtle")  # 設定形狀'arrow'或'turtle'
"circle", "square", "triangle", "classic"

turtle.stamp()  # 蓋章
turtle.penup()  # 提筆
