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


@client.event
async def on_message(message):
    if message.content.lower().startswith('!youtube'):
        if message.channel.id == "474317552936288277":
            await client.send_message(message.channel, "Hier gibt es Videos die dir gefallen könnten : https://goo.gl/8HUkBW")  
        if message.channel.id != "474317552936288277":    
            await client.send_message(message.channel, "Commands bitte nur im #bot Channel eingeben")
#        for role in message.author.roles:
#            if role.name == "Discord Mod":             
    if message.content.lower().startswith('!abo'):
        await client.send_message(message.channel, "Noch kein Abonnent ? Hier kannst du mich abonnieren: https://goo.gl/kHwHVN")
    if message.content.lower().startswith('!server'):
        await client.send_message(message.channel, "Auf diesem Minecraft Server spiele ich gerade: https://unicacity.de Auf dem Server kommst du mit der 1.12 Version der Java Edition")
    if message.content.lower().startswith('!tp'):
        await client.send_message(message.channel, "Mit diesem Texture Pack spiele ich zurzeit: http://bdcraft.net")
    if message.content.lower().startswith('!trinkgeld'):
        await client.send_message(message.channel, "Hier kannst du mir etwas Trinkgeld geben: https://goo.gl/g2N4Vb")
    if message.content.lower().startswith('!twitch'):
        await client.send_message(message.channel, "Du schaust Livestreams lieber auf Twitch ? Hier ist der Link : https://goo.gl/5Kbc3m")
    if message.content.lower().startswith('!twitter'):
        await client.send_message(message.channel, "Hier ist meine Twitter Seite: https://twitter.com/DangerZockt")
    if message.content.lower().startswith('!uploadplan'):
        await client.send_message(message.channel, "Hier ist mein Uploadplan: https://goo.gl/eaJat8")
    if message.content.lower().startswith('!facebook'):
        await client.send_message(message.channel, "Hier ist meine Facebook Seite: https://goo.gl/35VuhR")
    if message.content.lower().startswith('!premium'):
        await client.send_message(message.channel, "Wenn du diesen Command `/geworben Y8DEEH70` auf dem UnicaCity Server eingibst, bekommst du 14 Tage Premium (auf UnicaCity) nachdem du Level 10 auf dem Server erreicht hast.")      
    if message.content.lower().startswith('!commands'):
        await client.send_message(message.channel, "**Hier sind die Commands:**\n\n`!abo` zeigt dir wo du Danger abonnieren kannst.\n`!einladung` gibt dir eine einladung.\n`!facebook` gibt dir den Link zur Facebook Seite von Danger.\n`!premium` beschreibt dir wie du premium auf UnicaCity bekommst.\n`!server` zeigt dir den Server auf dem Danger zurzeit spielt.\n`!tp` zeigt dir das Resource Pack mit dem Danger zurzeit spielt.\n`!trinkgeld` zeigt dir einen Link wo du Danger etwas Trinkgeld hinterlassen kannst.\n`!twitch` gibt dir den Link zu Dangers Twitch Kanal.\n`!twitter` gibt dir den Link zur Twitter Seite von Danger.\n`!uploadplan` gibt dir den Link der dich zum Uploadplan von Danger weiterbringt.\n`!youtube` gibt dir den Link zu Dangers YouTube Kanal.\n`tippspiel` gibt dir den Link zum Tippspiel von Danger.")
    if message.content.lower().startswith('!einladung'):
        await client.send_message(message.channel, "Hier ist ein Link womit du Freunde auf denn Danger Zockt Community Discord Server einladen kannst: https://discord.gg/qmzzm5y .")                                           
    if message.content.lower().startswith('!tippspiel'):
        await client.send_message(message.channel, "Bundesliga Tippspiel 2018/19 - trete der Dangerliga bei! https://dangerliga.webtippspiel.net")                                                
        
@client.async_event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, id="397010173513826306")
    await client.add_roles(member, role)


client.run(os.getenv('TOKEN'))
