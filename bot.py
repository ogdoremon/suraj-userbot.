import os
from pyrogram import Client

# Hum ye details Koyeb/Render ki settings se uthayenge
string_session = os.environ.get("STRING_SESSION")
api_id = 24020709
api_hash = "94a6e04abc379a9ce0a0d2d13f8a8537"

app = Client("my_bot", session_string=string_session, api_id=api_id, api_hash=api_hash)

print("Bot starting...")
app.run()
