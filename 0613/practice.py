#input=讓使用者輸入資料
#文字轉成數字才能做運算

#ntd=input('請輸入台幣金額:')
#=int(ntd)/0.2
#print(int(jpy))
#使用f''字串(f-string)可以將文字及變數串聯在一起，用大括弧{}把變數放進去
#print('台幣'+ntd+'約為日幣'+str(jpy)) 可以用f字串改成以下
#print(f'台幣{ntd}約為日幣{jpy}')


#加入判斷式，輸入資料不是<數字>時會跳出else的結果 而不是報錯
#ntd=input('請輸入台幣金額:')
#if ntd.isdigit():
#    jpy = int(ntd) / 0.2
#    print(f'台幣{ntd}約為日幣{jpy}')
#else:
#    print('請輸入正確的數字')



ntd=input('請輸入台幣金額:')
if not ntd.isdigit():
    exit('請輸入正確的數字')
jpy = int(ntd) / 0.2
print(f'台幣{ntd}約為日幣{jpy}')