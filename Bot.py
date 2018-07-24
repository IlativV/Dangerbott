import discord
form discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print('ist jetzt aktiv!')
    print('----------------')
    
    
@client.event
async def on_message(message):
    if message.content.lower().startswith('!abo'):
        await client.send_message(message.channel, "Noch kein Abonnent ? Hier kannst du mich abonnieren : https://goo.gl/kHwHVN")

@client.async_event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, id="397010173513826306")
    await client.add_roles(member, role)

client.run(os.getenv('TOKEN'))
