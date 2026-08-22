#list串列

lt1=['apple','banana','kiwi','lemon','orange','pinapple']
print(lt1)
print(lt1[0])
print(lt1[2])
print(lt1[1:3])
print(lt1[2:])
print(lt1[::-1])

#串列切片
print(lt1[1:3])
print(lt1[::2])
print(lt1[::-1])

# for item in range(3):
#     print(lt1[item])

for x in lt1:
    print(x)

#enumerate() 是 Python 的內建函式，用於在迭代可迭代對象（如列表、元組或字串）時，同時獲取索引和值。它返回一個 enumerate 對象，通常用於 for 迴圈中。
for i,x in enumerate(lt1):
    print(i+1,x)



