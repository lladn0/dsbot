from discord.ext import commands
import discord


class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        Deletes all messages in chat for gender choice(because stupid people sometimes write there "funny" jokes, insted of command)
        """
        if message.channel.id == 985209615883059210 and message.author.bot == False:
            await message.delete()


    @commands.Cog.listener()
    async def on_member_join(self, member):
        """
        Adds a basic role for new people.
        """
        role = discord.utils.get(member.guild.roles, name='Chelik')
        await member.add_roles(role)

def setup(bot):
    """
    Important thing in discord py cogs. Just adds cog to main code
    """
    bot.add_cog(EventsCog(bot))