# 判斷數字 n 是否為質數
def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))


start, end = int(input("請輸入開始整數: ")), int(input("請輸入結束整數: "))

for num in range(start, end + 1):
    if is_prime(num):
        print(num)
# 迴圈 break可以用來跳出所屬的迴圈，所以判斷break屬於哪個迴圈時，必須注意縮排
# 例如：
for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            break
            print(f"i:{i},j:{j}")
# 這裡的break只會跳出內層的for迴圈，外層的for迴圈還是會繼續執行


print("歡迎使用飲料機！")
print("請選擇你想要的飲料：")
print("1. 蘋果汁")
print("2. 柳橙汁")
print("3. 葡萄汁")
print("4. 系統關閉")

while True:
    try:
        選擇 = int(input("請輸入飲料編號 (1-4)："))
        if 選擇 == 1:
            print("您選擇了：蘋果汁")
        elif 選擇 == 2:
            print("您選擇了：柳橙汁")
        elif 選擇 == 3:
            print("您選擇了：葡萄汁")
        elif 選擇 == 4:
            print("系統關閉，感謝使用！")
            break
        else:
            print("輸入錯誤查無此果汁，請重新輸入。")
    except ValueError:
        print("請輸入有效的數字編號。")
# continue
# 迴圈的continue可以用來跳出當前迴圈，繼續執行下一次的迴圈
# 例如：
for i in range(5):
    if i == 2:
        continue
    print(i)
# 這裡的continue會跳過i=2的那次迴圈，執行i=3的迴圈
# 所以輸出的結果是:0，1，2，3，4
# continue也可以用在while迴圈中
i = 0
while i < 5:
    if i == 2:
        continue
    print(i)
    i += 1
# 輸入跳繩次數
次數 = int(input("請輸入要跳繩的次數："))

# 開始跳繩
for 跳次 in range(1, 次數 + 1):
    if 跳次 % 10 == 0:
        print(f"跳到第 {跳次} 下，休息一下！")
        continue  # 跳過這次跳繩，進入下一次
    print(f"跳繩第 {跳次} 下")
