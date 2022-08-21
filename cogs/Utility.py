import discord, typing
from typing import Union, Optional
from discord.ext import commands
from discord import app_commands

class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name='ping',description='Shows the bot latency')
    async def ping(self, ctx):
        embed=discord.Embed(title="Bot Ping", description=f"My ping is {round(self.bot.latency * 1000)}ms", color=0xff0000)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='avatar', description='Shows the user avatar')
    async def avatar(self, ctx, user: Optional[Union[discord.Member, discord.User]]):
        if not user: user = ctx.author
        embed = discord.Embed(colour=0x303236)
        embed.set_image(url=user.display_avatar.url)
        av_button = discord.ui.Button(label='Download', url=user.display_avatar.url, emoji='⬇️')
        view = discord.ui.View()
        view.add_item(av_button)
        await ctx.send(embed=embed, view=view)

    
    @commands.hybrid_command(name='role', with_app_command=True, description='This is a role giving command')
    @app_commands.rename(ye_user='member', ye_role='role')
    @commands.bot_has_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    @app_commands.describe(ye_user='Select a user', ye_role='Select a role')
    async def role(self, ctx, ye_user: discord.Member, ye_role: Optional[discord.Role]):
        await ctx.defer(ephemeral=True)
        user = ye_user
        role = ye_role
        if ctx.author.top_role.position < user.top_role.position or ctx.author.id != ctx.guild.owner_id: return await ctx.send("You can not change their roles!!")
        await user.add_roles(role)
        await ctx.send(f"{role} added to {user.mention}!")


    @commands.hybrid_group(name='parent', description='This is the parent command')
    async def parent(self, ctx):
        pass

    @parent.command(name='subcommand', description='This is a sub command')
    async def subcommand(self, ctx):
        await ctx.send("Hii! Im subcommand.", ephemeral=True)








    @commands.hybrid_command(name='help', description='Shows a list of commands.')
    async def help(self, ctx):
        embed=discord.Embed(title="Bot Help Command", description="This is very nice bot", color=0xff0000)
        for c in self.bot.cogs:
            cog = self.bot.get_cog(c)
            if len([cog.walk_commands()]):
                embed.add_field(name=cog.qualified_name, value=', '.join(f"`{i.name}`" for i in cog.walk_commands()))
        
        await ctx.send(embed=embed)





async def setup(bot: commands.Bot):
    await bot.add_cog(Misc(bot))