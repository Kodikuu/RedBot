import argparse

import redbot
import utilities

if __name__ == "__main__":
    # Parse commandline arguments
    cmd_parser = argparse.ArgumentParser("Runs Redbot")
    cmd_parser.add_argument('--debug', action='store_true', help="Enable debug logging")
    cmd_parser.add_argument('--token', default=None, help="Discord bot token to run with")

    args = cmd_parser.parse_args()

    # Initialise logging
    logger = utilities.init_logging(args.debug)

    # Initialise bot
    logger.debug("Initalising RedBot")
    _bot = redbot.init(logger=logger)

    # Assign token
    logger.debug("Assigning token")
    token = args.token or utilities.env("DISCORD_REDBOT_TOKEN")
    if not token:
        raise ValueError("Token not provided.")

    del args

    # Start bot instance
    logger.debug("Starting instance")
    _bot.run(token)
    logger.debug("Exiting")

    # Cleanup
    del logger
    del token
    del _bot
