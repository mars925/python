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