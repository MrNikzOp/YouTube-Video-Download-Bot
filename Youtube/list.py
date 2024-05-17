import os, random 

from pyrogram import Client, filters
from Youtube.config import Config
from Youtube.forcesub import handle_force_subscribe
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)

@Client.on_message(filters.private & filters.command("list"))
async def list(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
await message.reply_photo(photo=random.choice(PICS), caption=HELP_TEXT.format(user=message.from_user.mention, bot=client.mention), reply_markup=reply_markup,)
