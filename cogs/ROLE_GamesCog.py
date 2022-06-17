from discord.ext import commands
import discord
from discord.utils import get


class Emoji_role_games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_any_role(978586486511398912, 968910586865926164)  # Ботовод, Zadrotik
    async def role_games(self, ctx):
        """
        Writes embed text, adds reactions with games` logos
        """
        text = discord.Embed(title="Выбери игры, в которые играешь")
        moji = await ctx.channel.send(embed=text)
        for i in ['Genshin_impact', 'Valorant', 'Dota2', 'LOL', 'SeaOfThieves', 'CSGO']:
            await moji.add_reaction(get(ctx.message.guild.emojis, name=i))



    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        """
        From payload gets message`s id, checks what emoji was sent, gets role, gives role to user
        """
        message_id = payload.message_id
        if message_id == 979076458431512616:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if payload.emoji.name == "Genshin_impact":
                role = discord.utils.get(guild.roles, name='Genshin Impact')
                await member.add_roles(role)
            elif payload.emoji.name == "Valorant":
                role = discord.utils.get(guild.roles, name='Valorant')
                await member.add_roles(role)
            elif payload.emoji.name == "Dota2":
                role = discord.utils.get(guild.roles, name='Dota 2')
                await member.add_roles(role)
            elif payload.emoji.name == "LOL":
                role = discord.utils.get(guild.roles, name='League Of Legends')
                await member.add_roles(role)
            elif payload.emoji.name == "SeaOfThieves":
                role = discord.utils.get(guild.roles, name='Sea Of Thieves')
                await member.add_roles(role)
            elif payload.emoji.name == "CSGO":
                role = discord.utils.get(guild.roles, name='CS:GO')
                await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        """
        From payload gets message`s id, checks what emoji was sent, gets role, removes role from user
        """
        message_id = payload.message_id
        if message_id == 979076458431512616:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if payload.emoji.name == "Genshin_impact":
                role = discord.utils.get(guild.roles, name='Genshin Impact')
                await member.remove_roles(role)
            elif payload.emoji.name == "Valorant":
                role = discord.utils.get(guild.roles, name='Valorant')
                await member.remove_roles(role)
            elif payload.emoji.name == "Dota2":
                role = discord.utils.get(guild.roles, name='Dota 2')
                await member.remove_roles(role)
            elif payload.emoji.name == "LOL":
                role = discord.utils.get(guild.roles, name='League Of Legends')
                await member.remove_roles(role)
            elif payload.emoji.name == "SeaOfThieves":
                role = discord.utils.get(guild.roles, name='Sea Of Thieves')
                await member.remove_roles(role)
            elif payload.emoji.name == "CSGO":
                role = discord.utils.get(guild.roles, name='CS:GO')
                await member.remove_roles(role)


def setup(bot):
    """
    Important thing in discord py cogs. Just adds cog to main code
    """
    bot.add_cog(Emoji_role_games(bot))