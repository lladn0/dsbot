from discord.ext import commands
import discord
from discord_components import Button, ButtonStyle
import youtube_dl, pafy, ffmpeg


class ComCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.song_queue = {}

    @commands.command()
    async def gender(self, ctx):
        if ctx.channel.id == 985209615883059210:  # под серв
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
                    role = discord.utils.get(ctx.guild.roles, name='boy')
                    await member.add_roles(role)

                elif response.component.label == 'Девочка':
                    role = discord.utils.get(ctx.guild.roles, name='girl')
                    await member.add_roles(role)

    @commands.command()
    # @commands.has_any_role(978586486511398912, 968910586865926164)
    async def clear(self, ctx, arg: int):
        await ctx.channel.purge(limit=arg)

    '''
    music
    '''

    async def join_to_voice(self, ctx):
        """
        Checks if pearson in vc. If True joins to him
        """
        if ctx.author.voice is None:
            return await ctx.send('Зайди в войс')
        if ctx.voice_client is None:
            await ctx.author.voice.channel.connect()

    async def check_queue(self, ctx):
        """
        Checking queue of songs
        """
        if len(self.song_queue[ctx.guild.id]) > 0:
            ctx.voice_client.stop()
            await self.play_song(ctx, self.song_queue[ctx.guild.id][0])
            self.song_queue[ctx.guild.id].pop(0)

    async def search_song(self, amount, song, get_url=False):
        """
        searching the song and returns url of song
        """
        info = await self.bot.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL(
            {'format': 'bestaudio', 'quiet': True}).extract_info(f'ytsearch{amount}:{song}', download=False,
                                                                 ie_key='YoutubeSearch'))
        if len(info['entries']) == 0:
            return None
        return [entry['webpage_url'] for entry in info['entries']] if get_url else None

    async def play_song(self, ctx, song):
        url = pafy.new(song).getbestaudio().url
        FFMPEG_PATH = 'fmpeg.exe'
        ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url, executable=FFMPEG_PATH)))

    @commands.command()
    async def leave(self, ctx):
        """
        Leaves from a voice channel
        """
        if ctx.channel.id == 987274272093380648:
            try:
                await ctx.voice_client.disconnect()
            except:
                pass

    @commands.command()
    async def play(self, ctx, *, song=None):
        """
        Merged functions, that were before.
        """
        if ctx.channel.id == 987274272093380648:
            if song is None:
                return await ctx.send('Укажи название песни после команды, чтобы ее проиграть')

            if ctx.voice_client is None:  # Checks if bot already in vc
                await self.join_to_voice(ctx)

            if ctx.voice_client.is_playing():
                return await ctx.send('Подожди окончания песни, и затем попробуй поставить свою снова')

            if not ('youtu' in song):
                await ctx.send('Поиск песни. Подожди...')
                result = await self.search_song(1, song, get_url=True)

                if result is None:
                    await ctx.send('Песня не найдена')

                song = result[0]

            # if ctx.voice_client.source is not None: # Adding songs in queue
            #     queue_len = len(self.song_queue)
            #
            #     if queue_len > 0:
            #         self.song_queue[ctx.guild.id] = []
            #         self.song_queue[ctx.guild.id].append(song)
            #         return await ctx.send('Твоя песня была записана в очередь. Ее место -', queue_len+1)
            #     else:
            #         return await ctx.send('Максимум очереди песен - 10. Подожди, и потом добавь песню в очередь')

            await self.play_song(ctx, song)
            await ctx.send(f'Сейчас играет:{song}')

    @commands.command()
    async def skip(self, ctx):
        """
        Skips the song, that is playing now
        """
        if ctx.channel.id == 987274272093380648:
            try:
                return await ctx.voice_client.stop()
            except:
                pass

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        voice_state = member.guild.voice_client

        try:
            if len(voice_state.channel.members) == 1:
                await voice_state.disconnect()
        except:
            pass


def setup(bot):
    bot.add_cog(ComCog(bot))