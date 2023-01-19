import discord
import os
from discord.ext import commands
from discord_components import DiscordComponents

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
# @commands.has_permissions(administrator = True)



@bot.event
async def on_ready():
    DiscordComponents(bot)
    print('bot online')


extensions = ['cogs.EventCog', 'cogs.ROLE_GamesCog', 'cogs.CommandsCog']
for i in extensions:
    bot.load_extension(i)



try:
    bot.run('OTc3ODk3MjA5MTc1NjIxNjcz.GKcrpN.Es_ZU7F0W64nyoBgyORIBzwKOy70WV5basbsYo')
except:
    os.system("kill 1")
