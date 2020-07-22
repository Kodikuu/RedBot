from discord.ext import commands
import utilities
import checks


class DiscordCog(commands.Cog, name="Role Assignment"):
    def __init__(self, bot):
        self.bot = bot
        self.bot.logger.debug("Role Assignment Cog loaded")

    async def _work(self, ctx, rolename):
        role = await utilities.get_role_by_name(ctx, rolename)
        user = ctx.author
        if await utilities.toggle_role(user, role):
            await ctx.send(f"{user.display_name} has been added to the {role} role.")
        else:
            await ctx.send(f"{user.display_name} has been removed from the {role} role.")

    @commands.command(aliases=["timeattacker"])
    @commands.check(checks.chan_assignment)
    async def tt(self, ctx):
        await self._work(ctx, "Time Attack")

    @commands.command(aliases=["screenshotter"])
    @commands.check(checks.chan_assignment)
    async def ss(self, ctx):
        await self._work(ctx, "Screenshotter")

    @commands.command(aliases=["matchmaking"])
    @commands.check(checks.chan_assignment)
    async def mm(self, ctx):
        await self._work(ctx, "Matchmaking")

    @commands.command()
    @commands.check(checks.chan_assignment)
    async def pc(self, ctx):
        await self._work(ctx, "PC")

    @commands.command()
    @commands.check(checks.chan_assignment)
    async def ps4(self, ctx):
        await self._work(ctx, "PS4")

    @commands.command()
    @commands.check(checks.chan_assignment)
    async def xbox(self, ctx):
        await self._work(ctx, "XBOX")

    @commands.command()
    @commands.check(checks.chan_assignment)
    async def switch(self, ctx):
        await self._work(ctx, "Switch")
