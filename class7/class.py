# 請使用者輸入一個整數
num = int(input("請輸入一個整數："))

# 假設 num 是質數
is_prime = True

# 使用 for 迴圈從 2 到 num-1 進行除法運算
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

# 印出結果
if is_prime and num > 1:
    print(f"{num} 是質數")
else:
    print(f"{num} 不是質數")
#for...else 
#當for迴圈正常結束時，執行else區塊的程式
#example:
for i in range(5):
    print(i)
else:
    print("for循環完成")

# while...else
    #當while迴圈正常結束時，執行else區塊的程式
# example:
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("while循環完成")


#while...else
#當while迴圈正常結束時，執行else區塊的程式
#example:
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("while循環完成")
import time
s=int(input("請輸入秒數："))
for i in range(s,1,-1):
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    try:
        start = int(input("請輸入開始整數: "))
        end = int(input("請輸入結束整數: "))
        primes = list_primes_in_range(start, end)
        for prime in primes:
            print(prime)
    except ValueError:
        print("請輸入有效的整數")
          # 質數判斷
# 1. 輸入一個數字
# 2. 判斷這個數字是否為質數
# 3. 如果是質數, 就印出"是質數"
# 4. 如果不是質數, 就印出"不是質數"
# 5. 質數的定義: 只能被1和自己整除的數字, 且大於1
# 6. 例如: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...都是質數


num = int(input("請輸入一個數字: "))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False

if is_prime and num > 1:
    print(f"{num} 是質數")
else:
    print(f"{num} 不是質數")


# for ...else
# 當 for 迴圈正常結束時, 執行 else 區塊的程式
# example:
for i in range(5):
    print(i)
else:
    print("for 迴圈正常結束")

# while ...else
# 當 while 迴圈正常結束時, 執行 else 區塊的程式
# example:
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("while 迴圈正常結束")