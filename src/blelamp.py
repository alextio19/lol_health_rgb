import asyncio
import os
from btledstrip import BTLedStrip, MELKController


ADDRESS = os.getenv('RGB_ADDRESS') # YOUR MAC_ADDRESS (RGB LAMP)


class Lamp:
    def __init__(self):
        self.controller = MELKController()
        self.strip = BTLedStrip(self.controller, ADDRESS)
        self.last_color = None

    async def connect(self):
        await self.strip.__aenter__()
        await self.strip.exec.turn_on()

    async def disconnect(self):
        await self.strip.__aexit__(None, None, None)

    async def set_health(self, health):
        health = max(0, min(100, health))

        color = (
            100 - health,
            health,
            0
        )

        if color == self.last_color:
            return

        self.last_color = color

        await self.strip.exec.color(
            red=color[0],
            green=color[1],
            blue=color[2],
        )