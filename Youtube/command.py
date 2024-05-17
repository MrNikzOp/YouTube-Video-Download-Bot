# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from Youtube.config import Config
from Youtube.script import Translation
from Youtube.forcesub import handle_force_subscribe

########################🎊 Lisa | NT BOTS 🎊######################################################
@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()

# About command handler
@Client.on_message(filters.private & filters.command("about"))
async def about(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return      
    await message.reply_photo(photo="https://telegra.ph/file/97e325476ebe8dd8676ad.jpg", caption="Test")      
    await message.reply_text(
        text=Translation.ABOUT_TXT,
        reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('⛔️ ᴄʟᴏꜱᴇ', callback_data='cancel')]
        ]
    ))


# Start command handler
@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
    #user = message.from_user
    await message.reply_text(
        text=Translation.START_TEXT.format(message.from_user.first_name),
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
                InlineKeyboardButton('⛔️ ᴄʟᴏꜱᴇ', callback_data='cancel')
            ]
        ]
    ))

# Help command handler
@Client.on_message(filters.command("help"))
def help(client, message):
    help_text = """
    __**Welcome to the YouTube Video Uploader Bot!

To upload a YouTube video, simply send me the YouTube link.
    
Enjoy using the bot!**__

    """
    message.reply_text(help_text)


########################🎊 Lisa | NT BOTS 🎊######################################################
