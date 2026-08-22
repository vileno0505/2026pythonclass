#整數 interger
a = 1
g = -1
h = 0
#浮點數 float
b = 3.14
#文字 string (需加入引號)
c = 'hello'
a2 = '1'
#布林 boolean True/False值(T.F要大寫)
e = True
f = False

#變數命名規則
#英文大小寫不同
#開頭不能是數字，只能是英文或底線
#只能是英文、數字及底線的組合
#不可和phthon關鍵字重複
A = 88
a_3 = 'water'
_38 = 44.55

print(type(_38))
print(type(a_3))
print(type(A))
print(type(a))
print(type(b))
print(type(c))
print(type(a2))
print(type(e))
print(type(f))

#關鍵字
import keyword
print(keyword.kwlist)

#型別轉換=轉換原先的變數設定類型
# int()
# float()
# str()

x='10'
y='50'
print(x+y)
print(int(x)+int(y))
#文字相加=連續顯示，但無法相乘

print('*' *20)
#使用數字乘法可以倍數顯示文字


