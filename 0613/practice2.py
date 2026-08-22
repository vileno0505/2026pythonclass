m=input('請選擇功能 (1)台幣轉美金 (2)台幣轉日幣')
if m !='1' and m !='2':
    exit('請輸入正確的功能')
ntd=input('請輸入台幣金額:')
if not ntd.isdigit():
    exit('請輸入正確的數字')
if m=='1':
    result=int(ntd)/32
    print(f'台幣{int(ntd):,}約為{result:,.0f}美金')
if m=='2':
    result=int(ntd)/0.198
    print(f'台幣{int(ntd):,}約為{result:,.0f}日幣')