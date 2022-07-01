#! /usr/bin/python3

import discord
import subprocess
from subprocess import check_output
import time
client = discord.Client()

def scramble(sentence):
    out = check_output(["python","bristol/main.py",sentence])
    print(out)
    return out

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.guild.me in message.mentions:
        sentence = message.content.replace("<@418271589356797952>","")
        sentence = str(scramble(sentence),'utf-8')
        await message.channel.send(sentence)

f = open("token.txt","r")
token = f.read().strip()
client.run(token)