次數 = int(input("請輸入要跳繩的次數："))

# 開始跳繩
for 跳次 in range(1, 次數 + 1):
    if 跳次 % 10 == 0:
        print(f"跳到第 {跳次} 下，休息一下！")
        continue  # 跳過這次跳繩，進入下一次
    print(f"跳繩第 {跳次} 下")