import discord
from discord.ext.commands import Bot
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


@bot.command(pass_context=True)
async def lul(ctx):
    if ctx.message.channel.id == "bot":
        await client.send_message(message.channel, "Hier gibt es Videos die dir gefallen könnten : https://goo.gl/8HUkBW")
        
@client.async_event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, id="397010173513826306")
    await client.add_roles(member, role)


client.run(os.getenv('TOKEN'))
