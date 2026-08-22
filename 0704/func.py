#function 函式
#def定義函式

#def 函式名稱:
#return 值(要把值存回去函式名稱內，才能給別的函式作計算)

def bar():
    return'bar'
b=bar()
print(b)

def bigo(a):
    return a*30
print(bigo(5))

def bingo(b):
    return b*50
print(bingo(5))

print(bigo(5)*bingo(5))

def account(money , tax=1.15):
    return(money*tax)

print(int(account(400)))
print(account(tax=5,money=500))
print(int(account(money=2000)))
print(account(5000,3))


#加一個* 讓回傳值變成tuple型別
def aa(*args):
    return sum(args)
print(aa(1,2,4,16,132))


#加兩個*，讓回傳值變成dict型別
def bb(**kwargs):
    return kwargs

print(bb(name='amy',age='25'))
