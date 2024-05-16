from pyrogram import Client, filters
from Youtube.config import Config
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["cmd"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[ 
       		  [ 
       		    InlineKeyboardButton("📡 Sʜᴀʀᴇ Yᴏᴜʀ Lɪɴᴋ" ,url=f"https://t.me/share/url?url=https://t.me/Lufffybro_bot?start={message.from_user.id}") ],
       		     [
       		                    InlineKeyboardButton('👩‍💻ᴅᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/Luffy0000007'),
       		                    InlineKeyboardButton('👥 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/+qveQSMp0Hl9mMzdh'),
       		                ],
                [
                    InlineKeyboardButton('⛔️ ᴄʟᴏꜱᴇ', callback_data='cancel')
                ]
       		    ])
    await message.reply_photo(photo="./775f18aed5f6c9f3e5d332e158c092dd.jpg",
                              caption="**Mʏ ɴᴀᴍᴇ** : [ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ ᴠ4](https://t.me/UploadLinkToFileBot)

**Cʜᴀɴɴᴇʟ** : [Luffy Bᴏᴛs](https://t.me/NT_BOT_CHANNEL)

**Sᴏᴜʀᴄᴇ** : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/LISA-KOREA/UPLOADER-BOT-V4)

**Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ** : [Luffy Bᴏᴛs Sᴜᴘᴘᴏʀᴛ](https://t.me/NT_BOTS_SUPPORT)

**Dᴀᴛᴀʙᴀsᴇ** : [MᴏɴɢᴏDB](https://cloud.mongodb.com)

**Lᴀɴɢᴜᴀɢᴇ :** [Pʏᴛʜᴏɴ 3.12.3](https://www.python.org/)

**Fʀᴀᴍᴇᴡᴏʀᴋ :** [ᴘʏʀᴏɢᴀᴍ 2.0.106](https://docs.pyrogram.org/)

**Dᴇᴠᴇʟᴏᴘᴇʀ :** @Luffy0000007",
                              reply_markup=reply_markup,)
