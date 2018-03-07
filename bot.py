# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')
extensions = ["modules.moderation.moderation", "modules.games.games"]


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('-------------')
    await client.change_presence(game=discord.Game(name="Ready for commands!"), afk=False)

if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    client.run('NDIwMzcyNTU5MzkwMDQ4MjU2.DYClJg.8wUzQZSijt8kjOZ_IA_RIwocEg4')
