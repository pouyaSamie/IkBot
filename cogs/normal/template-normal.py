import json
import os
import sys

from disnake.ext import commands
from disnake.ext.commands import Context

from helpers import checks

# Only if you want to use variables that are in the config.json file.
if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


# Here we name the cog and create a new class for the cog.
class Template(commands.Cog, name="template-normal"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="testcommand",
        description="This is a testing command that does nothing.",
    )
    @checks.not_blacklisted()
    @checks.is_owner()
    async def testcommand(self, context: Context) -> None:
        """
        This is a testing command that does nothing.
        :param context: The context in which the command has been executed.
        """
        # Do your stuff here

        # Don't forget to remove "pass", that's just because there's no content in the method.
        pass


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
def setup(bot):
    bot.add_cog(Template(bot))
