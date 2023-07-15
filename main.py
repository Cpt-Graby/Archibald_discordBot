import settings
import discord
from discord.ext import commands
from inventory import *

logger = settings.logging.getLogger("bot")
log_channel = settings.DISCORD_LOG_CHANNEL 

def init_inventaire_BDE():
    inventaire = Inventory()
    inventaire.add_item("Balisto", 0)
    inventaire.add_item("Bounty", 0)
    inventaire.add_item("Branche C", 0)
    inventaire.add_item("Coca", 0)
    inventaire.add_item("Coca Zero", 0)
    inventaire.add_item("Kit Kat", 0)
    inventaire.add_item("Knopper", 0)
    inventaire.add_item("Kagi", 0)
    inventaire.add_item("Maltesers", 0)
    inventaire.add_item("Mars", 0)
    inventaire.add_item("Mate", 0)
    inventaire.add_item("Mentos", 0)
    inventaire.add_item("Monster", 0)
    inventaire.add_item("Red Bull", 0)
    inventaire.add_item("Smarties", 0)
    inventaire.add_item("Snickers", 0)
    inventaire.add_item("The froid citron", 0)
    inventaire.add_item("The froid pêche", 0)
    inventaire.add_item("Kinder Bueno", 0)
    inventaire.add_item("Mister Freeze", 0)
    return inventaire
        
def main():
    Inventaire = init_inventaire_BDE()

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="/", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User:{bot.user} (ID: {bot.user.id})")

    @bot.command(aliases=['a'])
    async def achat(ctx, name: str, qty: int = 1):
        """Permet d'annoncer que tu achetes quelques choses aux BDE """
        channel_log = bot.get_channel(log_channel)
        if (Inventaire.item_exists(name) == True):
            Inventaire.achat_item(name, qty)
            await channel_log.send(f"{ctx.author} - {name}: {qty} achat")
        else:
            await ctx.send(f"Doesn't exist")

    @bot.command(aliases=['er'])
    async def error(ctx, name: str, qty: int = 1):
        """Permet d'annoncer une erreur"""
        channel_log = bot.get_channel(log_channel)
        if (Inventaire.item_exists(name) == True):
            Inventaire.correct_error(name, qty)
            await channel_log.send(f"{ctx.author} - {name}: {qty} rendu")
        else:
            await ctx.send(f"Doesn't exist")

    @bot.command()
    async def list(ctx):
        """Voici une maniere simple d'avoir les noms des elements dans
        l'inventaire. """
        line = "Voici la liste incluses dans l'inventaire:\n"
        await ctx.send(f"{line}```{Inventaire.get_inventory_keys()} ```")

    @bot.command(hidden=True,
                 aliases=['add'])
    async def add_item(ctx, name: str, qty:int = 1):
        channel_log = bot.get_channel(log_channel)
        if (Inventaire.item_exists(name) == False):
            Inventaire.add_item(name, qty)
            await channel_log.send(f"{ctx.author} - a ajoute {name}")
        else:
            Inventaire.add_item(name, qty)
            await channel_log.send(f"{ctx.author} - a mis a jour {name}")

    @bot.command(hidden=True)
    async def reset(ctx):
        channel_log = bot.get_channel(log_channel)
        await channel_log.send(f"{ctx.author} is ressetting the invertoy:\n{Inventaire}")
        Inventaire.reset_inventory()

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__== "__main__":
    main()
