import discord
from discord.ext import commands
import random
import asyncio

command_prefix='!'
bot = commands.Bot(command_prefix)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Connected!')
        print('Username: {0.name}\nID: {0.id}'.format(self.user))

    @bot.command(description='For when you wanna settle the score some other way')
    async def choose(ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))


client = MyClient()
f = open("token.txt","r")
token = f.read().strip()
client.run(token)
