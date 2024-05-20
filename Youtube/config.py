import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6799891281:AAG7kEpQaujkPfQFmKtFxqWL8CVYE1QD2Qs")
    API_ID = int(os.environ.get("API_ID", 29478734))
    API_HASH = os.environ.get("API_HASH", "8bd53e36eceada3329fbe46d9b961d1f")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1002070853757")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
    PICS = os.environ.get('PICS' ,'https://telegra.ph/file/97e325476ebe8dd8676ad.jpg')
    ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6807518752').split()]
    # add premium logs channel id
    PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002070853757'))
