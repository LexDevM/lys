import log_config
import logging
from discord.ext import commands

logger = logging.getLogger('lys_bot.cogs.admin')

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        logger.info('Cog Admin inicializado')

async def setup(bot):
    await bot.add_cog(Admin(bot))
    logger.info('Cog Admin añadido al bot')