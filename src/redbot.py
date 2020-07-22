from discord import ext, Embed, Color, utils
import logging
from datetime import datetime

import utilities

import cog_roleassign
import cog_misc

COMMAND_PREFIX = '>'

COGS = [cog_roleassign.DiscordCog,
        cog_misc.DiscordCog,
        ]


def init(prefix=COMMAND_PREFIX,
        logger=None):
    """
    Setup function for Redbot.

    Returns bot object.
    """

    # Debug logging with no logger would be bad
    logger = logger or logging.NullHandler()

    # Sort out the prefix and init the actual bot object
    trigger = ext.commands.when_mentioned_or(prefix)
    bot = ext.commands.Bot(command_prefix=trigger)

    # Enable referencing the logger from anywhere
    setattr(bot, "logger", logger)

    # Set up message logging for debug
    @bot.event
    async def on_message(message):
        channel = message.channel.name
        name = message.author.display_name
        content = message.content
        logger.debug(f"#{channel} - {name}: {content}")
        await bot.process_commands(message)

    # Automatic "Playing Redout" assignment
    @bot.event
    async def on_member_update(before, member):
        is_playing = False
        for activity in member.activities:
            if activity.name is None:
                continue
            if is_playing := "redout" in activity.name.lower():
                break

        role = await utilities.get_role_by_name(member, "Playing Redout")
        has_role = role in member.roles

        if (is_playing + has_role) == 1:
            await utilities.toggle_role(member, role)

    # Deletion log
    @bot.event
    async def on_message_delete(message):
        channel = utils.get(bot.get_all_channels(), name="redbot-log")

        emb = Embed(**{"description": message.content, },
                    color=Color.red(),
                    timestamp=datetime.now())
        emb.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        await channel.send("Deleted/Missing Message", embed=emb)

    # Register cogs (bot modules)
    for cog in COGS:
        bot.add_cog(cog(bot))

    return bot
