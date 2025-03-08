import discord
from discord.ext import commands
import random
import asyncio

# Ganti dengan token akunmu
TOKEN = 'NDM0NzQ1MDMwMTgwMjA4NjQx.GQWnhe.RAftPCohe-c72f3gB5Gl0kDePM5dcE9Wbm5LUo'
# Ganti dengan ID channel tempat kamu ingin chatting
CHANNEL_ID = 1027161980970205225

messages = ["momenentum the best", "when next quest?", "lol", "soo cool", "roadmap?"]

bot = commands.Bot(command_prefix='!', self_bot=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(CHANNEL_ID)
    while True:
        message = random.choice(messages)
        await channel.send(message)
        await asyncio.sleep(random.randint(300, 600))

bot.run('NDM0NzQ1MDMwMTgwMjA4NjQx.GQWnhe.RAftPCohe-c72f3gB5Gl0kDePM5dcE9Wbm5LUo')
