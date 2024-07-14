import log_config
import os
import logging
from dotenv import load_dotenv

logger = logging.getLogger('lys_bot.config')

class LysConfig:
    load_dotenv()
    token = os.getenv('DC_TOKEN') 
    command_prefix = "!"

    @classmethod
    def validate_config(cls):
        if not cls.token:
            logger.error("Token no congfigurado en las variables de entorno")
            raise ValueError("El token del bot no está configurado. Verifica tu configuración.")
        else:
            logger.info("Token configurado correctamente")
        logger.info(f"Prefijo de comandos configurado: {cls.command_prefix}")


LysConfig.validate_config()