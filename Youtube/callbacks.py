import os, asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from Youtube.config import Config
from Youtube.script import Translation
from Youtube.forcesub import handle_force_subscribe

PIC = "https://telegra.ph/file/97e325476ebe8dd8676ad.jpg",
########################🎊 Lisa | NT BOTS 🎊######################################################
@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()

@Client.on_callback_query()
async def button(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=Translation.START_TEXT.format(update.from_user.mention),
           # reply_markup=Translation.START_BUTTONS,
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
            text=Translation.START_TEXT.format(update.from_user.mention),
           # reply_markup=Translation.HELP_BUTTONS,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
        [
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
    elif update.data == "premium":
        await update.message.edit_text(
            text=Translation.PREMIUM_DETAILS.format(update.from_user.mention),
           # reply_markup=Translation.ABOUT_BUTTONS,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('Pᴀʏ 100 💰', callback_data='pay'),
            ]
        ]
    ))
