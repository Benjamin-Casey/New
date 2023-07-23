# bot.py
import os

import discord
import asyncio

from role_selection import player_roles


TOKEN = "MTEzMTExNjE3ODEzNjM3MTIxMA.GJzmH1.VcIX_TngLPcbgew5S3yKyY49kYOJqUr8Xz7gEA"


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)


# Roles command
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!AdvRoles'):

        players = []

        for player in message.mentions:
            players.append(player)

        roles = player_roles(players)

        for player in roles.keys():
            await player.create_dm()
            await player.dm_channel.send(f'{roles[player][0]}: {roles[player][1]}\n{roles[player][2]}')


client.run(TOKEN)
