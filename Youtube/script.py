from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = '__**Hello,** {}!\n\n**Send me the YouTube link of the video you want to upload**__' 

    HOME_TEXT = '__**Hello,** {}!\n\n**Send me the YouTube link of the video you want to upload**__'

    PREMIUM_TEXT = '𝐇𝐄𝐋𝐋𝐎 {}😍👋,\n𝗦𝗲𝗹𝗲𝗰𝘁 𝗧𝗵𝗲 𝗚𝗥𝗢𝗨𝗣 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧🌺‼️\n\nനിങ്ങൾക് ഇഷ്ടമുള്ള ഗ്രുപ്പ് select ചെയ്യുക.!!!'

    LUFFY_IMG = 'https://telegra.ph/file/97e325476ebe8dd8676ad.jpg'

    PREMIUM_DETAILS = '**Hello  {} 🫦\n\n» രോമാഞ്ചം പ്രീമിയം 🔕\n\n✅ • Daily Videos Updated\n✅ • iOS supported\n✅ • Full Direct Videos\n✅ • Rare Collections & Hot Collections\n✅ • Mallu aunty, Girls, etc… available \n\n🔞Many more features 👍🏻\n\nPrice: 100\n\nClick Pay Button, Pay The Amount And JOIN 🫦**'
    
    HELP_TXT = '✨ Hᴇʟʟᴏ {}!!\n\nWelcome to the YouTube Video Uploader Bot!\n\nTo Upload a YouTube Video, Simply Send me the YouTube link.\n\nEnjoy using the bot!'

    INFO_TXT = """<i>
<u>Yᴏᴜʀ Dᴇᴛᴀɪʟꜱ</u>

**○ ID** : <code>{id}</code>
**○ DC** : <code>{dc}</code>
**○ First Name** : <code>{n}<code>
**○ UserName** : @{u}
**○ link** : <code>https://t.me/{u}</code>

Thank You For Using Me❣️</i>"""
    
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

PREMIUM_TXT = """
𝐇𝐄𝐋𝐋𝐎 {}😍👋,
𝗦𝗲𝗹𝗲𝗰𝘁 𝗧𝗵𝗲 𝗚𝗥𝗢𝗨𝗣 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧🌺‼️

**നിങ്ങൾക് ഇഷ്ടമുള്ള ഗ്രുപ്പ് select ചെയ്യുക.!!!**
"""
PREMIUM_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('❔ ʜᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton('⛔️ ᴄʟᴏsᴇ', callback_data='close')
        ]]
)

