from discord import Embed, Color
from discord.ext import commands
from random import choice, randint
from datetime import datetime
import checks


class DiscordCog(commands.Cog, name="Misc"):
    def __init__(self, bot):
        self.bot = bot
        self.bot.logger.debug("Misc Command Cog loaded")

    @commands.command(description="Flips a coin... Or a table.", usage="[table]")
    @commands.check(checks.chan_commands)
    async def flip(self, ctx, args=None):
        if args == "table":
            await ctx.send("(╯°□°）╯︵ ┻━┻")
        elif args is not None:
            await ctx.send("Might I suggest `>help flip`?")
        else:
            await ctx.send(choice(["Heads", "Tails"]))

    @commands.command(description="Rolls dice, giving the total and individual results.", usage="AdB")
    @commands.check(checks.chan_commands)
    async def roll(self, ctx, args=""):
        dice = args.split("d")

        if args.lower() == "adb":
            await ctx.send("Don't get smart with me. Replace A and B with positive integers.")

        elif args.lower() == "d":
            await ctx.send("I don't want the d...")

        elif args.lower() == "a":
            await ctx.send("B, C, D, E, F... Wait, this isn't preschool!")

        elif len(dice) != 2:
            await ctx.send(f"'{args}' doesn't look like a dice roll to me..." + " Did you mean >help roll?"*("help" in args))

        elif not dice[0].isdigit() or not dice[1].isdigit():
            await ctx.send("The format is AdB, where A and B are natural numbers (1, 2, 3, 4).")

        else:
            dice[0], dice[1] = int(dice[0]), int(dice[1])
            if dice[0] < 1:
                await ctx.send("I need to roll at least *one* dice, bud.")

            elif dice[0] > 10:
                await ctx.send("I appreciate the enthusiasm, but you can only roll up to 10 dice at once.")

            elif dice[1] < 2:
                await ctx.send("I cannot mathematically roll anything less than a d2 and still call it rolling.")

            elif dice[1] > 1000:
                await ctx.send("Going beyond a d1000 is a bit silly, so... Don't.")

            else:
                total = 0
                results = []
                for i in range(dice[0]):
                    result = randint(1, dice[1])
                    results.append(str(result))
                    total = total + result
                resultstr = f"{args}: {', '.join(results)} = {total}."

                emb = Embed(**{"description": resultstr, },
                            color=Color.dark_purple(),
                            timestamp=datetime.now())
                emb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=emb)
