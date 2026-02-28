
        
import os
from pyrogram import Client, idle

# Render settings se details uthana
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
STRING_SESSION = os.environ.get("STRING_SESSION")

# Client setup
app = Client(
    "suraj_userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

def start_bot():
    app.start()
    print("Bhai, Tera Userbot Ab 24/7 Live Hai! 🚀")
    idle()
    app.stop()

if __name__ == "__main__":
    start_bot()
    
