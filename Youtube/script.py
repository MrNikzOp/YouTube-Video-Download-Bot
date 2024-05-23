from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = '__**Hello,** {}!\n\n**Send me the YouTube link of the video you want to upload**__' 

    HOME_TEXT = '__**Hello,** [{update.from_user.first_name}](tg://user?id={update.from_user.id})!\n\n**Send me the YouTube link of the video you want to upload**__'

    HELP_TXT = '✨ Hᴇʟʟᴏ {}!!\n\nWelcome to the YouTube Video Uploader Bot!\n\nTo Upload a YouTube Video, Simply Send me the YouTube link.\n\nEnjoy using the bot!'
    
    ABOUT_TXT = """
╭───────────⍟
├📛 **My Name** : [YouTube Video Uploader Bot](https://t.me/Luffy0000007)
├📢 **Framework** : [Pyrogram 2.0.106](https://docs.pyrogram.org/)
├💮 **Language** : [Python 3.12.3](https://www.python.org)
├👥 **Support Group** : [LUFFY BOTS SUPPORT](https://t.me/Luffy0000007)
├🥏 **Channel** : [LUFFY BOT CHANNEL](https://t.me/Luffy0000007)
├⛲ **Source** : [Click Here](https://github.com/LISA-KOREA/YouTube-Video-Download-Bot)
├🎓 **Developer** : **[ㅤᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ. Anonymous ❂℡](https://t.me/Luffy0000007)**
╰───────────────⍟
"""
HELP_TEXT = """
<b>✨ Hᴇʟʟᴏ {user}.

Mʏ Nᴀᴍᴇ Is {bot}.

Welcome to the YouTube Video Uploader Bot!

To Upload a YouTube Video, Simply Send me the YouTube link.
    
Enjoy using the bot!
╭───────────⍟     
├ /start - Check Bot Online 🔔
├ /help - How To Use The Bot 🆘
├ /about - Something About Me 😌
├ /thumbnail - generate video thumbnail 
╰───────────────⍟
"""
