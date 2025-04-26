# while 回圈
# 這是條件式迴圈，當條件成立時，會執行回圈內的程式
i = 1
while i < 10:
    # 當i小於10時，執行回圈內的程式
    print(i)
    i = i + 1

# 算數指定運算子
# +=, -=, *=, /=, %=,**=,//=
# x = x + 1 等於x =+ 1
# x = x - 1 等於x =- 1
# x = x * 1 等於x =* 1
# x = x / 1 等於x =/ 1
# x = x % 1 等於x =% 1
# x = x ** 1 等於x =** 1
# x = x // 1 等於x =// 1

# 符號優先順序
# 1. () 先執行括號內的運算式
# 2. ** 指數運算
# 3. + - 正負號
# 4. * / // % 乘除法, 取餘數, 整數乘法
# 5. + - 加減法
# 6. == != > < >= <= 比較運算
# 7. and or not 邏輯運算
# 8. = += -= *= /= %= //= **=

i = 1
while i < 10:
    print(i)
    i += 1  # 等於i = i + 1

# 設定正確的密碼
correct_password = "1234"

# 使用 while 迴圈持續要求輸入，直到輸入正確為止
password = ""
while password != correct_password:
    # 提示使用者輸入密碼
    password = input("請輸入密碼：")

    # 檢查輸入是否正確
    if password == correct_password:
        print("歡迎使用本系統！")
    else:
        print("密碼錯誤，請再試一次。")
