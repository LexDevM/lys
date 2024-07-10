import os
from dotenv import load_dotenv


class LysConfig:
    token = os.getenv('DC_TOKEN') 
    command_prefix = "!"