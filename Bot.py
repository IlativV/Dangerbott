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
    if message.content.lower().startswith('!'):

        await client.delete_message(message)

        if message.channel.id == "474317552936288277":


            if message.content.lower().startswith('!abo'):
                await client.send_message(message.channel,
                                        "Noch kein Abonnent? Hier kannst du mich abonnieren: https://goo.gl/kHwHVN")
            if message.content.lower().startswith('!server'):
                await client.send_message(message.channel,
                                        "Auf diesem Minecraft Server spiele ich gerade: https://unicacity.de Auf den Server kommst du mit der 1.12 Version der Java Edition")
            if message.content.lower().startswith('!tp'):
                await client.send_message(message.channel,
                                        "Mit diesem Texture Pack spiele ich zurzeit: http://bdcraft.net")
            if message.content.lower().startswith('!trinkgeld'):
                await client.send_message(message.channel,
                                        "Hier kannst du mir etwas Trinkgeld geben: https://www.tipeeestream.com/dangerzockt-lp/tip")
            if message.content.lower().startswith('!twitch'):
                await client.send_message(message.channel,
                                        "Du schaust Livestreams lieber auf Twitch ? Hier ist der Link : https://www.twitch.tv/dangerzockt")
            if message.content.lower().startswith('!twitter'):
                await client.send_message(message.channel,
                                        "Hier ist meine Twitter Seite: https://twitter.com/DangerZockt")
            if message.content.lower().startswith('!uploadplan'):
                await client.send_message(message.channel,
                                        "Hier ist mein Uploadplan: https://goo.gl/eaJat8")
            if message.content.lower().startswith('!facebook'):
                await client.send_message(message.channel,
                                        "Hier ist meine Facebook Seite: https://www.facebook.com/DangerZockt")
            if message.content.lower().startswith('!premium'):
                await client.send_message(message.channel,
                                        "Wenn du diesen Command `/geworben Y8DEEH70` auf dem UnicaCity Server eingibst, bekommst du 14 Tage Premium (auf UnicaCity) nachdem du Level 10 auf dem Server erreicht hast.")
            if message.content.lower().startswith('!commands'):
                await client.send_message(message.channel,
                                        "**Hier sind die Commands:**\n\n`!abo` zeigt dir wo du Danger abonnieren kannst.\n`!einladung` gibt dir eine einladung.\n`!facebook` gibt dir den Link zur Facebook Seite von Danger.\n`!premium` beschreibt dir wie du premium auf UnicaCity bekommst.\n`!server` zeigt dir den Server auf dem Danger zurzeit spielt.\n`!tp` zeigt dir das Resource Pack mit dem Danger zurzeit spielt.\n`!trinkgeld` zeigt dir einen Link wo du Danger etwas Trinkgeld hinterlassen kannst.\n`!twitch` gibt dir den Link zu Dangers Twitch Kanal.\n`!twitter` gibt dir den Link zur Twitter Seite von Danger.\n`!uploadplan` gibt dir den Link der dich zum Uploadplan von Danger weiterbringt.\n`!youtube` gibt dir den Link zu Dangers YouTube Kanal.\n`!tippspiel` gibt dir den Link zum Tippspiel von Danger.")
            if message.content.lower().startswith('!einladung'):
                await client.send_message(message.channel,
                                        "Hier ist ein Link womit du Freunde auf den Danger Zockt Community Discord Server einladen kannst: https://discord.gg/qmzzm5y .")
            if message.content.lower().startswith('!tippspiel'):
                await client.send_message(message.channel,
                                        "Bundesliga Tippspiel 2018/19 - trete der Dangerliga bei! https://dangerliga.webtippspiel.net")
            if message.content.lower().startswith('!instagram'):
                await client.send_message(message.channel,
                                        "Hier ist mein Instagram Account: https://www.instagram.com/dangerzockt")
            if message.content.lower().startswith('!key'):
                await client.send_message(message.channel,
                                        "Günstige Gamekeys auf MMOGA https://mmo.ga/Cp8o")
            if message.content.lower().startswith('!youtube'):
                await client.send_message(message.channel,
                                          "Hier gibt es Videos die dir gefallen könnten : https://www.youtube.com/DangerZockt")



        elif message.author.id == "234379486580178954" or "303343324767715328" or "287861614353448961" :

            if message.content.lower().startswith('!abo'):
                await client.send_message(message.channel,
                                        "*Noch kein Abonnent? Hier kannst du mich abonnieren: https://goo.gl/kHwHVN*")
            if message.content.lower().startswith('!server'):
                await client.send_message(message.channel,
                                        "*Auf diesem Minecraft Server spiele ich gerade: https://unicacity.de Auf den Server kommst du mit der 1.12 Version der Java Edition*")
            if message.content.lower().startswith('!tp'):
                await client.send_message(message.channel,
                                        "*Mit diesem Texture Pack spiele ich zurzeit: http://bdcraft.net*")
            if message.content.lower().startswith('!trinkgeld'):
                await client.send_message(message.channel,
                                        "*Hier kannst du mir etwas Trinkgeld geben: https://www.tipeeestream.com/dangerzockt-lp/tip*")
            if message.content.lower().startswith('!twitch'):
                await client.send_message(message.channel,
                                        "*Du schaust Livestreams lieber auf Twitch ? Hier ist der Link : https://www.twitch.tv/dangerzockt*")
            if message.content.lower().startswith('!twitter'):
                await client.send_message(message.channel,
                                        "*Hier ist meine Twitter Seite: https://twitter.com/DangerZockt*")
            if message.content.lower().startswith('!uploadplan'):
                await client.send_message(message.channel,
                                        "*Hier ist mein Uploadplan: https://goo.gl/eaJat8*")
            if message.content.lower().startswith('!facebook'):
                await client.send_message(message.channel,
                                        "*Hier ist meine Facebook Seite: https://www.facebook.com/DangerZockt*")
            if message.content.lower().startswith('!premium'):
                await client.send_message(message.channel,
                                        "*Wenn du diesen Command `/geworben Y8DEEH70` auf dem UnicaCity Server eingibst, bekommst du 14 Tage Premium (auf UnicaCity) nachdem du Level 10 auf dem Server erreicht hast.*")
            if message.content.lower().startswith('!commands'):
                await client.send_message(message.channel,
                                        "**Hier sind die Commands:**\n\n`!abo` zeigt dir wo du Danger abonnieren kannst.\n`!einladung` gibt dir eine Einladung für den Discord Server.\n`!facebook` gibt dir den Link zur Facebook Seite von Danger.\n`!instagram` gibt dir den Link zur Instagram Seite von Danger.\n`!key` zeigt dir wo du güstig Game Keys und anderes billig kaufen kannst.\n`!premium` beschreibt dir wie du premium auf UnicaCity bekommst.\n`!server` zeigt dir den Server auf dem Danger zurzeit spielt.\n`!tippspiel` gibt dir den Link wo du der Dangerliger beitreten kannst.\n`!tp` zeigt dir das Resource Pack mit dem Danger zurzeit spielt.\n`!trinkgeld` zeigt dir einen Link wo du Danger etwas Trinkgeld hinterlassen kannst.\n`!twitch` gibt dir den Link zu Dangers Twitch Kanal.\n`!twitter` gibt dir den Link zur Twitter Seite von Danger.\n`!uploadplan` gibt dir den Link der dich zum Uploadplan von Danger weiterbringt.\n`!youtube` gibt dir den Link zu Dangers YouTube Kanal.\n`!tippspiel` gibt dir den Link zum Tippspiel von Danger.")
            if message.content.lower().startswith('!einladung'):
                await client.send_message(message.channel,
                                        "*Hier ist ein Link womit du Freunde auf den Danger Zockt Community Discord Server einladen kannst: https://discord.gg/qmzzm5y .*")
            if message.content.lower().startswith('!tippspiel'):
                await client.send_message(message.channel,
                                        "*Bundesliga Tippspiel 2018/19 - trete der Dangerliga bei! https://dangerliga.webtippspiel.net*")
            if message.content.lower().startswith('!instagram'):
                await client.send_message(message.channel,
                                        "*Hier ist mein Instagram Account: https://www.instagram.com/dangerzockt*")
            if message.content.lower().startswith('!key'):
                await client.send_message(message.channel,
                                        "*Günstige Gamekeys auf MMOGA https://mmo.ga/Cp8o*")
            if message.content.lower().startswith('!youtube'):
                await client.send_message(message.channel,
                                          "*Hier gibt es Videos die dir gefallen könnten : https://www.youtube.com/DangerZockt*")

        else:
            await client.send_message(message.channel,
                                      "Commands bitte nur im <#474317552936288277> Channel eingeben!")

    
@client.async_event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, id="397010173513826306")
    await client.add_roles(member, role)


client.run(os.getenv('TOKEN'))
