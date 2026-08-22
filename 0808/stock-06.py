import yfinance
import mplfinance as mpl

code=['0050.TW']

result = yfinance.download(code, period='3mo', auto_adjust=False)
result.columns = result.columns.get_level_values(0)

marker_color = mpl.make_marketcolors(
    up = 'red',
    down = 'green',
    inherit = True
)

style = mpl.make_mpf_style(
    marketcolors = marker_color
)


#畫出k線圖
#volume=圖上加入交易量
#mav=圖上加入均線(需指定天數)，一張圖只能畫一條均線
mpl.plot(result , type='candle' , style=style , volume=True , mav=5)