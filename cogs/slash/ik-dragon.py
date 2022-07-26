import json
import os
import sys

from disnake import ApplicationCommandInteraction, Option, OptionType
import disnake
from disnake.ext import commands
from Data.repository import GetAllDragons

from helpers import checks

# Only if you want to use variables that are in the config.json file.
if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


# Here we name the cog and create a new class for the cog.
class IkDragon(commands.Cog, name="ik-dragon-slash"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="dragoncost",
        description="Show the Dragon gold cost for each level.",
        options=[
            Option(
                name="level",
                description="Dragon Level",
                type=OptionType.integer,
                required=True
            )
        ],
    )
    # This will only allow non-blacklisted members to execute the command
    @checks.not_blacklisted()
    # This will only allow owners of the bot to execute the command -> config.json
    @checks.is_owner()
    async def ShowDragonCost(self, interaction: ApplicationCommandInteraction,level: int ):
        """
        this method will retur the dragon gold cost.
        Note: This is a SLASH command
        :param interaction: The application command interaction.
        """
        if level < 0 or level >50 :
              embed = disnake.Embed(
                    title="invalid Dragon Level",
                    description="Drgaon Level should be between 1 and 50.",
                    color=0xE02B2B
                )
              await interaction.send(embed=embed)
        else:
            drag = GetAllDragons(level)
            strGoldCost= ""
            if(drag.gold_cost<1000000):
                strGoldCost = str(drag.gold_cost)
            else:
                strGoldCost = str(drag.gold_cost/1000000) + "M"

            embed = disnake.Embed(
                title=f"Dragon {level}",
                description=f"You need {strGoldCost} gold",
                color=0x9C84EF
            )
            
            await interaction.send(embed=embed)
        


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
def setup(bot):
    bot.add_cog(IkDragon(bot))
