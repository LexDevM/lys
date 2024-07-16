import logging
import log_config
import discord
from discord.ext import commands
from .config import LysConfig


logger = logging.getLogger('lys_bot.core')

class lys_bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(command_prefix=LysConfig.command_prefix, intents=intents)
        logger.info(f"Bot inicializado con prefijo: {LysConfig.command_prefix}")

    async def setup_hook(self):
        await self.load_cogs()

    async def on_ready(self):
        await self.wait_until_ready()
        await self.change_presence(activity=discord.Game(name="con Python | !ping"))
        logger.info(f"Bot conectado como {self.user}")

    async def on_message(self, message):
        logger.debug(f'Mensaje recibido: {message.content} de {message.author}')
        await self.process_commands(message)

    async def load_cogs(self):
        initial_extensions = ['bot.cogs.admin', 'bot.cogs.fun', 'bot.cogs.interaction_commands']
        for extension in initial_extensions:
            try:
                await self.load_extension(extension)
                logger.info(f'Cargado el módulo {extension}')
            except Exception as e:
                logger.error(f'Error al cargar el módulo {extension}: {e}')
