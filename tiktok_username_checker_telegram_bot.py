import os,random,time,telebot,requests,pathlib
from user_agent import generate_user_agent
from telebot import *
from datetime import datetime
token = '5943413715:AAFizjF69Ja6-Th9Z1xdrotczKNzP0QF2Tc'
ue3ex = '749710232'
s = requests.session()
print('BOT IS RUNNING >>>>>>>>>')
RunPosts = True
bot = telebot.TeleBot(token)
markup_stop = types.InlineKeyboardMarkup()
stop = types.InlineKeyboardButton(text='Stop', callback_data='stop')
markup_stop.add(stop)
time_sleep = 3
requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ue3ex}&text=𝗕𝗼𝘁 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝘀𝘁𝗮𝗿𝘁𝗲𝗱 ▶ \n\n 𝗖𝗹𝗶𝗰𝗸 /start  𝗧𝗼 𝘀𝘁𝗮𝗿𝘁 𝗯𝗼𝘁 (:')
@bot.message_handler(commands=['start'])
def start(message):
    list = open('done.txt', 'r')
    li = len(list.readlines())
    idd = message.from_user.id
    markup_inline = types.InlineKeyboardMarkup()
    start = types.InlineKeyboardButton(text='دەست پێ کردن ▶', callback_data='start')
    make = types.Ies.InlineKeyboardButton(text='دروست کردنی لیست List 📜', callback_data='make')
    delete = types.InlineKeyboardButton(text='ڕەشکردنەوەی لیست 🗑', callback_data='delete')
    file = types.Ies.InlineKeyboardButton(text='ناردنی لیست 📁', callback_data='file')
    donefilee = types.Ies.InlineKeyboardButton(text='فایلی یوزەرە دۆزراوەکان ✅', callback_data='done')
    deletedone = types.Inles.InlineKeyboardButton(text='ڕەشکردنەوەی فایلی یوزەرە دۆزراوەکان 🗑', callback_data='deletedone')
    sid = types.es.InlineKeyboardButton(text='سیزن ئایدی دانێ 🆔', callback_data='sid')
    emt = types.InlineKeyboardButton(text='', callback_data='emt')
    markup_inline.row_width = 2
    markup_inline.add(start, make, file, delete, donefilee, deletedone, sid, emt)
    if idd == ue3ex or idd == 749710232:
        if li == 0:
            bot.send_message(message.chat.id, text='𝗧𝗜𝗞𝗧𝗢𝗞 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 🤍\n\n'
                                                   f'[✅] دانەی دۆزراوە : 0\n\n'
                                                   f'Ξ سەرۆک : @ue3ex\n\n'
                                                   f'Ξ ناو :@ue3ex \n\n'
                                                   f'Ξ پاس :@ue3ex \n\n',
                             reply_markup=markup_inline)
        else:
            bot.send_message(message.chat.id, text='𝗧𝗜𝗞𝗧𝗢𝗞 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 🤍\n\n'
                                                   f'[✅] دانەی دۆزراوا : {li}\n\n'
                                                   f'Ξ سەرۆک : @ue3ex\n\n'
                                                   f'Ξ ناو :@ue3ex \n\n'
                                                   f'Ξ پاس :@ue3ex \n\n',
                             reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    global RunPosts
    if call.data == 'make':
        sent = bot.send_message(call.message.chat.id, text='🔢 چەند دانە  :')
        bot.register_next_step_handler(sent, length)
    if call.data == 'start':
        check(call.message)
    if call.data == 'stop':
        RunPosts = False
    elif call.data == 'delete':
        delete(call.message)

    elif call.data == 'file':
        files(call.message)
    elif call.data == 'done':
        done(call.message)
    elif call.data == 'sid':
        sent = bot.send_message(call.message.chat.id, text='🆔 ناردنی سیزن ئایدی  :')
        bot.register_next_step_handler(sent, sidinput)
    elif call.data == 'deletedone':
        deletedone(call.message)
def sidinput(message):
    sid = message.text
    url = f'https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id=s2kk&app_language=en'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": generate_user_agent(),
        "Connection": "Keep-Alive",
        "Host": "www.tiktok.com",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0"}
    data = ""
    cookies = {'sessionid': sid}
    res = s.get(url, data=data, headers=headers, cookies=cookies)
    markup_inline = types.InlineKeyboardMarkup()
    markup_inlinee = types.InlineKeyboardMarkup()
    start = types.InlineKeyboardButton(text='دەست کردن بە چێک ▶', callback_data='start')
    sidd = types.es.InlineKeyboardButton(text='دانانی سیزن ئایدی 🆔', callback_data='sid')
    markup_inlinee.row_width = 2
    markup_inline.row_width = 2
    markup_inline.add(start)
    markup_inlinee.add(sidd)
    if 'This username isn’t available.' in res.text or '"is_valid":false' in res.text or '"is_valid":true' in res.text or '"status_msg":""' in res.text:
        sidf = open("sessionid.txt", "w")
        sidf.write(sid)
        sidf.close()
        bot.send_message(message.chat.id, text='تەواو بوو بەرێز ئێستا ئەتوانی دەست پێ بکەیت [✅] ',
                         reply_markup=markup_inline)
    elif '{}' in res.text:
        bot.send_message(message.chat.id,
                         text='[🛑] سیزن ئایدیەکات باندە ',
                         reply_markup=markup_inlinee)

    elif 'Login expired' in res.text:
        bot.send_message(message.chat.id,
                         text='[⚠] سیزن ئایدیەکەت بەسەرچووە ',
                         reply_markup=markup_inline)


def check(message):
    listt = open('list.txt', 'r')
    liii = len(listt.readlines())
    listt.close()
    cid = message.chat.id
    mid = message.message_id
    markup_inline = types.InlineKeyboardMarkup()
    sid = types.InlineKeyboardButton(text='دانانی سیزن ئایدی 🆔', callback_data='sid')
    global RunPosts
    RunPosts = True
    markup_inline.add(sid)
    d = 0
    b = 0
    er = 0
    rem = liii
    sidread = open('sessionid.txt', 'r').read()
    sessioniddd = sidread
    if os.path.exists("sessionid.txt"):
        sessionidd = open('sessionid.txt', 'r')
        lis = len(sessionidd.readlines())
        sessionidd.close()
        if lis == 0:
            bot.send_message(message.chat.id, text='[⚠] پێویستە سەرەتا سیزن ئایدی داخڵ بکەیت ')
        else:
            if os.path.exists("list.txt"):
                list = open('list.txt', 'r')
                li = len(list.readlines())
                user = open('list.txt').read().splitlines()
                list.close()
                rem = li
                if li == 0:
                    bot.send_message(message.chat.id, text='Ξ پێویستە سەرەتا لیستێک دروست بکەیت 📜')
                else:
                    while RunPosts == True:
                        for checkusers in user:
                            nowtime = datetime.now()
                            current_time = nowtime.strftime("%H:%M:%S")
                            if rem == 0:
                                bot.send_message(message.chat.id, text='چێک کردن دەستی پێ کرد چاوەڕوانبە  ✅!')
                                s.cookies.clear()
                                s.close()
                                RunPosts = False
                            if not RunPosts:
                                bot.send_message(message.chat.id, text='بۆ وەستاندن ⏸')
                                s.cookies.clear()
                                s.close()
                                break
                            url = f'https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id=' + checkusers + '&app_language=en'
                            headers = {
                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                "User-Agent": generate_user_agent(),
                                "Connection": "Keep-Alive",
                                "Host": "www.tiktok.com",
                                "Accept-Encoding": "gzip, deflate",
                                "Cache-Control": "max-age=0"}
                            data = ""
                            cookies = {'sessionid': sessioniddd}
                            res = s.get(url, data=data, headers=headers, cookies=cookies)
                            if 'This username isn’t available.' in res.text or '"is_valid":false' in res.text or '"is_valid":true' in res.text:
                                if os.path.exists('sessionid.txt'):
                                    if '"status_msg":""' in res.text and '"is_valid":true' in res.text and RunPosts == True:
                                        with open('done.txt', 'a') as x:
                                            x.write(checkusers + '\n')
                                        time.sleep(time_sleep)
                                        rem -= 1
                                        d += 1
                                        bot.edit_message_text(chat_id=cid, text='چێک کردن دەستی پێ کرد ▶\n\n'
                                                                                f'[🆔] : {sidread}\n\n'
                                                                                f'Ξ دانە  : {li}\n\n'
                                                                                f'Ξ دانەی چێک کراو : {checkusers}\n\n'
                                                                                f'[✅] بەردەست : {d}\n\n'
                                                                                f'[❌] بەردەست نیە :   {b}\n\n'
                                                                                f'[⚠] کێشەی تێکەوتووە  :   {er}\n\n'
                                                              , message_id=mid,
                                                              reply_markup=markup_stop)
                                        bot.send_message(message.chat.id,
                                                         text='ئەم یوزەرە دۆزراوە [✅]\n\n'
                                                              f'Ξ یوزەرنەیم : {checkusers}\n\n'
                                                              f'Ξ کاتژمێر {current_time}')

                                    elif '"is_valid":false' in res.text or '' in res.text and RunPosts == True:
                                        time.sleep(time_sleep)
                                        b += 1
                                        rem -= 1
                                        bot.edit_message_text(chat_id=cid, text='چێک کردن دەستی پێ کرد ▶\n\n'
                                                                                f'[🆔] : {sidread}\n\n'
                                                                                f'Ξ دانە  : {li}\n\n'
                                                                                f'Ξ دانەی چێک کراو : {checkusers}\n\n'
                                                                                f'[✅] بەردەست : {d}\n\n'
                                                                                f'[❌] بەردەست نیە :   {b}\n\n'
                                                                                f'[⚠] کێشەی تێکەوتووە  :   {er}\n\n'
                                                              , message_id=mid,
                                                              reply_markup=markup_stop)
                                    else:
                                        time.sleep(time_sleep)
                                        bot.send_message(message.chat.id, text=res.text)
                                        rem -= 1
                                        er += 1
                                        bot.edit_message_text(chat_id=cid, text='چێک کردن دەستی پێ کرد ▶\n\n'
                                                                                f'[🆔] : {sidread}\n\n'
                                                                                f'Ξ دانە  : {li}\n\n'
                                                                                f'Ξ دانەی چێک کراو : {checkusers}\n\n'
                                                                                f'[✅] بەردەست : {d}\n\n'
                                                                                f'[❌] بەردەست نیە :   {b}\n\n'
                                                                                f'[⚠] کێشەی تێکەوتووە  :   {er}\n\n'
                                                              , message_id=mid,
                                                              reply_markup=markup_stop)

                                else:
                                    bot.send_message(message.chat.id, text='Call @ue3ex')
                                    break
                            elif 'Login expired' in res.text:
                                bot.send_message(message.chat.id,
                                                 text='[⚠] سیزن ئایدیەکە ئێکسپایەر بوو',
                                                 reply_markup=markup_inline)
                                requests.session().close()
                                s.cookies.clear()
                                s.close()
                                RunPosts = False
                                break
                            elif '{}' in res.text:
                                bot.send_message(message.chat.id,
                                                 text='[🛑] سیزن ئایدیەکە باند بوو',
                                                 reply_markup=markup_inline)
                                requests.session().close()
                                s.cookies.clear()
                                s.close()
                                RunPosts = False
                                break
                            else:
                                print(res.text)
            elif liii == 0:
                bot.send_message(message.chat.id, text='پێویست سەرەتا لیستێک درووست بکەیت 📜')

            else:
                bot.send_message(message.chat.id, text='پێویست سەرەتا لیستێک درووست بکەیت 📜')


def length(message):
    amount = message.text
    length = bot.send_message(message.chat.id, text='🔢 چەند پیت :')
    bot.register_next_step_handler(length, make, amount)


def files(message):
    file = pathlib.Path("list.txt")
    if file.exists():
        send = open('list.txt', 'rb')
        bot.send_document(message.chat.id, send)
    else:
        bot.send_message(message.chat.id, text='فایل نەدۆزراوە ❌')


def done(message):
    file = pathlib.Path("done.txt")
    if file.exists():
        list = open('done.txt', 'r')
        li = len(list.readlines())
        if li == 0:
            bot.send_message(message.chat.id, text='فایلەکە بەتاڵە  📂')
        else:
            send = open('done.txt', 'rb')
            bot.send_document(message.chat.id, send)
    else:
        bot.send_message(message.chat.id, text='فایلەکە نەدۆزراوە  ❌')


def make(message, amount):
    markup_inline = types.InlineKeyboardMarkup()
    startt = types.InlineKees.InlineKeyboardButton(text='دەست پێکردن ▶', callback_data='start')
    markup_inline.row_width = 2
    markup_inline.add(startt)
    length = message.text
    amount = int(amount)
    length = int(length)
    if os.path.exists("list.txt"):
        bot.send_message(message.chat.id, text='فایل دانراوە بەرێزم بۆ نوێکردنەوە\n'
                                               'دانەی بەردەست رەشبکەرەوە وە دانەیەکی نوێ داخڵ بکە')
    else:
        bot.send_message(message.chat.id, text='⏳ چاوەڕێ بکە تکایە >>>>')
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890_.'
        for user in range(amount):
            user = ''
            for item in range(length):
                user += random.choice(chars)
            with open('list.txt', 'a') as xx:
                xx.write(user + '\n')

        bot.send_message(message.chat.id, text='تەواو بوو ✅', reply_markup=markup_inline)


def deletedone(message):
    if os.path.exists("done.txt"):
        sidf = open("done.txt", "w")
        sidf.write('')
        bot.send_message(message.chat.id, text='فایل بە سەرکەوتووی ڕەشکرایەوە ✅')
    else:
        bot.send_message(message.chat.id, text='🛑 ببورە بەڵام هیچ فایلێک نیە بۆ ڕەشکردنەوە',
                         parse_mode='markdown')


def delete(message):
    markup_inline = types.InlineKeyboardMarkup()
    makee = types.Inlinees.InlineKeyboardButton(text='دروست کردنی لیست 📜', callback_data='make')
    markup_inline.row_width = 2
    markup_inline.add(makee)
    if os.path.exists("list.txt"):
        os.remove("list.txt")
        bot.send_message(message.chat.id, text='فایلەکە ڕەشکرایەوە ✅',
                         reply_markup=markup_inline)
    else:
        bot.send_message(message.chat.id, text='🛑 ببورە بەڵام هیچ فایلێک نیە بۆ ڕەشکردنەوە')


try:
	bot.polling(none_stop=True)
except:
	pass
