import os
from pyrogram import Client, filters
from pyrogram.types import Message

bot = Client(
    'classplus_bot',
    api_id=int(os.getenv('22470912')),
    api_hash=os.getenv('511be78079ed5d4bd4c967bc7b5ee023'),
    bot_token=os.getenv('8195714950:AAEN5WOiCNPGA5ZwRQkATEIpyieLu1XaWfE')
)

@bot.on_message(filters.command('start'))
async def start_cmd(client, message: Message):
    await message.reply_text('👋 Welcome to Classplus Extractor Bot!')

# You would include /drm, /batch, /txt handlers here

bot.run()
