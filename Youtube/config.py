import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6799891281:AAG7kEpQaujkPfQFmKtFxqWL8CVYE1QD2Qs")
    API_ID = int(os.environ.get("API_ID", 29478734))
    API_HASH = os.environ.get("API_HASH", "8bd53e36eceada3329fbe46d9b961d1f")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
