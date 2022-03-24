from pyrogram import Client
from pyrogram.types import *
import instabot
import os
list_input = []
telenstabot = Client(
    session_name="Telebot",
    api_id=12010694,
    api_hash="32915c5f87292ddf7f6bb9b540494bfb",
    bot_token="5163817138:AAFcEHornWaDWbb2UEEOBDLCxa8IJ2DiDdc",
)
async def start(Client,message):
    await telenstabot.send_message(message.chat.id,f"Hello dear{message.chat.first_name}👋🏻👋🏻\nwelcome to telenstabot🌹🌹")
    instabot.login_insta_1()
async def user_pass(Client,message):
    button = ReplyKeyboardMarkup(keyboard=[
        ['Set username - password ✅']
    ], resize_keyboard=True)
    await telenstabot.send_message(message.chat.id,f"dear{message.chat.first_name}\nplease enter your username/password example => username-password",reply_markup=button)
async def ID(Client,message):
    button = ReplyKeyboardMarkup(keyboard=[
        ['Set ID 🆔']
    ], resize_keyboard=True)
    await telenstabot.send_message(message.chat.id,f"dear{message.chat.first_name}\nplease enter an ID example => username",reply_markup=button)
x = []
@telenstabot.on_message()
async def telensta(Client,message):
    text = message.text
    list_input.append(text)
    if text == '/start':
        await start(Client, message)
        #await user_pass(Client, message)
    #if message.text == 'Set username - password ✅':
        #user_pass_m = list_input[-2]
        #user_pass_m = str(user_pass_m)
        #user_pass_m = user_pass_m.replace(" ", "")
        #username, password = user_pass_m.split("-")
        #try:
            #instabot.login_insta_1(username, password)
        await ID(Client, message)
        #except:
            #button = ReplyKeyboardMarkup(keyboard=[
                #['Set username - password ✅']
            #], resize_keyboard=True)
        #await telenstabot.send_message(message.chat.id,f"dear{message.chat.first_name}\nyour password was wrong \nplease enter an ID example => username",reply_markup=button)
            #instabot.login_insta_1(username, password)
        #await ID(Client, message)
    if text == 'Set ID 🆔':
        button = ReplyKeyboardMarkup(keyboard=[
            ['Story 🌀','Post 💬','Highlight ❇️'],
            ['🔙']
        ], resize_keyboard=True)
        id = list_input[-2]
        id = str(id)
        id = id.replace(" ", "")
        id = id.replace("@", "")
        x.append(id)
        try:
            name_profile = instabot.download_profile(id)
            await telenstabot.send_message(message.chat.id, f"Please wait to download the information ...",reply_markup=button)
        except:
            await telenstabot.send_message(message.chat.id, f"Username was incorrect")
            x.clear()
            id = ""
            await ID(Client, message)
        name = id
        if instabot.is_verified(id) == True:
            name += " ✅"
        await telenstabot.send_photo(message.chat.id,fr'C:\Users\Lenovo\Desktop\bot\{id}\{name_profile}',caption=name+"\n"+instabot.biography(id)+ "\n"*2 +'followers: '+str(instabot.number_of_follower(id))+"\n"+"following: "+str(instabot.number_of_followees(id)),reply_markup=button)
        os.remove(fr'C:\Users\Lenovo\Desktop\bot\{x[0]}\{name_profile}')
    if text == 'Story 🌀':
        instabot.login_insta_1()
        instabot.story(x[0])
        story = instabot.storys()
        for i in story:
            if 'jpg' in i:
                await telenstabot.send_photo(message.chat.id,fr'C:\Users\Lenovo\Desktop\bot\：stories\{i}',caption='image story')
            elif 'mp4' in i:
                await telenstabot.send_video(message.chat.id,fr'C:\Users\Lenovo\Desktop\bot\：stories\{i}',caption='video story')
        dir = os.listdir(fr'C:\Users\Lenovo\Desktop\bot\：stories')
        for i in dir:
            os.remove(fr'C:\Users\Lenovo\Desktop\bot\：stories\{i}')
        if len(dir) == 0:
            await telenstabot.send_message(message.chat.id,'There isn\'t story 😕.')
        else:
            await telenstabot.send_message(message.chat.id,'Story are over 😃.')
    elif text == 'Post 💬':
        instabot.login_insta_1()
        instabot.post(x[0])
        posts = instabot.posts(x[0])
        instabot.login_insta_1()
        captions = instabot.caption(x[0])
        for i in range(len(posts)):
            if 'jpg' in posts[i]:
                await telenstabot.send_photo(message.chat.id,fr'C:\Users\Lenovo\Desktop\bot\{x[0]}\{posts[i]}',caption=captions[i])
            elif 'mp4' in posts[i]:
                await telenstabot.send_video(message.chat.id,fr'C:\Users\Lenovo\Desktop\bot\{x[0]}\{posts[i]}',caption=captions[i])
        if len(posts) == 0:
            await telenstabot.send_message(message.chat.id,'There isn\'t story 😕.')
        else:
            await telenstabot.send_message(message.chat.id,'Story are over 😃.')
    elif text == 'Highlight ❇️':
        instabot.login_insta_1()
        instabot.highlight(x[0])
        dict = instabot.highlights(x[0])
        print(dict)
        dict_keys = []
        dict_values = []
        for i in dict:
            dict_keys.append(i)
        for i in dict.values():
            dict_values.append(i[len(x[0])+1:])
        for i in range(len(dict)):
            if 'jpg' in dict_keys[i] or 'webp' in dict_keys[i]:
                await telenstabot.send_photo(message.chat.id,dict_keys[i],caption=dict_values[i])
            elif 'mp4' in dict_keys[i]:
                await telenstabot.send_video(message.chat.id,dict_keys[i],caption=dict_values[i])
        if len(dict) == 0:
            await telenstabot.send_message(message.chat.id,'There isn\'t highlight 😕.')
        else:
            await telenstabot.send_message(message.chat.id,'Highlights are over 😃.')
    if text == "🔙":
        x.clear()
        await ID(Client, message)

telenstabot.run()