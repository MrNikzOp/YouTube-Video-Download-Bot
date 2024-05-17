import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6799891281:AAG7kEpQaujkPfQFmKtFxqWL8CVYE1QD2Qs")
    API_ID = int(os.environ.get("API_ID", 29478734))
    API_HASH = os.environ.get("API_HASH", "8bd53e36eceada3329fbe46d9b961d1f")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1002070853757")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
    PICS = (environ.get('PICS' ,'https://graph.org/file/01ddfcb1e8203879a63d7.jpg https://graph.org/file/d69995d9846fd4ad632b8.jpg https://graph.org/file/a125497b6b85a1d774394.jpg https://graph.org/file/43d26c54d37f4afb830f7.jpg https://graph.org/file/60c1adffc7cc2015f771c.jpg https://graph.org/file/d7b520240b00b7f083a24.jpg https://graph.org/file/0f336b0402db3f2a20037.jpg https://graph.org/file/39cc4e15cad4519d8e932.jpg https://graph.org/file/d59a1108b1ed1c6c6c144.jpg https://te.legra.ph/file/3a4a79f8d5955e64cbb8e.jpg https://graph.org/file/d69995d9846fd4ad632b8.jpg')).split()
