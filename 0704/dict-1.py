d1={'name':'Mickey','age':'100','race':'mouse'}
# print(d1)
# print(d1['name'])
# print(d1['age'])
# print(d1['races'])
# print(d1.get('minnie'))
#用.get的方式找資料，查無時會顯示none，不會報錯 無法執行

#新增(原本沒有的會加上去)/修改(原本有的會覆蓋成新資料)/刪除
# d1['girlfriend']='Minnie'
# d1['age']='150'
# del d1['race']
# print(d1)

#印出key
for data in d1:
    print(data)

#印出內容
for data in d1.values():
    print(data)

#印出key
for data in d1.keys():
    print(data)

#印出key和values(但還會有()和'')
for data in d1.items():
    print(data)

#印出key和values(不顯示()和'')
for k,v in d1.items():
    print(k,v)


#update更新---可一次新增多筆資料
data=({'friend1':'Donald','friend2':'Goofy'})
d1.update(data)
print(d1)

#查詢
#查詢分類/內容(bool值)
print('race' in d1.keys())
print('minnie' in d1.values())

#查詢分類數量
print(len(d1))