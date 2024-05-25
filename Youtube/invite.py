from pyrogram import Client, filters
from Youtube.config import Config
from Youtube.script import Translation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply

PIC ="https://telegra.ph/file/97e325476ebe8dd8676ad.jpg",


@Client.on_message(filters.private & filters.command(["invite"]))
async def refer(client,message):
 #   await message.react(emoji="🔥")
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
    await message.reply_photo(photo="https://telegra.ph/file/26f266c4dae9930625cb6.jpg, https://telegra.ph/file/72b1efaa44944d2b9e1b9.jpg",caption="**» രോമാഞ്ചം പ്രീമിയം 🔕\n\n✅ • ᴅᴀɪʟʏ ᴜᴘᴅᴀᴛᴇᴅ\n✅ • ɪᴏꜱ ꜱᴜᴘᴘᴏʀᴛᴇᴅ\n✅ • ꜰᴜʟʟ ᴅɪʀᴇᴄᴛ ᴠɪᴅᴇᴏꜱ\n✅ • ʀᴀʀᴇ ᴄᴏʟʟᴇᴄᴛɪᴏɴꜱ\n✅ • ᴍᴀʟʟᴜ ᴀᴜɴᴛʏ, ɢɪʀʟꜱ, ᴇᴛᴄ… ᴀᴠᴀɪʟᴀʙʟᴇ\n\n\nᴍᴀɴʏ ᴍᴏʀᴇ ꜰᴇᴀᴛᴜʀᴇꜱ 👍🏻\nᴘʀɪᴄᴇ: 100 Rs\n\nᴄʟɪᴄᴋ Pay ʙᴜᴛᴛᴏɴ & ᴘᴀʏ ᴛʜᴇ ᴀᴍᴏᴜɴᴛ ᴀɴᴅ ᴇɴᴊᴏʏ 🫦**", reply_markup=reply_markup,)

@Client.on_message(filters.private & filters.command(["me"]))
async def me(client, message):
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
    await message.reply_photo(photo="https://telegra.ph/file/97e325476ebe8dd8676ad.jpg",caption=Translation.HOME_TEXT.format(message.from_user.first_name), reply_markup=reply_markup,)
