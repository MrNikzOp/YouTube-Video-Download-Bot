import os, random 

from pyrogram import Client, filters
from Youtube.config import Config
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)

 @Client.on_message(filters.private & filters.command(["list"]))
await message.reply_photo(photo=random.choice(PICS), caption=HELP_TEXT.format(user=message.from_user.mention, bot=client.mention), reply_markup=reply_markup,)
