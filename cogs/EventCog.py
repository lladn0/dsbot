from discord.ext import commands
import discord


class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.make_lobby_vc_id = 865213779343966222
        self.bot = bot
        self.ml_category_id = 978218896173727764

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

  
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        """
        Event that checks if somebody is in special voice channel 'make lobby'. If there is somebody, it makes
        special voice channel, that can be configured by this user.
        """
        try:
            category = discord.utils.get(guild.categories, id=self.ml_category_id)
            if after.channel.id == self.make_lobby_vc_id:
                for guild in self.bot.guilds:
                    category = discord.utils.get(guild.categories, id=self.ml_category_id)
                    channel_p = await guild.create_voice_channel(name=f'{member.display_name}`s room', category=category)
                    await channel_p.set_permissions(member, connect=True, mute_members=True, move_members=True,
                                                    manage_channels=True)
                    await member.move_to(channel_p)

                    # Next code
                    def check(x, y ,z):
                        return len(channel_p.members) == 0
                    await self.bot.wait_for('voice_state_update', check=check)
                    await channel_p.delete()

            if after.channel.category == category and len(after.channel.members) == 0:
                await after.channel.delete()
                    

        except:
            pass

def setup(bot):
    """
    Important thing in discord py cogs. Just adds cog to main code
    """
    bot.add_cog(EventsCog(bot))