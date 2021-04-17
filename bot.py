import botkeys
import yt_api
import random
import os
import discord
import sys
import emoji
import asyncio
import datetime
from discord.ext import commands
from discord import Embed, File

client = commands.Bot(command_prefix = '$')

## Setup
os.chdir(os.path.dirname(sys.argv[0]))
@client.event
async def on_ready():
    yt_api.playlistUpdate()
    print('Bot is ready with ' + str(len(yt_api.vid_ids)) + ' videos cached.')
    custom = discord.Game('Editing Archive')
    await client.change_presence(status=discord.Status.online, activity=custom)
## commands
@client.command()
async def edit(ctx, *, source=None):
    if source == 'source':
        await ctx.send('Videos are sourced from this playlist here: https://www.youtube.com/playlist?list=PL-qDtdxHx3uLL7QVV3hXh08tKJU5PHy-5')
    else:
        vid_link = 'https://www.youtube.com/watch?v=' + str(random.choice(yt_api.vid_ids))
        await ctx.send(vid_link)

client.run(botkeys.discord_key)
