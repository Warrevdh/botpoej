import discord
from discord.ext import commands
from discord import app_commands
import requests
from dotenv import load_dotenv
import os

load_dotenv() # This line brings all environment variables from .env into os.environ
class PoejClient(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            GUILD = discord.Object(id=1101966854433538120)
            synced = await self.tree.sync(guild=GUILD)
            print(f'Synced {len(synced)} commands!')
        except Exception as e:
            print(f'Error syncing commands: {e}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content == 'crazy':
            await message.channel.send(f'Crazy? \nI was crazy once \nThey locked me in a room \nA rubber room \nA rubber room with rats \nAnd rats make me crazy')
        if message.content == 'skibidi':
            await message.channel.send('Toilet')


intents = discord.Intents.default()
intents.message_content = True
client = PoejClient(command_prefix='!', intents=intents)

GUILD_ID = discord.Object(id=1101966854433538120)

@client.tree.command(name='poej', description='Show poej!', guild=GUILD_ID)
async def showPoej(interaction: discord.Integration):
    # await interaction.response.send_message('https://cataas.com/cat/gif')
    response = requests.get('https://api.thecatapi.com/v1/images/search')

    if response.url:
        data = response.json()
        await interaction.response.send_message(data[0]['url'])
    else:
        return

client.run(os.environ['BOT_TOKEN'])
