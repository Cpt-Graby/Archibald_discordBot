import settings
import discord
from discord.ext import commands
from inventory import *
from  stockDB import *

logger = settings.logging.getLogger("bot")
log_channel = settings.DISCORD_LOG_CHANNEL 
bilan_channel = settings.DISCORD_BILAN_CHANNEL 

def init_stock_DB():
    stock = Product()
    stock.add_item("Balisto", 100, 0, 1.0)
    stock.add_item("Bounty", 100, 0, 1.0)
    stock.add_item("BrancheC", 100, 0, 1.0)
    stock.add_item("Coca", 100, 0, 1.0)
    stock.add_item("CocaZero", 100, 0, 1.0)
    stock.add_item("KitKat", 100, 0, 1.0)
    stock.add_item("Knopper", 100, 0, 1.0)
    stock.add_item("Kagi", 100, 0, 1.0)
    stock.add_item("Maltesers", 100, 0, 1.0)
    stock.add_item("Mars", 100, 0, 1.0)
    stock.add_item("Mate", 100, 0, 2.0)
    stock.add_item("Mentos", 100, 0, 1.0)
    stock.add_item("Monster", 100, 0, 2.0)
    stock.add_item("Redbull", 100, 0, 2.0)
    stock.add_item("Smarties", 100, 0, 1.0)
    stock.add_item("Snickers", 100, 0, 1.0)
    stock.add_item("Thefroidcitron", 100, 0, 1.0)
    stock.add_item("Thefroidpeche", 100, 0, 1.0)
    stock.add_item("KinderBueno", 100, 0, 1.0)
    stock.add_item("MisterFreeze", 100, 0, 1.0)

    print(stock)
    return stock
        
def main():
    Stock = init_stock_DB()
    

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="/", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User:{bot.user} (ID: {bot.user.id})")

    @bot.command(aliases=['a'])
    async def achat(ctx, name: str, qty: int = 1):
        """Permet d'annoncer que tu achetes quelques choses aux BDE """
        emoji1 = '\N{THUMBS UP SIGN}'
        emojiX = '\N{THUMBS DOWN SIGN}'
#            or '\U0001f44d' or '👍'
        channel_log = bot.get_channel(log_channel)
        if (Stock.achat_item(name, qty) == 0):
            await channel_log.send(f"{ctx.author} - {name}: {qty} achat")
            await ctx.message.add_reaction(emoji1)
        else:
            await ctx.send(f"Some error happen")
            await ctx.message.add_reaction(emojiX)

    @bot.command(aliases=['er'])
    async def error(ctx, name: str, qty: int = 1):
        """Permet d'annoncer une erreur"""
        channel_log = bot.get_channel(log_channel)
        emoji1 = '\N{THUMBS UP SIGN}'
        emojiX = '\N{THUMBS DOWN SIGN}'
#            or '\U0001f44d' or '👍'
        if (Stock.correct_error(name, qty) == 0):
            await channel_log.send(f"{ctx.author} - {name}: {qty} rendu")
            await ctx.message.add_reaction(emoji1)
        else:
            await ctx.send(f"Doesn't exist")
            await ctx.message.add_reaction(emojiX)

    @bot.command()
    async def list(ctx):
        """Voici une maniere simple d'avoir les noms des elements dans
        l'inventaire. """
        line = "Voici la liste des elements inclusent dans l'inventaire:\n"
        await ctx.send(f"{line}```{Stock.read_table()} ```")

    @bot.command(hidden=True,
                 aliases=['add'])
    async def add_item(ctx, name: str, qty:int = 1):
        emoji1 = '\N{THUMBS UP SIGN}'
        emojiX = '\N{THUMBS DOWN SIGN}'
        channel_log = bot.get_channel(log_channel)
        if (Stock.add_item(name, stock, soldQty, sellPrice) == 0):
            await channel_log.send(f"{ctx.author} - a ajoute {name}")
            await ctx.message.add_reaction(emoji1)

    @bot.command(hidden=True)
    async def reset(ctx):
        channel_bilan = bot.get_channel(bilan_channel)
        emoji1 = '\N{THUMBS UP SIGN}'
        await channel_bilan.send(f"{ctx.author} is ressetting the invertoy:\n```{Inventaire}```")
        await ctx.message.add_reaction(emoji1)

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__== "__main__":
    main()
