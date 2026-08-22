import yfinance
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']

code = ['2330.TW']

result = yfinance.download(code, period='7d')

result.columns = result.columns.get_level_values(0)

plt.bar(result.index,result['Volume'],color='purple')

plt.show()