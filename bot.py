import os
import asyncio
from pyrogram import Client

# Ab ye details GitHub se nahi, Render ki settings se aayengi
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
string_session = os.environ.get("STRING_SESSION")

async def main():
    app = Client(
        "suraj_userbot",
        session_string=string_session,
        api_id=api_id,
        api_hash=api_hash
    )
    
    async with app:
        print("Tera Userbot Securely Chalu Ho Gaya Hai! 🚀")
        from pyrogram.methods.utilities.idle import idle
        await idle()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    
