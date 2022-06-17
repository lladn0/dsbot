from discord.ext import commands
import discord
from peewee import *
from discord_components import DiscordComponents
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
# @commands.has_permissions(administrator = True)

conn = SqliteDatabase('level_db')
cursor = conn.cursor()

@bot.event
async def on_ready():
    DiscordComponents(bot)
    print('bot online')


extensions = ['cogs.EventCog', 'cogs.GamesCog', 'cogs.CommandsCog']
for i in extensions:
    bot.load_extension(i)


bot.run('OTc3ODk3MjA5MTc1NjIxNjcz.G1HxX1.jvrNGE_FYoQDmxfZyzmvV0taQTmC99eArslx0M')
