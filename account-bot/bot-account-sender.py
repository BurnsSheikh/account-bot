import telebot
from telebot import util, types
import random
import time

API_TOKEN = '5428836071:AAETpXDfhdzgDBN2sudi-st66MiqlvwRcHI'
    # sostituisci x con id:codice
bot = telebot.TeleBot(API_TOKEN)


                            ### sezione pre

groupchat = -1001188404328

canalesave =  -1001783207797

                            ### fine sezione pre

        ### sezione cmd

@bot.message_handler(commands=['start'])
def send_welcome(message):
    mkup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dev 🧑‍💻", url="t.me/piteasy")
    mkup.add(url_button)

    name = str(message.from_user.id)
    f = str(message.from_user.first_name)
    i = str(message.from_user.id)
    bot.reply_to(message, """🙋‍♂️ Ciao <a href='tg://user?id="""+i+"""'>""" + f + """</a>"""+""", benvenuto nel bot di @SusySeLLer questo bot permette di generare <b>vari account</b>, usa /cmd per <b>scoprire i comandi</b> """, parse_mode="HTML", reply_markup=mkup)

    u = str(message.from_user.username)
    bot.send_message(chat_id=canalesave, text="@"+u+" ha avviato il bot")

@bot.message_handler(commands=['cmd'])
def send_cmd(message):
    name = str(message.from_user.id)
    f = str(message.from_user.first_name)
    i = str(message.from_user.id)
    bot.reply_to(message, """🙋‍♂️ Ciao <a href='tg://user?id="""+i+"""'>""" + f + """</a>"""+""", ecco a te i comandi del bot :

/start
/cmd

!netflix
!crunchyroll
!dazn
!disney
!fortnite
!nordvpn
!nowtv
!onlyfans
!spotify """, parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "!netflix")
def net_id(message):
    if message.chat.id == groupchat:
        with open("netflix.txt","r") as file:
            x = file.read()
            lista = [ a.strip() for a in x.split(" ") if a]
            acc = random.choice(lista)
            i = str(message.from_user.id)
            bot.send_message(chat_id=i, text="ecco il tuo account netflix ⇨<code> " + acc +"</code>", parse_mode="HTML")
            if message.chat.id == groupchat:
                bot.reply_to(message, "il tuo account è stato inviato in privato, assicurati ti aver già avviato questo bot.", parse_mode="HTML")

                u = str(message.from_user.username)
                bot.send_message(chat_id=canalesave, text="@"+u+" ha generato un account netflix")
    else:
        bot.reply_to(message, "non puoi utilizzare questo comando", parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "!crunchyroll")
def crunchyroll_id(message):
    if message.chat.id == groupchat:
        with open("crunchyroll.txt","r") as file:
            x = file.read()
            lista = [ a.strip() for a in x.split(" ") if a]
            acc = random.choice(lista)
            i = str(message.from_user.id)
            bot.send_message(chat_id=i, text="ecco il tuo account crunchyroll ⇨<code> " + acc +"</code>", parse_mode="HTML")
            if message.chat.id == groupchat:
                bot.reply_to(message, "il tuo account è stato inviato in privato, assicurati ti aver già avviato questo bot.", parse_mode="HTML")

                u = str(message.from_user.username)
                bot.send_message(chat_id=canalesave, text="@"+u+" ha generato un account crunchyroll")
    else:
        bot.reply_to(message, "non puoi utilizzare questo comando", parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "!dazn")
def dazn_id(message):
    if message.chat.id == groupchat:
        with open("dazn.txt","r") as file:
            x = file.read()
            lista = [ a.strip() for a in x.split(" ") if a]
            acc = random.choice(lista)
            i = str(message.from_user.id)
            bot.send_message(chat_id=i, text="ecco il tuo account dazn ⇨<code> " + acc +"</code>", parse_mode="HTML")
            if message.chat.id == groupchat:
                bot.reply_to(message, "il tuo account è stato inviato in privato, assicurati ti aver già avviato questo bot.", parse_mode="HTML")

                u = str(message.from_user.username)
                bot.send_message(chat_id=canalesave, text="@"+u+" ha generato un account dazn")
    else:
        bot.reply_to(message, "non puoi utilizzare questo comando", parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "!disney")
def disney_id(message):
    if message.chat.id == groupchat:
        with open("disney.txt","r") as file:
            x = file.read()
            lista = [ a.strip() for a in x.split(" ") if a]
            acc = random.choice(lista)
            i = str(message.from_user.id)
            bot.send_message(chat_id=i, text="ecco il tuo account disney ⇨<code> " + acc +"</code>", parse_mode="HTML")
            if message.chat.id == groupchat:
                bot.reply_to(message, "il tuo account è stato inviato in privato, assicurati ti aver già avviato questo bot.", parse_mode="HTML")

                u = str(message.from_user.username)
                bot.send_message(chat_id=canalesave, text="@"+u+" ha generato un account disney")
    else:
        bot.reply_to(message, "non puoi utilizzare questo comando", parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "!fortnite")
def fortnite_id(message):
    if message.chat.id == groupchat:
        with open("fortnite.txt","r") as file:
            x = file.read()
            lista = [ a.strip() for a in x.split(" ") if a]
            acc = random.choice(lista)
            i = str(message.from_user.id)
            bot.send_message(chat_id=i, text="ecco il tuo account fortnite ⇨<code> " + acc +"</code>", parse_mode="HTML")
            if message.chat.id == groupchat:
                bot.reply_to(message, "il tuo account è stato inviato in privato, assicurati ti aver già avviato questo bot.", parse_mode="HTML")

                u = str(message.from_user.username)
                bot.send_message(chat_id=canalesave, text="@"+u+" ha generato un account fortnite")
    else:
        bot.reply_to(message, "non puoi utilizzare questo comando", parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "!nordvpn")
def nordvpn_id(message):
    if message.chat.id == groupchat:
        with open("nordvpn.txt","r") as file:
            x = file.read()
            lista = [ a.strip() for a in x.split(" ") if a]
            acc = random.choice(lista)
            i = str(message.from_user.id)
            bot.send_message(chat_id=i, text="ecco il tuo account nordvpn ⇨<code> " + acc +"</code>", parse_mode="HTML")
            if message.chat.id == groupchat:
                bot.reply_to(message, "il tuo account è stato inviato in privato, assicurati ti aver già avviato questo bot.", parse_mode="HTML")

                u = str(message.from_user.username)
                bot.send_message(chat_id=canalesave, text="@"+u+" ha generato un account nordvpn")
    else:
        bot.reply_to(message, "non puoi utilizzare questo comando", parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "!nowtv")
def nowtv_id(message):
    if message.chat.id == groupchat:
        with open("nowtv.txt","r") as file:
            x = file.read()
            lista = [ a.strip() for a in x.split(" ") if a]
            acc = random.choice(lista)
            i = str(message.from_user.id)
            bot.send_message(chat_id=i, text="ecco il tuo account nowtv ⇨<code> " + acc +"</code>", parse_mode="HTML")
            if message.chat.id == groupchat:
                bot.reply_to(message, "il tuo account è stato inviato in privato, assicurati ti aver già avviato questo bot.", parse_mode="HTML")

                u = str(message.from_user.username)
                bot.send_message(chat_id=canalesave, text="@"+u+" ha generato un account nowtv")
    else:
        bot.reply_to(message, "non puoi utilizzare questo comando", parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "!onlyfans")
def onlyfans_id(message):
    if message.chat.id == groupchat:
        with open("onlyfans.txt","r") as file:
            x = file.read()
            lista = [ a.strip() for a in x.split(" ") if a]
            acc = random.choice(lista)
            i = str(message.from_user.id)
            bot.send_message(chat_id=i, text="ecco il tuo account onlyfans ⇨<code> " + acc +"</code>", parse_mode="HTML")
            if message.chat.id == groupchat:
                bot.reply_to(message, "il tuo account è stato inviato in privato, assicurati ti aver già avviato questo bot.", parse_mode="HTML")

                u = str(message.from_user.username)
                bot.send_message(chat_id=canalesave, text="@"+u+" ha generato un account onlyfans")
    else:
        bot.reply_to(message, "non puoi utilizzare questo comando", parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "!spotify")
def spotify_id(message):
    if message.chat.id == groupchat:
        with open("spotify.txt","r") as file:
            x = file.read()
            lista = [ a.strip() for a in x.split(" ") if a]
            acc = random.choice(lista)
            i = str(message.from_user.id)
            bot.send_message(chat_id=i, text="ecco il tuo account spotify ⇨<code> " + acc +"</code>", parse_mode="HTML")
            if message.chat.id == groupchat:
                bot.reply_to(message, "il tuo account è stato inviato in privato, assicurati ti aver già avviato questo bot.", parse_mode="HTML")

                u = str(message.from_user.username)
                bot.send_message(chat_id=canalesave, text="@"+u+" ha generato un account spotify")
    else:
        bot.reply_to(message, "non puoi utilizzare questo comando", parse_mode="HTML")

        ### fine sezione cmd

### end

if __name__ == '__main__':
     bot.infinity_polling(timeout=20, long_polling_timeout = 10)

# BOT CREATO DA @P1etr0_p3rfetto SOLO ED ESCLUSIVAMENTE PER @SusySeLLer
    # @SusySeLLer NON È AUTORIZZATO ALLA VENDITA DI QUESTO BOT
        #IN CASO DI PROBLEMI RELATIVI ALLE PRECEDENTI INFO CONTATTATE @P1etr0_p3rfetto@P1etr0_p3rfetto
