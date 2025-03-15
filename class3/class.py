# try: except:
# 錯誤處理
try:
    # 嘗試執行可能會出錯的程式碼
    n = int(input("請輸入一個整數:"))

except:
    # 如果有錯誤發生，執行這段成執行這段成式碼
    print("you showld input a number")

else:
    # 如果沒有錯誤發生，執行這段程式碼
    print(n + 1)

try:
    h = float(input("請輸入身高:"))
    w = float(input("請輸入體重:"))
    bmi = w / h**2
    print(f"你的BMI為{bmi}")
except:
    print("請輸入有效的數字")
# 比較運算子
print(1 == 1)  # true，1等於1
print(1 != 1)  # false，1不等於1
print(1 != 2)  # true，1不等於2
print(1 < 2)  # true，1小於2
print(1 > 2)  # false，1大於2
print(1 <= 2)  # true，1小於等於2

# 邏輯運算子
# and代表全部條件都要成立才會回傳true
# or代表只要有一個條件成立就會回傳true
# not代表將原來的布林值反轉


print(True and True)  # True， true and True
print(True and False)  # False，True and False
print(False and True)  # False，False and True
print(False and False)  # False，False and False
print(True or True)  # True，True and True
print(True or False)  # True，True and False
print(not True)  # False，not True
print(not False)  # True，not False

password = input("請輸入密碼:")
if password == "mars":
    print("密碼正確")
else:
    print("error")
# if elif else
pwd = input("請輸入密碼:")
if pwd == "mars":
    print("密碼正確")
elif pwd == "moon":  # 如果密碼是456
    print("密碼正確")  # 印出歡迎moon
else:
    print("密碼錯誤")
# if elif else是連續的判斷，只要一個條件成立，後面的判斷就不會執行
# if一定要有，elif可以有多個但是選用，else只能有一個
