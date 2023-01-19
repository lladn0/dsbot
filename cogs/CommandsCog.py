from discord.ext import commands
import discord
from discord_components import Button, ButtonStyle


class ComCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.song_queue = {}

    @commands.command()
    async def gender(self, ctx):
        if ctx.channel.id == 978696022190616646:  # под серв
            await ctx.send(
                embed=discord.Embed(title=f"{ctx.author},какой твой пол?"), components=[
                    Button(style=ButtonStyle.blue, label='Мальчик', custom_id='boy'),
                    Button(style=ButtonStyle.red, label='Девочка', custom_id='girl')
                    # Button(style=ButtonStyle.gray, label='Свапнуть роль', custom_id='no_role')
                ], delete_after=10
            )
            # Добавляются айди ролей. Нужно подгонять под сервер
            response = await self.bot.wait_for('button_click')
            await response.respond(type=6)
            member = ctx.message.author
            if response.channel == ctx.channel:
                if response.component.label == 'Мальчик':
                    role = discord.utils.get(ctx.guild.roles, name='bой')
                    await member.add_roles(role)

                elif response.component.label == 'Девочка':
                    role = discord.utils.get(ctx.guild.roles, name='gьорл')
                    await member.add_roles(role)
        await ctx.message.delete()

    @commands.command()
    @commands.has_any_role(978586486511398912, 968910586865926164, 977126932565086219)
    async def clear(self, ctx, arg: int):
        await ctx.channel.purge(limit=arg+1)

    @commands.command()
    @commands.has_any_role(978586486511398912, 968910586865926164)
    async def write(self, ctx, *, arg):
        await ctx.send(arg)
        await ctx.message.delete()

    @commands.command()
    @commands.has_any_role(978586486511398912, 968910586865926164)
    async def join_to_voice(self, ctx):
      try:
        if ctx.voice_client is None:
            await ctx.author.voice.channel.connect()
            await ctx.message.delete()
      except:
        print('Не вышло')

    @commands.command()
    @commands.has_any_role(978586486511398912, 968910586865926164)
    async def leave(self, ctx):
          """
          Comm to leave from a voice channel
          """
          if ctx.author.voice.channel.id == ctx.voice_client.channel.id:
              try:
                  await ctx.voice_client.disconnect()
                  await ctx.message.delete()
              except:
                  pass
    
    
                  
def setup(bot):
    bot.add_cog(ComCog(bot))