#這個連動teleegram的方式就不需要另建env

import requests
import bs4

# 常數
TOKEN = '8952152433:AAF7vnKr04M33S6H2nmavXxo2aM34UoqJqw'
#取得資料
GET_UPDATES_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
#傳送訊息
SEND_MESSAGES_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

update_id = 0

response = requests.get(GET_UPDATES_URL)
msg = response.json()
# print(msg)

chat_id = msg['result'][0]['message']['chat']['id']
print(chat_id)

for update in msg['result']:
    print(update['message']['text'])
    #聊天室id(只要都在這個聊天室裡對話，id就不會變)
    print(update['message']['chat']['id'])
    #每則訊息的專屬id
    print(update['update_id'])

    # 讓機器人發送訊息
    send_msg = requests.post(SEND_MESSAGES_URL, data={'chat_id': chat_id, 'text': '嗚啦呀哈'})

