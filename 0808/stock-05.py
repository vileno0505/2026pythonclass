import yfinance
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
code = ['2330.TW']

result = yfinance.download(code, period='30d')
result.columns = result.columns.get_level_values(0)

#fig 和 ax是慣例命名，不是規定，換掉也沒關係
#fig=figure 的縮寫，代表「整張圖」。
#ax=axes 的縮寫，代表「畫圖的區域／座標軸」。
fig , ax = plt.subplots(3,1)

#plot=折線圖  bar=長條圖
ax[0].plot(result.index , result['Open'] , color='blue')
ax[0].plot(result.index , result['Close'] , color='red')
ax[1].bar(result.index , result['Volume'])
ax[2].plot(result.index , result['High'] , color='purple')

#為各表格加上標題
ax[0].set_title('2330開盤價-藍 收盤價-紅')
ax[1].set_title('2330交易量')
ax[2].set_title('2330最高價')

#表格若擠在一起會自動幫分開
plt.tight_layout()

plt.show()