while True:
    try:
        guess = int(input('請猜一個 1 到 100 的數字：'))
        if guess < target:
            print('再大一點')
        elif guess > target:
            print('再小一點')
        else:
            print('猜中了！')
            break
    except ValueError:
        print('請輸入有效的數字。')