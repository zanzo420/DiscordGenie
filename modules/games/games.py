# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com
import random

from discord.ext import commands

from modules.moderation.moderation import abuse_internal


class Commands:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roll(self):
        r = random.randint(1, 6)
        await self.client.say("You rolled {}!".format(r))

    @commands.command(pass_context=True)
    async def roulette(self, ctx):
        r = random.randint(1, 6)
        if r == 3:
            await self.client.say("You were shot. Have fun!")
            txt = ".abuse {} 5".format(ctx.message.author.mention)
            message = await self.client.say(txt)
            await abuse_internal(self.client, message, 5)
        else:
            await self.client.say("You're safe!")


def setup(client):
    client.add_cog(Commands(client))
