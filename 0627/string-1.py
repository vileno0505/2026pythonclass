#字串切片
#print(s[]) 用中括號去切想要的範圍(索引的意思)
#都是從左往右算的
#左邊從0開始
#右邊從-1開始

# w=('phthon class')
# print(w[0])  #左邊第一位
# print(w[1])
# print(w[2])
# print(w[-1]) #右邊數來第一位
# print(w[-2])
# print(w[0:6]) #左邊第一位到第五位
# print(w[:6])
# print(w[-5:]) #右邊第五位到右邊最後一位
# print(w[3:11]) #左邊第三位到第十位


#step[:] 提取xx間隔的字
#字串[開始: 結束: 間距:]
#[start: end: step]
s=('123456789')
# print(s[:]) #沒寫間隔就是全部
# print(s[::1])
# print(s[::2])
# print(s[::3])
# print(s[::-1]) #反轉字串


q='dISney CHAnNEl.HEllo WORLD.'
print(q.upper()) #全大寫
print(q.lower()) #全小寫
print(q.capitalize()) #只有第一個單字首字大寫
print(q.title()) #單字首字字母大寫


#取代replace
#old和new會自己跳出來 不用打

s2='hello world!'
result=(s2.replace('hello','wow'))
print(result)


#find尋找
#找不到會顯示-1
#用字元去算數

print(s2.find('h'))
print(s2.find('hello'))
print(s2.find('world'))
print(s2.find('word'))


#startswith 判斷開頭是否包含特定字元(bool值)
print(s2.startswith('hello'))
print(s2.startswith('woops'))
print(s2.startswith('h'))

#endswith  判斷結尾是否包含特定字元(bool值)
print(s2.endswith('!'))
print(s2.endswith('d'))
print(s2.endswith('world'))

#count 計算文字數量
print(s2.count('hello'))
print(s2.count('h'))
print(s2.count('H'))

#lens 計算文字長度
print(len(s2))
print(len(q))

x='今天星期六，上午11:49分 6/27號'
print(len(x))


#isdigit 全數字判斷(bool值)
#isalpha 全文字判斷
#isalnum 全文字+數字判斷
n='現在是星期六11點09分'
print(n.isdigit())
print(n.isalpha())
print(n.isalnum())

#數字有小數點(=符號)是不行的
n2='圓周率是3.1415926535'
print(n2.isdigit())
print(n2.isalpha())
print(n2.isalnum())


#join 合併文字
c=['apple','papaya','lemon']
print(''.join(c))
print('、'.join(c))


#split 分割文字
c2='apple, mango ,lemon'
print(c2.split())
print(c2.split(','))