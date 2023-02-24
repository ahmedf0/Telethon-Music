import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "27882738"))
    API_HASH = os.environ.get("API_HASH", "5611a2d437fadf322c3166d5cf3c28b6")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5863690899:AAFC4JYNCcHWG6Y-ljwZpczJDFZKJh0l5Kg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BAAjpTA1BDBIZsDH9wsvi5ofLLkxrKq290UMMbVzXeRNm3HPconfotWLJ2SUzUZSUJ2GXxNiy9_269W7uiPxzBHsf-4koza267M5oT35inuz81Rh1YgCPUePYiM_xRx8kcxnAnVSVdw-UPfQ4Mvj3hb-xZ1GfDWR-Q_qLKz8o1Pe1YQ90AhTix3lWVvBqAGwtJdKZy2cUdPfntjOxBQtjcLaAGlsO8PzuA6Tz2cg9MMK9xeR_y5uuWUSrCptMrKN3c5J3HQJVRAA6rm5VbjT86AdS_U-B_E3UXemUKoPjyi4mtosrcHQkv7v6zFmVWL2V5GvCIYhMzAqGmjjvjZPnZfaAAAAAXU2HF0A")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
