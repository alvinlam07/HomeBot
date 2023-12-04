import discord
import os
from dotenv import load_dotenv

load_dotenv()

# bot
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('DISCORD_TOKEN'))