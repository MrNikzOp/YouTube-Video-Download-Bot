
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


# Start command handler
@Client.on_message(filters.private & filters.command("pst"))
async def start(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
    #user = message.from_user
    await message.reply_photo(
        photo=Translation.LUFFY_IMG,
        caption=Translation.PREMIUM_TXT.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('രോമാഞ്ചം പ്രീമിയം 🔕', callback_data='cancel'),
            ]
        ]
    ))
