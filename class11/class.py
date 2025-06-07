# z複製list,避免原本的list被修改
L = ["hello", "world"]
L2 = L.copy()  # 使用copy()複製list
print(L2)  # ["hello", "world"]
L2 = "python"  # 修改複製後List的索引0資料
print(L2)  # ["python", "world"] #修改原本List的索引0資料
print(L)  # ["hello", "world"] #修改原本List的索引0資料
# 列表可以存入不同型態的資料
# 列表可以存入不同型態的資料

# 列表取值
# 列表取值的方式和字串一樣, 使用[]符號
# 列表取值的方式和字串一樣, 也可以使用[:]符號
# 列表當中的資料編號(index)以0為開頭
L = ["hello", "world"]
# remove:移除List中指定的資料
L.remove("hello")
print(L)
# pop:刪除List中最後一個資料
L.pop()
print(L)

# pop:移除並回傳List中的元素
L = ["hello", "world"]
print(L.pop(0))
print(L)


import random

# 隨機生成 1 到 100 之間的整數
target = random.randint(1, 100)

while True:
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
# 功能說明：

# 新增東西：將物品名稱加入清單的尾端。

# 修改東西：根據物品編號修改清單中的物品。

# 刪除東西：根據物品編號刪除清單中的物品。

# 離開程式：結束程式。

# 這段程式碼提供了基本的購物清單管理功能，適合用來練習 Python 的列表操作與條件判斷。如果您有進一步的需求或想要擴充功能，歡迎提出！


# 資料來源
# 你說：
# 請解釋

# ChatGPT 說：
# 當然可以！讓我為您詳細解釋這段 Python 購物清單程式碼的運作原理。
# fnslearn.com

# 🧱 程式架構概覽
# 這段程式碼主要透過一個 while 迴圈，持續顯示功能選單並等待使用者輸入，直到使用者選擇「離開程式」為止。在每次迴圈中，程式會根據使用者的選擇執行相應的操作，並在操作後更新購物清單的內容。

# 📋 購物清單初始化
# python
# 複製
# 編輯
# shopping_list = []
# 這行程式碼創建了一個空的列表 shopping_list，用來儲存使用者的購物清單項目。

# 🔁 主迴圈與功能選單
# python
# 複製
# 編輯
# while True:
#     print("\n購物清單：")
#     if shopping_list:
#         for idx, item in enumerate(shopping_list):
#             print(f"{idx}. {item}")
#     else:
#         print("目前清單是空的！")
# 在每次迴圈中，程式會顯示當前的購物清單。如果清單中有項目，則列出每個項目的編號與名稱；如果清單為空，則顯示「目前清單是空的！」。

# 接著，程式會顯示功能選單，讓使用者選擇要執行的操作：

# python
# 複製
# 編輯
# print("\n功能選單：")
# print("1. 新增東西")
# print("2. 修改東西")
# print("3. 刪除東西")
# print("4. 離開程式")
# choice = input("請輸入你的選擇 (1-4)：")
# 🛒 新增物品
# python
# 複製
# 編輯
# if choice == "1":
#     item = input("請輸入要新增的物品：")
#     shopping_list.append(item)
#     print(f"{item} 已加入清單！")
# 如果使用者選擇「新增東西」，程式會提示使用者輸入物品名稱，並將該物品加入 shopping_list 列表的尾端。

# ✏️ 修改物品
# python
# 複製
# 編輯
# elif choice == "2":
#     try:
#         idx = int(input("請輸入要修改的物品編號："))
#         if 0 <= idx < len(shopping_list):
#             new_item = input("請輸入新的物品：")
#             shopping_list[idx] = new_item
#             print("物品已修改！")
#         else:
#             print("無效的編號。")
#     except ValueError:
#         print("請輸入有效的編號。")
# 如果使用者選擇「修改東西」，程式會提示使用者輸入要修改的物品編號。如果該編號有效，則提示使用者輸入新的物品名稱，並更新清單中的該項目。如果編號無效或輸入的不是數字，則顯示錯誤訊息。

# 🗑️ 刪除物品
# python
# 複製
# 編輯
# elif choice == "3":
#     try:
#         idx = int(input("請輸入要刪除的物品編號："))
#         if 0 <= idx < len(shopping_list):
#             removed_item = shopping_list.pop(idx)
#             print(f"{removed_item} 已從清單中移除。")
#         else:
#             print("無效的編號。")
#     except ValueError:
#         print("請輸入有效的編號。")
# 如果使用者選擇「刪除東西」，程式會提示使用者輸入要刪除的物品編號。如果該編號有效，則使用 pop() 方法將該項目從清單中移除，並顯示移除的物品名稱。如果編號無效或輸入的不是數字，則顯示錯誤訊息。

# 👋 離開程式
# python
# 複製
# 編輯
# elif choice == "4":
#     print("再見！")
#     break
# 如果使用者選擇「離開程式」，程式會顯示「再見！」並終止 while 迴圈，結束程式執行。

# ❌ 無效選擇處理
# python
# 複製
# 編輯
# else:
#     print("無效的選擇。")
# 如果使用者輸入的選擇不是 1、2、3 或 4，程式會顯示「無效的選擇。」並重新顯示功能選單，等待使用者重新輸入。

# ✅ 總結
# 這段程式碼展示了如何使用 Python 的列表（list）來管理購物清單，並透過條件判斷與迴圈實現互動式的功能。它涵蓋了新增、修改、刪除和查看清單等基本操作，適合初學者練習 Python 的基本語法與邏輯結構。
# 如果您有任何疑問或需要進一步的說明，請隨時提出！

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

# 複製 List，避免原本的 List 被更動
L = ["Hello", "World"]
L2 = L.copy()  # 使用 copy() 複製 List
print(L2)  # ['Hello', 'World']
L2[0] = "Python"  # 修改複製後 List 的索引 0 資料
print(L)  # ['Hello', 'World'] 原本的 List 不受影響
print(L2)  # ['Python', 'World'] 只有複製的 List 被改變
# 這跟變數的=賦值不同，一般情況下會開2個記憶體空間，
# 在List的情況下使用=會讓兩個變數名稱指向同一個記憶體空間，
# 這導致修改一個 List 會影響到另一個 List。
# 所以在需要複製 List 時，應該使用 copy() 方法。


# remove：移除 List 中指定的元素（只會移除第一個找到的）
L = ["Hello", "World", "Python"]
L.remove("World")  # 移除 "World"
print(L)  # ['Hello', 'Python']

# pop：移除並回傳 List 中的元素
L = ["Hello", "World", "Python"]
# 不給索引時，pop() 會移除最後一個元素
L.pop()  # 移除最後一個元素
print(L)  # ['Hello', 'World']
s = L.pop(1)  # 移除索引 1 的元素，並回傳該值
print(s)  # World
print(L)  # ['Hello']

shopping_list = []

while True:
    # 自動列出目前的購物清單
    print("購物清單：")
    if shopping_list:
        for i in range(len(shopping_list)):
            print(f"{i}. {shopping_list[i]}")
    else:
        print("目前清單是空的！")  # 功能選單
    print("功能選單：")
    print("1. 新增東西")
    print("2. 修改東西")
    print("3. 刪除東西")
    print("4. 離開程式")

    choice = input("請輸入你的選擇 (1-4)：")

    # 新增（Create）
    if choice == "1":
        print("新增選單：")
        print("a. 加到尾端")
        print("b. 插入指定位置")
        add_choice = input("請選擇方法 (a/b)：")
        if add_choice == "a":
            item = input("請輸入要新增的物品：")
            shopping_list.append(item)
            print(f"{item} 已加入清單！")

        elif add_choice == "b":
            item = input("請輸入要新增到清單中的物品：")
            position = int(input("請輸入位置 (0 為第一個)："))
            if 0 <= position <= len(shopping_list):
                shopping_list.insert(position, item)
                print(f"{item} 已新增到清單中的位置 {position}！")
            else:
                print("無效的位置！")

        else:
            print("無效的新增選項！")

    # 更新（Update）
    elif choice == "2":
        print("修改選單：")
        index = int(input("請輸入要修改的物品編號："))
        if 0 <= index < len(shopping_list):
            new_item = input("請輸入新的物品：")
            shopping_list[index] = new_item
            print("物品已修改！")
        else:
            print("無效的物品編號！")

    # 刪除（Delete）
    elif choice == "3":
        print("刪除選單：")
        print("a. 依名稱刪除")
        print("b. 依位置刪除")
        delete_choice = input("請選擇方法 (a/b)：")
        if delete_choice == "a":
            item = input("請輸入要刪除的物品名稱：")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} 已從清單中移除。")
            else:
                print("找不到該物品！")

        elif delete_choice == "b":
            index = int(input("請輸入要刪除的物品編號："))
            if 0 <= index < len(shopping_list):
                removed = shopping_list.pop(index)
                print(f"{removed} 已從清單中移除。")
            else:
                print("無效的物品編號！")
        else:
            print("無效的刪除選項！")

    # 離開程式
    elif choice == "4":
        print("再見！")
        break

    else:
        print("請輸入 1 到 4 之間的數字。")
