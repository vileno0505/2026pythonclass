import yfinance
import matplotlib.pyplot as plt

#指定字體
plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']

#台股代號.TW 日經代號.T 美股直接寫代碼
#各國股市顯示的金額為各國貨幣

code = ['2327.TW']
#code = input('請輸入股市代碼:')

#台股用
#esult = yfinance.download(f'{code}.TW', period='1mo')

#其他股市(input時需要打完整)
#period='1mo' 從今天開始回推一個時間區間
#start+end=指定精準時間段
#result = yfinance.download(code, '2025-07-01','2026-08-07')
result = yfinance.download(code, period='5mo')

plt.title('2327國巨走勢圖')
plt.plot(result.index,result['High'],label='最高價',color='red',linewidth='1')
plt.plot(result.index,result['Low'],label='最低價',color='green',linewidth='1')
plt.plot(result.index,result['Close'],label='收盤價',color='orange',linewidth='1')

#print(result)

#線條label的說明框
plt.legend()

plt.show()