#while True: 當滿足條件時~
#break中斷迴圈
#continue繼續迴圈(強迫進入下一round迴圈，回到起點。後面沒跑完的不會繼續)

while True:
    m = input('請選擇功能 (1)台幣轉美金 (2)台幣轉日幣 (3)選擇3結束程式')
    if m == '3':
        print('BYE')
        break
    if m != '1' and m != '2':
        print('請輸入正確的功能')
        continue
    ntd = input('請輸入台幣金額:')
    if not ntd.isdigit():
        print('請輸入正確的數字')
        continue
    if m == '1':
        result = int(ntd) / 32
        print(f'台幣{int(ntd):,}約為{result:,.0f}美金')
    if m == '2':
        result = int(ntd) / 0.198
        print(f'台幣{int(ntd):,}約為{result:,.0f}日幣')