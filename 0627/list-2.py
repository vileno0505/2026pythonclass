
#串列方法

fruits=['Apple','orange','Grapes','mango','Lemon','lime','BAnana']
#加入
#append
# fruits.append('kiwi')


#insert
# fruits.insert(3,'coconuts')


#extend
# fruits.extend(['coconuts'])


#刪除
#remove 填入名字刪除一項(如遇同名則刪除左邊數來第一個遇到的)
# fruits.remove('apple')

# del  填入物件索引值刪除
#del串列[索引值]
# del fruits[2]

#pop 1)移除最後一個 2)移除指定索引值
#fruits.pop()
#fruits.pop(5)

# #clear 清空串列
# fruits.clear()

# #修改內容
# fruits[3]='蜜柑'
# print(fruits)


#查詢
#index 回傳查詢物件的所在索引值(沒有就會報錯)
# print(fruits.index('lime'))

#count 計算物件數量(沒有會顯示0)
#print(fruits.count('lime'))

#確認串列中是否有存在查詢的物件
#print('lime' in fruits)


#排序
#只能排英文或數字
#中文排序看中文內碼，不是筆畫，所以即使排了也不知道在排什麼

#reverse 把順序完全反轉，但不排序
#fruits.reverse()

#sort
#串列名稱.sort()
#遇到大小寫不同時有可能排序會亂掉，需另外讓系統將單字視為全大寫或全小寫
#fruits.sort()
#fruits.sort(key = str.lower)
#fruits.sort(key = str.upper)

#print(fruits)


#另一種-ed的寫法
#會產生一個新的串列

# fruits_sorted=sorted(fruits)
# print(fruits_sorted)


fruits_reversed=reversed(fruits)
#print(fruits_reversed) #如果只寫這樣，結果會是一個串列
#要再寫一個迴圈繞出來
for item in fruits_reversed:
    print(item)