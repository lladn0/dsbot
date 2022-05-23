from discord.ext import commands
import requests, string, discord
from discord_components import DiscordComponents, Button, ButtonStyle
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
# @commands.has_permissions(administrator = True)


@bot.event
async def on_ready():
    DiscordComponents(bot)
    print('bot online')


@bot.command
@commands.has_permissions(administrator=True)
async def clear(ctx):
    await ctx.channel.purge(limit = 100)



@bot.command(name = 'sex')
async def sex(ctx):
    if ctx.channel.id == 977912045267738655: # под серв
        await ctx.send(
            embed=discord.Embed(title="Какой твой пол?"),components=[
                Button(style=ButtonStyle.blue, label='Мальчик', custom_id='boy'),
                Button(style=ButtonStyle.red, label='Девочка', custom_id='girl')
                # Button(style=ButtonStyle.gray, label='Свапнуть роль', custom_id='no_role')
            ], delete_after=30
        )
        # Добавляются айди ролей. Нужно подгонять под сервер
        response = await bot.wait_for('button_click')
        await response.respond(type=6)
        member = ctx.message.author
        if response.channel == ctx.channel:
            if response.component.label == 'Мальчик':
                role = discord.utils.get(ctx.guild.roles, id = 977910921378811924)
                await member.add_roles(role)

            elif response.component.label == 'Девочка':
                role = discord.utils.get(ctx.guild.roles, id = 977911887398318080)
                await member.add_roles(role)
        await ctx.message.delete()

            # elif response.component.label == 'Свапнуть роль':
            #     try:
            #         role = discord.utils.get(ctx.guild.roles, id = 977910921378811924 )
            #         await member.remove_roles(role)
            #         role = discord.utils.get(ctx.guild.roles, id=977911887398318080)
            #         await member.add_roles(role)
            #     except:
            #         role = discord.utils.get(ctx.guild.roles, id=977911887398318080)
            #         await member.remove_roles(role)
            #         role = discord.utils.get(ctx.guild.roles, id=977910921378811924)
            #         await member.add_roles(role)

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel.id == 865213779343966222:
        for guild in bot.guilds:
            category = discord.utils.get(guild.categories, id = 978218896173727764)
            channel_p = await guild.create_voice_channel(name = f'{member.display_name}`s room', category=category)
            await channel_p.set_permissions(member, connect=True, mute_members= True, move_members=True, manage_channels=True)
            await member.move_to(channel_p)
            def check(x,y,z):
                return len(channel_p.members) == 0
            await bot.wait_for('voice_state_update', check=check)
            await channel_p.delete()



# music.
# @bot.command(name='play')
# async def play(ctx, *, arg):
#     data = requests.get(f'https://www.youtube.com/results?search_query={arg}')
#     print(data.text)
#     await ctx.send('123')




bot.run('OTc3ODk3MjA5MTc1NjIxNjcz.G1HxX1.jvrNGE_FYoQDmxfZyzmvV0taQTmC99eArslx0M')
