import os
import asyncio
from pyrogram import Client, idle

# Render settings se data uthana
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
string_session = os.environ.get("STRING_SESSION")

async def start_bot():
    app = Client(
        "suraj_userbot",
        session_string=string_session,
        api_id=api_id,
        api_hash=api_hash
    )
    
    await app.start()
    print("Bhai, Tera Userbot 24/7 Chalu Ho Gaya Hai! 🚀")
    await idle()
    await app.stop()

if __name__ == "__main__":
    # Naye Python versions ke liye sabse sahi tarika
    try:
        asyncio.run(start_bot())
    except (KeyboardInterrupt, SystemExit):
        pass
        
