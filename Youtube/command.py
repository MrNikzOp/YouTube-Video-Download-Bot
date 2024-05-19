# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot
import os, asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from Youtube.config import Config
from Youtube.script import Translation
from Youtube.forcesub import handle_force_subscribe

PICS = "https://telegra.ph/file/97e325476ebe8dd8676ad.jpg"
########################🎊 Lisa | NT BOTS 🎊######################################################
@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()

@Client.on_callback_query()
async def button(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=Translation.START_TEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('📍 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/https://t.me/+qveQSMp0Hl9mMzdh'),
            ],
            [
                InlineKeyboardButton('👩‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/Luffy0000007'),
                InlineKeyboardButton('👥 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/+qveQSMp0Hl9mMzdh'),
            ],
            [
                InlineKeyboardButton('♻️ Aʙᴏᴜᴛ', callback_data='about'),
                InlineKeyboardButton('✘ Cʟᴏꜱᴇ', callback_data='cancel'),
            ]
        ]
    ))
        
    elif update.data == "help":
        await update.message.edit_text(
            text=Translation.HELP_TXT,
            reply_markup=Translation.ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=Translation.ABOUT_TXT,
           # reply_markup=Translation.ABOUT_BUTTONS,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
        [
            [
            InlineKeyboardButton('« Bᴀᴄᴋ', callback_data='home'),
            InlineKeyboardButton('✘ Cʟᴏꜱᴇ', callback_data='cancel'),
            ]
        ]
    ))
        
            
# About command handler
@Client.on_message(filters.private & filters.command("about"))
async def about(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return      
  #  await message.reply_photo(photo="https://telegra.ph/file/97e325476ebe8dd8676ad.jpg", caption="Test")      
    await message.reply_photo(
        chat_id=message.from_user.id,
        photo="https://telegra.ph/file/97e325476ebe8dd8676ad.jpg", 
        caption="╭───────────⍟\n├📛 **My Name** : [YouTube Video Uploader Bot](https://t.me/YouTubeUploaderOneBot)\n├📢 **Framework** : [Pyrogram 2.0.106](https://docs.pyrogram.org/)\n├💮 **Language** : [Python 3.12.3](https://www.python.org)\n├👥 **Support Group** : [NT BOTS SUPPORT](https://t.me/NT_BOTS_SUPPORT)\n├🥏 **Channel** : [NT BOT CHANNEL](https://t.me/NT_BOT_CHANNEL)\n├⛲ **Source** : [Click Here](https://github.com/LISA-KOREA/YouTube-Video-Download-Bot)\n├🎓 **Developer** : [LISA 👑](https://t.me/Luffy0000007)\n╰───────────────⍟",
       # text=Translation.ABOUT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('« Bᴀᴄᴋ', callback_data='home'),
                InlineKeyboardButton('✘ Cʟᴏꜱᴇ', callback_data='cancel'),
            ]
        ]
    ))


# Start command handler
@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
    #user = message.from_user
    await message.reply_text(
        text=Translation.START_TEXT.format(message.from_user.first_name),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('📍 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/https://t.me/+qveQSMp0Hl9mMzdh'),
            ],
            [
                InlineKeyboardButton('👩‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/Luffy0000007'),
                InlineKeyboardButton('👥 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/+qveQSMp0Hl9mMzdh'),
            ],
            [
                InlineKeyboardButton('♻️ Aʙᴏᴜᴛ', callback_data='about'),
                InlineKeyboardButton('✘ Cʟᴏꜱᴇ', callback_data='cancel'),
            ]
        ]
    ))
    
# Help command handler
@Client.on_message(filters.command("help"))
def help(client, message):
    help_text = """
    **Welcome to the YouTube Video Uploader Bot!

To upload a YouTube video, simply send me the YouTube link.
    
Enjoy using the bot!**

    """
    message.reply_text(help_text)

# [ LuffyBot ] #

########################🎊 Lisa | NT BOTS 🎊######################################################
