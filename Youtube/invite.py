from pyrogram import Client, filters
from Youtube.config import Config
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)

@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()

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
    
@Client.on_message(filters.private & filters.command(["invite"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[ 
       		  [ 
       		    InlineKeyboardButton("📡 Sʜᴀʀᴇ Yᴏᴜʀ Lɪɴᴋ" ,url=f"https://t.me/share/url?url=https://t.me/Lufffybro_bot?start={message.from_user.id}") 
              ],
       		     [
       		                    InlineKeyboardButton('✨ Aʙᴏᴜᴛ', callback_data='about'),
       		                ],
                [
                InlineKeyboardButton('« Bᴀᴄᴋ', callback_data='home'),    
                InlineKeyboardButton('✘ Cʟᴏꜱᴇ', callback_data='cancel'),    
                ]
       		    ])
    await message.reply_photo(photo="./775f18aed5f6c9f3e5d332e158c092dd.jpg",caption="**INVITE YOUR FRIENDS**", reply_markup=reply_markup,)
