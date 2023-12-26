from os import path, getenv

class Config:
    API_ID = "8605278"
    API_HASH = "c4c4027fb3e88ca3ab5a86c532f0e5de"
    BOT_TOKEN = "6918090292:AAGexWYEKotU-lx300PX6ayW3LKwoZO1wkw"
    FSUB = "c_v_link"
    CHID = "-1001639613245"
    SUDO = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('SUDO', '1130533615').split()]
    MONGO_URI = "mongodb+srv://pmx:pmx@cluster0.s3qt5.mongodb.net/?retryWrites=true&w=majority"
    
cfg = Config()

