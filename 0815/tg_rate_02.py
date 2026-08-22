#學說話機器人 你說什麼他就說什麼

import requests
import bs4

# 常數
TOKEN = '8952152433:AAF7vnKr04M33S6H2nmavXxo2aM34UoqJqw'
#取得資料
GET_UPDATES_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
#傳送訊息
SEND_MESSAGES_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

update_id = 0

while True:
    try:
        param = {
            'offset' : update_id,
            'timeout' : 30
        }
        #使用者的timeout時間必須比tg的timeout時間長
        response = requests.get(GET_UPDATES_URL,params=param, timeout=35)
        data = response.json()
        for update in data['result']:
            update_id = update['update_id'] + 1  #每發送一次id就+1，這樣tg就不會抓到舊訊息
            chat_id = update['message']['chat']['id']
            user_text = update['message']['text']
            send_data = {'chat_id': chat_id, 'text': user_text}
            send_msg = requests.post(SEND_MESSAGES_URL, data=send_data, timeout=30)

    except:
        print('error')
        continue
