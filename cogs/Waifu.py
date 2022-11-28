import discord
import aiohttp
from aiohttp import ClientSession
from discord.ext import commands
       


class Waifus(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def getWaifu(self, tag):
        async with ClientSession() as resp:
            async with resp.get(f'https://api.waifu.im/search/?included_tags={tag}') as response:
                data = await response.json()
        return data['images'][0]['url']

    @commands.hybrid_group(name='anime', description='Get anime pics!')
    async def anime(self, ctx):
        pass
    @anime.command(name='uniform', description='Get waifu related to uniform!')
    async def uniform(self, ctx):
        await ctx.send(
            embed=discord.Embed().set_image(url=await self.getWaifu('uniform'))
        )
    
    @anime.command(name='maid', description='Get waifu related to maid')
    async def maid(self, ctx):
        await ctx.send(
            embed=discord.Embed().set_image(url=await self.getWaifu('maid'))
        )
    
    @anime.command(name='waifu', description='Get waifu related to waifu')
    async def waifu(self, ctx):
        await ctx.send(
            embed=discord.Embed().set_image(url=await self.getWaifu('waifu'))
        )
    @anime.command(name='marin-kitagawa', description='Get waifu related to marin-kitagawa')
    async def marin_kitagawa(self, ctx):
        await ctx.send(
            embed=discord.Embed().set_image(url=await self.getWaifu('marin-kitagawa'))
        )
    
    @anime.command(name='mori-calliope', description='Get waifu related to mori-calliope')
    async def mori_calliope(self, ctx):
        await ctx.send(
            embed=discord.Embed().set_image(url=await self.getWaifu('mori-calliope'))
        )

    @anime.command(name='raiden-shogun', description='Get waifu related to raiden-shogun')
    async def raiden_shogun(self, ctx):
        await ctx.send(
            embed=discord.Embed().set_image(url=await self.getWaifu('raiden-shogun'))
        )

    @anime.command(name='oppai', description='Get waifu related to oppai')
    async def oppai(self, ctx):
        await ctx.send(
            embed=discord.Embed().set_image(url=await self.getWaifu('oppai'))
        )

async def setup(bot: commands.Bot):
    await bot.add_cog(Waifus(bot))
