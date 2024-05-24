from pyrogram import Client, filters
from Youtube.config import Config
from Youtube.script import Translation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply

PIC ="https://telegra.ph/file/97e325476ebe8dd8676ad.jpg",


@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()

@Client.on_callback_query()
async def button(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=Translation.HOME_TEXT,
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
                InlineKeyboardButton('ADMIN', user_id=int(6807518752))
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
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
        [
       	 [
       		 InlineKeyboardButton('✨ Aʙᴏᴜᴛ', callback_data='about'),
       		 ],
            [
            InlineKeyboardButton('« Bᴀᴄᴋ', callback_data='home'),
            InlineKeyboardButton('✘ Cʟᴏꜱᴇ', callback_data='cancel'),
            ]
        ]
    ))        
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
       		                    InlineKeyboardButton('📚 Hᴇʟᴘ', callback_data='help'),
       		                ],
                [
                InlineKeyboardButton('« Bᴀᴄᴋ', callback_data='home'),    
                InlineKeyboardButton('✘ Cʟᴏꜱᴇ', callback_data='cancel'),    
                ]
       		    ])
    await message.reply_photo(photo="./775f18aed5f6c9f3e5d332e158c092dd.jpg",caption="**INVITE YOUR FRIENDS**", reply_markup=reply_markup,)

@Client.on_message(filters.private & filters.command(["details"]))
async def details(client,message):
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
    await message.reply_photo(photo="https://telegra.ph/file/18407905c9e9cb49148aa.jpg",caption="**» രോമാഞ്ചം പ്രീമിയം 🔕\n\n✅ • ᴅᴀɪʟʏ ᴜᴘᴅᴀᴛᴇᴅ\n✅ • ɪᴏꜱ ꜱᴜᴘᴘᴏʀᴛᴇᴅ\n✅ • ꜰᴜʟʟ ᴅɪʀᴇᴄᴛ ᴠɪᴅᴇᴏꜱ\n✅ • ʀᴀʀᴇ ᴄᴏʟʟᴇᴄᴛɪᴏɴꜱ\n✅ • ᴍᴀʟʟᴜ ᴀᴜɴᴛʏ, ɢɪʀʟꜱ, ᴇᴛᴄ… ᴀᴠᴀɪʟᴀʙʟᴇ\n\n\nᴍᴀɴʏ ᴍᴏʀᴇ ꜰᴇᴀᴛᴜʀᴇꜱ 👍🏻\nᴘʀɪᴄᴇ: 100 Rs\n\nᴄʟɪᴄᴋ Pay ʙᴜᴛᴛᴏɴ & ᴘᴀʏ ᴛʜᴇ ᴀᴍᴏᴜɴᴛ ᴀɴᴅ ᴇɴᴊᴏʏ 🫦**", reply_markup=reply_markup,)

@Client.on_message(filters.private & filters.command(["me"]))
async def member(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[ 
       		  [ 
       		    InlineKeyboardButton("📡 Sʜᴀʀᴇ Yᴏᴜʀ Lɪɴᴋ" ,url=f"https://t.me/share/url?url=https://t.me/Lufffybro_bot?start={message.from_user.id}") 
              ],
       		     [
       		                    InlineKeyboardButton('✨ Aʙᴏᴜᴛ', callback_data='about'),
       		                ],
                [
       		                    InlineKeyboardButton('📚 Hᴇʟᴘ', callback_data='help'),
       		                ],
                [
                InlineKeyboardButton('« Bᴀᴄᴋ', callback_data='home'),    
                InlineKeyboardButton('✘ Cʟᴏꜱᴇ', callback_data='cancel'),    
                ]
       		    ])
    await message.reply_photo(photo=PIC,caption=HOME_TEXT, reply_markup=reply_markup,)
