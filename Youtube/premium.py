
import os, asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from Youtube.config import Config
from Youtube.script import Translation
from Youtube.forcesub import handle_force_subscribe

########################🎊 Luffy | RJ BOTS 🎊######################################################
@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()

@Client.on_callback_query(filters.regex("home"))
async def button(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=Translation.PREMIUM_TEXT.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('രോമാഞ്ചം പ്രീമിയം 🔕', callback_data='premium'),
            ],
            [
                InlineKeyboardButton('♻️ Aʙᴏᴜᴛ', callback_data='about'),
            ]
        ]
    ))
        
    elif update.data == "premium":
        await update.message.edit_text(
            text=Translation.PREMIUM_DETAILS.format(update.from_user.mention),
           # reply_markup=Translation.ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "details":
        await update.message.edit_text(
            text=Translation.PREMIUM_DETAILS.format(update.from_user.mention),
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

# Start command handler
@Client.on_message(filters.private & filters.command("pst"))
async def start(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
    #user = message.from_user
 #  m = await message.reply_sticker("CAACAgUAAxkBAAEBvlVk7YKnYxIHVnKW2PUwoibIR2ygGAACBAADwSQxMYnlHW4Ls8gQHgQ")
    # await asyncio.sleep(2)
   # return await m.delete()
    await message.reply_text(
        text=Translation.PREMIUM_TEXT.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('രോമാഞ്ചം പ്രീമിയം 🔕', callback_data='premium'),
            ],
            [
                InlineKeyboardButton('♻️ Aʙᴏᴜᴛ', callback_data='details'),
            ]
        ]
    ))
    
