import discord
from discord.ext import commands
from .config import LysConfig

class lys_bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(command_prefix=LysConfig.command_prefix, intents=intents)

    async def setup_hook(self):
        await self.load_cogs()

    async def on_ready(self):
        print(f'Conectado como {self.user}')

    async def on_message(self, message):
        print(f'Recibido mensaje: {message.content} de {message.author}')
        await self.process_commands(message)

    async def load_cogs(self):
        initial_extensions = ['bot.cogs.admin', 'bot.cogs.fun']
        for extension in initial_extensions:
            try:
                await self.load_extension(extension)
                print(f'Cargado el módulo {extension}')
            except Exception as e:
                print(f'Error al cargar el módulo {extension}: {e}')
