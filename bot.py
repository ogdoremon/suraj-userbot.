import os
import asyncio
from pyrogram import Client

# Environment variables se data uthana
string_session = os.environ.get("STRING_SESSION")
api_id = 24020709
api_hash = "94a6e04abc379a9ce0a0d2d13f8a8537"

async def main():
    app = Client(
        "suraj_userbot",
        session_string=string_session,
        api_id=api_id,
        api_hash=api_hash
    )
    
    async with app:
        print("Tera Userbot 24/7 Chalu Ho Gaya Hai! 🚀")
        # Bot ko chalu rakhne ke liye idle loop
        from pyrogram.methods.utilities.idle import idle
        await idle()

if __name__ == "__main__":
    # Event loop error se bachne ke liye naya tarika
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
  
