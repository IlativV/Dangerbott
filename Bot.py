import discord
from discord.ext import commands
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print('ist jetzt aktiv!')
    print('----------------')
  
async def on_message(message):
    if message.content.lower().startswith('!abo'):
        await client.send_message(message.channel, "Noch kein Abonnent ? Hier kannst du mich abonnieren : https://goo.gl/kHwHVN")

@client.async_event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, id="397010173513826306")
    await client.add_roles(member, role)

client.run('NDU5MDc2MjM1MzY5MTE5NzQ0.Dgw7og.aMKdT8tUYG-s5OIkyX9hwzqxxSs')
