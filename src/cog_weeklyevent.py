from discord.ext.commands import Cog
from discord import utils
import asyncio
import utilities

CHANNEL = "events"

EVENT = {"day": 5, "hour": 19}


class DiscordCog(Cog, name="Bartender"):
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.announcer())

    async def announcer(self, ):
        """
        A hardcoded announcer.
        """
        await self.bot.wait_until_ready()

        self.channel = utils.get(self.bot.get_all_channels(), name=CHANNEL)

        while True:
            timeto = utilities.time_to_weekly_event(**EVENT)

            if timeto > 3600:  # If more than an hour remains
                await asyncio.sleep(timeto - 3600)  # Wait until an hour prior
                await self.channel.send("@here **The Weekly Wall-Grind** will begin in 1 hour!")
                timeto = utilities.time_to_weekly_event(**EVENT)

            await asyncio.sleep(timeto)  # Wait until event
            await self.channel.send("@here The Weekly Wall-Grind has begun!")

            await asyncio.sleep(timeto)  # Close up the spacebar at 10pm EST, 2am UTC
            await self.channel.send("Happy hour is over")
