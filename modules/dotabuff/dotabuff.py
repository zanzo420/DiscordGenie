# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com

import re

from bs4 import BeautifulSoup
from discord.ext import commands

from modules.aws_lambda import aws


class Commands:
    def __init__(self, client):
        self.client = client

    def parse_heroes(self, page):
        soup = BeautifulSoup(page)
        rows = soup.find_all('tr')
        table = {}
        for row in rows:
            # cells = row.findChildren('td', class_="cell-icon")
            # for cell in cells:
            #     print(cell.string)
            hero = ''
            for cell in row.findChildren('td'):
                r = re.search('<td class=\"cell-icon\".{0,50}value=\"(\w+)\"', str(cell))
                if r:
                    hero = r.group(1)
                    table[hero] = 0
                    continue
                r = re.search('value=\"([\d\.]+).{50,75}win', str(cell))
                if r:
                    table[hero] = r.group(1)
        print(table)

    @commands.command(pass_context=True)
    async def winrate(self, ctx, request):
        positions = ["mid", "off", "safe", "jungle", "roaming"]

        if not request or request not in positions:
            usage = "```Usage:\n.dotabuff [mid|off|safe|jungle|roaming]"
            await self.client.say(usage)
        await self.client.say("Processing winrate request for position {}".format(request))

        self.parse_heroes(aws.process("dotabuff", request))


def setup(client):
    client.add_cog(Commands(client))
