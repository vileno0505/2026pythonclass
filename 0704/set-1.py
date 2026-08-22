#set 集合 {}
#不允許重複的值，在集合內有重複會自己刪掉
#無序=沒有索引值=不能用切片

#空集合不能用s={}的方式寫，這樣是dict
#要寫成 s=set()
s1={1,2,3,4,5}
s2={1,2,2,2,6,1,4,2,8,5}
s3={'桃園市','蘆竹區','桃園市','桃園區','桃園市','中壢區','桃園市','平鎮區','桃園市','八德區'}

print(s1)
print(s2)
print(s3)

#可以新增.修改．更新資料
s1.add(6)      #新增
s1.remove(1)   #要刪除的資料不存在會報錯
s1.discard(55) #要刪除的資料不存在也不會報錯
s1.update({123})  #不存在的=新增；已存在的=修改

print(s1)

print(len(s1))


#可以作資料的交叉比對
#集合運算
#遵守先乘除後加減，乘除之前先作()

q1={'A','B','C','F'}
q2={'A','B','E','F'}

#交集=有重複的
print(q1 & q2)
print(q1.intersection(q2))

#聯集=有出現的
print(q1 | q2)
print(q1.union(q2))

#差集=A扣掉跟B重複的
print(q1 - q2)
print(q2 - q1)
print(q1.difference(q2))
print(q2.difference(q1))

#對稱差集=A.B互扣之後沒有扣掉的
print(q1 ^ q2)
print(q1.symmetric_difference(q2))


print('-'*50)


day1={'A','B','C','D'}
day2={'A','B'}
day3={'B','C','D'}

print(day1 & day2 & day3)
print(day1 | day2 | day3)
print((day1 & day2) | day3)