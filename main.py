import log_config
import asyncio
import logging
from bot.core.bot import lys_bot
from bot.core.config import LysConfig

logger = logging.getLogger('lys_bot')

async def main():
    logger.info("Iniciando el bot")
    bot = lys_bot()
    
    logger.debug(f"Token configurado: {'Sí' if LysConfig.token else 'No'}")
    if LysConfig.token is None:
        logger.error("El token del bot no está configurado")
        raise ValueError("El token del bot no está configurado. Verifica tu configuración.")
   
    try:
        logger.info("Intentando iniciar el bot")
        await bot.start(LysConfig.token)
    except Exception as e:
        logger.error(f"Error al iniciar el bot: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot detenido manualmente")
    except Exception as e:
        logger.critical(f"Error crítico: {str(e)}")
        raise