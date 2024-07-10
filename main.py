import asyncio
from bot.core.bot import lys_bot
from bot.core.config import LysConfig

async def main():
    bot = lys_bot()
    await bot.start(LysConfig.token)

if __name__ == "__main__":
    asyncio.run(main())
