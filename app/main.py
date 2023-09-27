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
    stock.add_item("Balisto", 0, 1.0)
    stock.add_item("Bounty", 0, 1.0)
    stock.add_item("BrancheC", 0, 1.0)
    stock.add_item("Coca", 0, 1.0)
    stock.add_item("CocaZero", 0, 1.0)
    stock.add_item("KitKat", 0, 1.0)
    stock.add_item("Knopper", 0, 1.0)
    stock.add_item("Kagi", 0, 1.0)
    stock.add_item("Maltesers", 0, 1.0)
    stock.add_item("Mars", 0, 1.0)
    stock.add_item("Mate", 0, 2.0)
    stock.add_item("Mentos", 0, 1.0)
    stock.add_item("Monster", 0, 2.0)
    stock.add_item("Redbull", 0, 2.0)
    stock.add_item("Smarties", 0, 1.0)
    stock.add_item("Snickers", 0, 1.0)
    stock.add_item("Thefroidcitron", 0, 1.0)
    stock.add_item("Thefroidpeche", 0, 1.0)
    stock.add_item("KinderBueno", 0, 1.0)
    stock.add_item("MisterFreeze", 0, 1.0)

    print(stock)
    return stock
        
def main():
    Stock = init_stock_DB()
    

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="/", intents=intents)
    emoji1 = '\N{THUMBS UP SIGN}'
    emojiX = '\N{THUMBS DOWN SIGN}'
#            or '\U0001f44d' or '👍'

    @bot.event
    async def on_ready():
        logger.info(f"User:{bot.user} (ID: {bot.user.id})")

    @bot.command(aliases=['a'])
    async def achat(ctx, name: str, qty: int = 1):
        """Permet d'annoncer que tu achetes quelques choses aux BDE """
        channel_log = bot.get_channel(log_channel)
        if (Stock.achat_item(name, qty) == 0):
            await channel_log.send(f"{ctx.author} - {name}: {qty} achat")
            await ctx.message.add_reaction(emoji1)
        else:
            await ctx.send(f"Some error happen")
            await ctx.message.add_reaction(emojiX)

    @bot.command(aliases=['er', 'err'])
    async def error(ctx, name: str, qty: int = 1):
        """Permet d'annoncer une erreur"""
        channel_log = bot.get_channel(log_channel)
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
        await ctx.send(f"{line}```{Stock} ```")

    @bot.command(hidden=True,
                 aliases=['add'])
    async def add_item(ctx, name: str, qty:int = 1, sellPrice: int = 1):
        """
        Permet d'ajouter un item a la basse de donnee
        """
        channel_log = bot.get_channel(log_channel)
        return_value = Stock.add_item(name, qty, sellPrice) 
        if (return_value == 0):
            await channel_log.send(f"{ctx.author} - a ajoute {name}")
            await ctx.message.add_reaction(emoji1)
        elif (return_value == -1):
            await ctx.send(f"Error: negativ arguments")
            await ctx.message.add_reaction(emojiX)
        else:
            await ctx.send(f"Error: already exist: use error or course")
            await ctx.message.add_reaction(emojiX)

    @bot.command(hidden=True, aliases=['course'])
    async def change_value_item(ctx, name: str, new_qty: int):
        channel_log = bot.get_channel(log_channel)
        return_value = Stock.refill_item(name, new_qty)
        if (return_value == 0):
            await channel_log.send(f"{ctx.author} - a modifier le stock de {name} a {new_qty}.")
            await ctx.message.add_reaction(emoji1)
        elif (return_value == 1):
            await ctx.send(f"{name} n'existe po.")
            await ctx.message.add_reaction(emojiX)
        else:
            await ctx.send(f"{new_qty} fou la merde.")
            await ctx.message.add_reaction(emojiX)


    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__== "__main__":
    main()
