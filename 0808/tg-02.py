import yfinance
import requests
import bs4
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

#########################################
# 讀取..env
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# ******************************************#
# 取得前一日股票資訊
def get_stock(code):
    data = yfinance.download(f'{code}.TW', period='1d')
    return data

#取得當下股票交易價格
def get_stock_now(code):
    data = yfinance.Ticker(f'{code}.TW')
    return data.fast_info['lastPrice']

############################################
# 中央社國際新聞rss
def get_intworld_rss():
    url = 'https://feeds.feedburner.com/rsscna/intworld'
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'xml')
    items = soup.find_all('item')

    result = []

    for item in items:
        title = item.find('title').text
        content = item.find('description').text
        result.append({
            'title': title,
            'content': content
        })
        # print(title)
        # print(content)

    return result


# ******************************************#
# 處理股票/stock指令
async def stock_command(
        update: Update, context: ContextTypes.DEFAULT_TYPE
):
    if len(context.args) == 0:
        await update.message.reply_text('請輸入你想知道的股票代號，如/stock 2330')
        return
    if len(context.args) == 2:
        await update.message.reply_text(
            f'現在股價為：{get_stock_now(context.args[0])}'
        )
        return
    data = get_stock(context.args[0])
    open = data['Open']
    high = data['High']
    low = data['Low']
    close = data['Close']
    volume = data['Volume']

    await update.message.reply_text(
      f'開盤價{open} \n'
        f'收盤價{close} \n'
        f'最高價{high} \n'
        f'最低價{low} \n'
        f'成交量{volume} \n'
    )

############################################
# 處理 /start 指令
async def start_command(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "你好，我是 機器人0801！\n"
        "你可以傳送任何文字給我。"
    )


############################################
# 處理 /greet 指令
async def greet_command(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "我是機器人0801！\n"
        "逼波逼波，我什麼都不會，不要問我！"
    )


############################################
# 處理 /intworld 指令
async def intworld_command(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):
    for index, news in enumerate(get_intworld_rss()):
        await update.message.reply_text(
            f'{news['title']}'
            f'\n{news["content"]}'
        )
        if index == 10:
            break


######################################################
# 處理一般文字訊息
async def echo_message(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):
    # 取得使用者輸入的文字
    user_text = update.message.text

    print("使用者輸入：", user_text)

    # 將相同的文字回覆給使用者
    await update.message.reply_text(
        f"What did you say? {user_text}"
    )


# async+await用法=排隊，形成先後順序，async的事情做完之後才會輪到await動作

##############################################
# 主程式
def main():
    if not TELEGRAM_BOT_TOKEN:
        print("找不到TOKEN")
        print("請檢查..env")
        return

    # 建立Telegram Bot應用程式
    application = (
        ApplicationBuilder()
        .token(TELEGRAM_BOT_TOKEN)
        .build()
    )

    # 加入股票/stock指令
    application.add_handler(
        CommandHandler("stock", stock_command)
    )

    # 加入 /start指令處理器
    application.add_handler(
        CommandHandler("start", start_command)
    )
    # 加入 /greet指令處理器
    application.add_handler(
        CommandHandler("greet", greet_command)
    )

    # 加入 /intworld指令處理器
    application.add_handler(
        CommandHandler("intworld", intworld_command)
    )

    # 加入一般文字訊息處理器
    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,  # 篩選:是文字AND不是指令
            echo_message  # 符合 filter 的訊息，就呼叫
        )
    )

    print("Telegram Bot 已啟動")
    print("按下 Ctrl + C 可以停止程式")

    # 持續接收 Telegram 訊息
    application.run_polling()


if __name__ == "__main__":
    main()