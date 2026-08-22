import random
# print(input('樂透號碼產生器！點選Enter開始'))
# while True:
#  for n in range(6):
#      lottery=random.randint(1,49)
#      print(lottery)
#
#  replay=input('再來一組?點選任意鍵繼續，或按"e"結束程式')
#  if replay.lower() == 'e':
#      print('祝您中大獎!')
#      break

#單純做出取號機
#解法1
#設定result是空串列，要填入答案進去。從1-49選號，若有重複就刪掉，直到len長度達到6就終止抽取並印出。

# result=[]
# while True:
#     ans=random.randint(1,49)
#     if ans in result:
#         continue
#     result.append(ans)
#     if len(result) == 6 :
#         break
# print(result)

#解法2
#ramdom.sample隨機取樣不重複
# result=random.sample(range(1,49),6)
# print(result)

#解法3(有可能抽到重覆的)
#random.choice
# q=random.choices(range(1,49),k=6)
# print(q)

#補充random.choice用法：可以作抽卡機
cards=['R','SR','SSR']
weights=[85,10,5]
q=random.choices(cards,k=1,weights=weights)
print(q)