import discord, os, typing
from typing import *
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('TOKEN')

class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    async def on_ready(self):
        print(f"Logged in as {self.user}")


    async def setup_hook(self):
        for fn in os.listdir('cogs'):
            if fn.endswith('.py'):
                await self.load_extension(f"cogs.{fn[:-3]}")
    



intents = discord.Intents.default()
intents.message_content = True

bot = MyBot(command_prefix='!', intents=intents)

@bot.command()
@commands.guild_only()
async def sync(
  ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")


# Works like:
# !sync -> global sync
# !sync ~ -> sync current guild
# !sync * -> copies all global app commands to current guild and syncs
# !sync ^ -> clears all commands from the current guild target and syncs (removes guild commands)
# !sync id_1 id_2 -> syncs guilds with id 1 and 2

bot.run(TOKEN)