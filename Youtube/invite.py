from pyrogram import Client, filters
from Youtube.config import Config
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["invite"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[ 
       		  [ 
       		    InlineKeyboardButton("📡 Sʜᴀʀᴇ Yᴏᴜʀ Lɪɴᴋ" ,url=f"https://t.me/share/url?url=https://t.me/Lufffybro_bot?start={message.from_user.id}") ],
       		     [
       		                    InlineKeyboardButton('👩‍💻ᴅᴇᴠᴇʟᴏᴘᴇʀr', url='https://t.me/Luffy0000007'),
       		                    InlineKeyboardButton('👥 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/+qveQSMp0Hl9mMzdh'),
       		                ]
       		    ])
    await message.reply_photo(photo="./775f18aed5f6c9f3e5d332e158c092dd.jpg",caption="**INVITE YOUR FRIENDS\nEnjoy 📥**", reply_markup=reply_markup,)
