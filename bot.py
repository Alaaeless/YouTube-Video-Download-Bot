# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config

# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=Config.API_ID,7802065215
    api_hash=Config.API_HASH,AAHzXDnGhQg3liKw09qwfw5TFXxDT3gNv9k
    bot_token=Config.BOT_TOKEN,7802065215:AAE-tVJsYfNllyE2x-3dsl5oyoDGZnAcpkQ
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
