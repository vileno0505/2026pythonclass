import yfinance
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']

code = ['2327.TW']

result = yfinance.download(code, period='5mo')

plt.title('2327國巨')
#均線 MA .rolling(天數).mean()
MA5 = result['Close'].rolling(5).mean()
MA20 = result['Close'].rolling(20).mean()
close = result['Close']

#這邊MA5們已經設成變數了，就不用用[]再框起來
plt.plot(result.index,close,label='收盤價',linewidth='1')
plt.plot(result.index,MA5,label='5日均線',linewidth='1')
plt.plot(result.index,MA20,label='20日均線',linewidth='1')

plt.legend()

plt.show()