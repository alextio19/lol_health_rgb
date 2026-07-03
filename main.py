import os
import sys
sys.path.append(os.path.join(os.getcwd(),'src'))

from blelamp import Lamp
from common_utils import (
    find_value,
    check_port
)

from lol.champion import Champion
import asyncio


async def main():
    champion = Champion()
    lamp = Lamp()
    await lamp.connect()
    await lamp.strip.exec.turn_off()
    while True:
        if check_port('127.0.0.1', 2999):
            await lamp.strip.exec.turn_on()
            old_health = champion.current_health
            
            if champion.refresh_data():
                new_health = champion.current_health

                if new_health != old_health:
                    await lamp.set_health(champion.health_percentage)

                await asyncio.sleep(0.5)
            else:
                await lamp.strip.exec.turn_off()
                await asyncio.sleep(10)
    await lamp.disconnect()


if __name__ == "__main__":
    asyncio.run(main())