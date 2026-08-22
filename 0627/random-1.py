#random隨機
import random

#print(random.random())

#幾位數的隨機組合
#print(random.randint(a=1,b=999))

#可以用來隨機抽籤
# fruits=['Apple','Orange','Grapes','Mango','Lemon','Lime','Banana']
# print(random.choice(fruits))



#猜數字遊戲
while True:
    print('猜數字遊戲開始!')
    h=int(input('請輸入要猜的最大值:'))
    ans = random.randint(a=1,b=h)
    print(ans)
    low=1
    high=h
    while True:
        guess=input('請輸入數字:')
        guess = int(guess)

        if guess > ans:
            high = guess
            print(f'太大，在{low}~{high}之間')
        elif guess < ans:
            low = guess
            print(f'太小，在{low}~{high}之間')
        else:
            print('恭喜答對!')
            break

    replay = input('是否要再玩一次?按任意鍵重玩 輸入(n)結束')

    if replay.lower() == 'n':
        print('掰!')
        break