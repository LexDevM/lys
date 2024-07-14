import log_config
import logging
from discord.ext import commands

logger = logging.getLogger('lys_bot.cogs.fun')

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        logger.info('Cog Fun inicializado')

    @commands.command()
    async def ping(self, ctx):
        logger.debug(f'Comando ping ejecutado por {ctx.author}')
        await ctx.send('Pong!')

async def setup(bot):
    await bot.add_cog(Fun(bot))
    logger.info('Cog Fun añadido al bot')
