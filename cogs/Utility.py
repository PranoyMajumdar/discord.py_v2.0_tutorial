import discord, typing
from typing import Union, Optional
from discord.ext import commands
from discord import app_commands

class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    # @commands.command()
    # async def ping(self, ctx):
    #     embed=discord.Embed(title="Bot Ping", description=f"My ping is {round(self.bot.latency * 1000)}ms", color=0xff0000)
    #     await ctx.send(embed=embed)

    # @app_commands.command(name='ping', description='Bot latency')
    # async def _ping(self, ctx: discord.Interaction):
    #     embed=discord.Embed(title="Bot Ping", description=f"My ping is {round(self.bot.latency * 1000)}ms", color=0xff0000)
    #     await ctx.response.send_message(embed=embed)

    @commands.hybrid_command(name='kuch',description='Shows the bot latency')
    async def ping(self, ctx):
        embed=discord.Embed(title="Bot Ping", description=f"My ping is {round(self.bot.latency * 1000)}ms", color=0xff0000)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='pfp', description='Shows the user avatar')
    async def avatar(self, ctx, user: Optional[Union[discord.Member, discord.User]]):


        if not user: user = ctx.author
        embed = discord.Embed(colour=0x303236)
        embed.set_image(url=user.display_avatar.url)
        av_button = discord.ui.Button(label='Download', url=user.display_avatar.url, emoji='⬇️')
        view = discord.ui.View()
        view.add_item(av_button)
        await ctx.send(embed=embed, view=view)






async def setup(bot: commands.Bot):
    await bot.add_cog(Misc(bot))