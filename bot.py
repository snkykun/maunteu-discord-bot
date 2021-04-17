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
# os.chdir(os.path.dirname(sys.argv[0]))
@client.event
async def on_ready():
    yt_api.editplaylistUpdate()
    yt_api.clipsplaylistUpdate()
    print('Bot is ready with ' + str(len(yt_api.edit_vid_ids)) + ' edit museum videos and ' + str(len(yt_api.clips_vid_ids)) + ' clips in desc videos discovered.')
    custom = discord.Game('Editing Archive')
    await client.change_presence(status=discord.Status.online, activity=custom)
## commands
@client.command()
async def edit(ctx, *, source=None):
    if source == 'source':
        await ctx.send('Videos are sourced from this playlist here: https://www.youtube.com/playlist?list=PL-qDtdxHx3uLL7QVV3hXh08tKJU5PHy-5')
    else:
        vid_link = 'https://www.youtube.com/watch?v=' + str(random.choice(yt_api.edit_vid_ids))
        await ctx.send(vid_link)
@client.command()
async def clips(ctx, *, source=None):
    if source == 'source':
        await ctx.send('Videos are sourced from this playlist here: https://www.youtube.com/playlist?list=PLrT1rCQzYiy6GgXecOT90ICkSeRDTTx8z')
    else:
        vid_link = 'https://www.youtube.com/watch?v=' + str(random.choice(yt_api.clips_vid_ids))
        await ctx.send(vid_link)
@client.command()
async def servers(ctx):
  servers = list(client.guilds)
  await ctx.send(f"Connected on {str(len(servers))} servers:")
  await ctx.send('\n'.join(guild.name for guild in servers))


client.run(botkeys.discord_key)
