from discord import ext
import logging

COMMAND_PREFIX = '>'


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

    return bot
