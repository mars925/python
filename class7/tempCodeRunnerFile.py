for i in range(s，-1，-1):
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