import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.hybrid_command()
    async def hehe1(self, ctx):
        pass

    @commands.hybrid_command()
    async def hehe2(self, ctx):
        pass

    @commands.hybrid_command()
    async def hehe3(self, ctx):
        pass

    @commands.hybrid_command()
    async def hehe4(self, ctx):
        pass

async def setup(bot:commands.Bot):
    await bot.add_cog(Moderation(bot))