class Translation(object):

    START_TEXT = '__**Hello,** {}!\n\n**Send me the YouTube link of the video you want to upload**__' 

    ABOUT_TXT = """
╭───────────⍟
├📛 **My Name** : [YouTube Video Uploader Bot](https://t.me/Luffy0000007)
├📢 **Framework** : [Pyrogram 2.0.106](https://docs.pyrogram.org/)
├💮 **Language** : [Python 3.12.3](https://www.python.org)
├👥 **Support Group** : [LUFFY BOTS SUPPORT](https://t.me/Luffy0000007)
├🥏 **Channel** : [LUFFY BOT CHANNEL](https://t.me/Luffy0000007)
├⛲ **Source** : [Click Here](https://github.com/LISA-KOREA/YouTube-Video-Download-Bot)
├🎓 **Developer** : [ㅤᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ. Anonymous ❂℡](https://t.me/Luffy0000007)
╰───────────────⍟
"""
HELP_TEXT = """
**Welcome to the YouTube Video Uploader Bot!

To upload a YouTube video, simply send me the YouTube link.
    
Enjoy using the bot!**
"""

    PROGRESS = """
🏎️ Sᴘᴇᴇᴅ : {3}/s\n\n
✅ Dᴏɴᴇ : {1}\n\n
🟰 Tᴏᴛᴀʟ sɪᴢᴇ  : {2}\n\n
⏳ Tɪᴍᴇ ʟᴇғᴛ : {4}\n\n
"""


    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙️ sᴇᴛᴛɪɴɢs', callback_data='OpenSettings')
        ],[
        InlineKeyboardButton('❔ ʜᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('👨‍🚒 ᴀʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton('⛔️ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('👨‍🚒 ᴀʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton('⛔️ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('❔ ʜᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton('⛔️ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⛔️ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    TEXT = "sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴛᴏ sᴇᴛ ɪᴛ"
