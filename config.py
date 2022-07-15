## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAA6X_cA--zdh2OLgEf3gjX7FvQ1rIFJUdjLlMHpwT5jzPEdWMHx5HeuIBhCz22JobZ9uHad96BAr4CdGg6BmE5cmSyJLPC08MAsYApg3kmiWCa2AU3boKotn0qsiteH325ySxMfZhUV0jtp48RFxuMBLyExR2mhXIH0f8L3Yh-MBwjtb89MAE1e0Y4c6N-YuRzfpbg94QZKHkhRfvF0EghxSBLiV2q49OkFLi54gQvbSrWtUtkGikq-PxYTSZzGDMnE_CpdQW8NQdGHp8Bs5GL8MUEiV4rzGItck8c6YPvkrtQbXUs-PfPD7JBoWM1CToxvKRdrQqFohRTrgVUHKmPebg0hmQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5537253960:AAFFZFtgXJ2ZbiOEU_OoBAtU5fHxRp4HL7o")
BOT_NAME = getenv("BOT_NAME", "m_y_o_zk_bot")
API_ID = int(getenv("API_ID", "18988910"))
API_HASH = getenv("API_HASH", "4944199d77904cd9e4b9d3ff5f999d9a")
OWNER_NAME = getenv("OWNER_NAME", "فايرل ميوزك _ viral music")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ZzZzZ5")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "")
OWNER_ID = getenv("OWNER_ID", "1846354329")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "wxsxr")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! ." تشغيل).split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
