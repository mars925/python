hile True:
    try:
        guess = int(input("請猜一個 1 到 100 的數字："))
        if guess < target:
            print("再大一點")
        elif guess > target:
            print("再小一點")
        else:
            print("猜中了！")
            break
    except ValueError:
        print("請輸入數字")
        continue

# 初始化購物清單
shopping_list = []

while True:
    print("\n購物清單：")
    if shopping_list:
        for idx, item in enumerate(shopping_list):
            print(f"{idx}. {item}")
    else:
        print("目前清單是空的！")

    print("\n功能選單：")
    print("1. 新增東西")
    print("2. 修改東西")
    print("3. 刪除東西")
    print("4. 離開程式")
    choice = input("請輸入你的選擇 (1-4)：")

    if choice == "1":
        item = input("請輸入要新增的物品：")
        shopping_list.append(item)
        print(f"{item} 已加入清單！")

    elif choice == "2":
        try:
            idx = int(input("請輸入要修改的物品編號："))
            if 0 <= idx < len(shopping_list):
                new_item = input("請輸入新的物品：")
                shopping_list[idx] = new_item
                print("物品已修改！")
            else:
                print("無效的編號。")
        except ValueError:
            print("請輸入有效的編號。")

    elif choice == "3":
        try:
            idx = int(input("請輸入要刪除的物品編號："))
            if 0 <= idx < len(shopping_list):
                removed_item = shopping_list.pop(idx)
                print(f"{removed_item} 已從清單中移除。")
            else:
                print("無效的編號。")
        except ValueError:
            print("請輸入有效的編號。")

    elif choice == "4":
        print("再見！")
        break

    else:
        print("無效的選擇。")