import discord
from discord.ext import commands
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print('ist jetzt aktiv!')
    print('----------------')

@client.async_event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, id="397010173513826306")
    await client.add_roles(member, role)

client.run('NDU5MDc2MjM1MzY5MTE5NzQ0.Dgw7og.aMKdT8tUYG-s5OIkyX9hwzqxxSs')