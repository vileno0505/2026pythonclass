import yfinance
import mplfinance as mpl #畫出k線圖的程式

code = ['2327.TW']

result = yfinance.download(code, period='1mo')
print(result.columns)

#columns 指的就是 DataFrame 的「欄標題」
#取columns中位置為0的資料即可
#.get_level_values(數字) = 從「多層資料」中，拿出指定的那一層。
result.columns = result.columns.get_level_values(0)

print(result.columns)

marker_color = mpl.make_marketcolors(
    up = 'red',
    down = 'green',
    inherit = True
)

style = mpl.make_mpf_style(
    marketcolors = marker_color
)


#畫出k線圖
mpl.plot(result,type='candle',style=style)