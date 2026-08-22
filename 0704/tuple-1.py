#tuple元組
#長相:()小括號內有資料
#內容僅供檢視，無法修改.變動

t=('apple','orange','kiwi')

#可以不加括號但會較難辨識，不建議
# t='apple','orange','kiwi'

# t=('apple')
# t=tuple()
# print(t)

#兩個tuple可以相加
t2=('papaya','mango')
t3=t+t2
print(t3)

#也可以用切片抓資料
print(t3[0])
print(t3[-1])
print(t3[::2])
print(t3[::-1])

#解構
coord=(23.5,121.5)
lat,lon=coord
print(lat,lon)