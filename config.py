from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "21938068"))
API_HASH = getenv("API_HASH", "c18fd98f3e58484df0aecd95a3d5a6a9")

BOT_TOKEN = getenv("BOT_TOKEN", "6323485353:AAGKwvyeegk6Kh8c2Z7F0pWofoA1xXT5kr4")
OWNER_ID = int(getenv("OWNER_ID", "5787509903"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Room:yuvraj178@cluster1.2yw8l7q.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", "Infinity_XBotz")
