#迴圈  重複執行指令
#for
#用range來指定迴圈次數，知道迴圈次數的都用for來寫

#range(x) -> 0~x-1
#range(x,y)) -> x~y-1

#for n in range(5):
#('ALOHA!')

# #加入f字串
# #for n in range(1,5):
# #    print(f'ALOHA!{n}')
#
# i=5
# for n in range(i):
#     print('*' * (n+1))
# for n in range(i):
#     print('*' * (i-n))
#
#
# i=10
# for n in range(i):
#     print(' '*(i-n-1) + '*' * (2*n+1) )
#

#while 不定數迴圈
#用於無法確定迴圈次數的場合
#在條件滿足前會一直重複跑，設錯會產生無限迴圈
#
# x=0
# while x<10:
#     print(x)
#     x=x+1
#
# x=0
# while x<10:
#     x+=1
#     print(x)


#break 中斷迴圈

while True:
    x=input('請輸入內容:')
    print(x)
    if x == 'no':
        break