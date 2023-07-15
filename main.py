import settings
import discord
from discord.ext import commands
from inventory import *

logger = settings.logging.getLogger("bot")

def init_inventaire():
    inventaire = Inventory()

    #Inventaire des boissons qu'on vends
    inventaire.add_item("Coca", 0)
    inventaire.add_item("Ice Tea citron", 0)
    inventaire.add_item("Ice Tea peche", 0)
    inventaire.add_item("Mate", 0)
    inventaire.add_item("Redbull", 0)
    inventaire.add_item("Monster", 0)

    #Inventaire des boissons qu'on vends
    inventaire.add_item("Sneakers", 0)
    inventaire.add_item("Bounty", 0)
    inventaire.add_item("Kinder Bueno", 0)
    inventaire.add_item("Branche", 0)
    return (inventaire)
        
def main():
    Inventaire = init_inventaire()

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="/", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User:{bot.user} (ID: {bot.user.id})")

    @bot.command(aliases=['a'])
    async def achat(ctx, name: str, qty: int):
        """Permet d'annoncer que tu achetes quelques choses aux BDE """
        inventaire.achat_item(name, qty)
        print(inventaire)
        await ctx.send(what)

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__== "__main__":
    main()
