import discord
import random
import os
import sys
import pastas
import botkey
import ytSECRET
import YoutubeAPI
import emoji
import asyncio
import datetime
from discord.ext import commands
from discord import Embed, File
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.discovery import build
client = commands.Bot(command_prefix = '.')

## Setup
os.chdir(os.path.dirname(sys.argv[0]))
@client.event
async def on_ready():
    oec_gen = client.get_channel(743941628984557711)
    sai_gen = client.get_channel(565401084718481410)
    YoutubeAPI.playlistUpdate()
    print('Bot is ready')
    custom = discord.Game('snky.cc')
    await client.change_presence(status=discord.Status.online, activity=custom)
    await oec_gen.send('Bot is ready with ' + str(len(YoutubeAPI.vid_ids)) + ' videos cached.')
    await sai_gen.send('Bot is ready, hampter.')
picList = ["floppa", "possum"]
paster = ["goat", "innit", "based", "simp", "pee", "furry", "kephrii"]

## Pastas
@client.listen()
async def on_message(message):
    if message.author.id != 801119721407119411:
        str = message.content
  # if message.author.id == 390308146293243904:
  #     await message.add_reaction('🐒')
  # if message.author.id == 274656834315616256:
  #     await message.add_reaction('<:cryingcat:796506331523055686>')
        if message.channel.id == 814613616950902834 and len(message.embeds) > 0:
            channel = client.get_channel(565401767416692747)
            embed = discord.Embed.copy(message.embeds[0])
            await channel.send(embed=embed)
        #
        # for x in paster:
        #     if x in str.lower():
        #         paste = pastas.(x)
        #         await message.channel.send(paste)


# STANDALONE TRIGGERS
        if 'cum' in str.lower():
            # await message.add_reaction('👎')
            await message.channel.send('cum')
        if 'shadowplay' in str.lower():
                await message.channel.send(file=File("./data/chadowplay.mp4"))
        if 'cock' in str.lower():
            await message.channel.send('and balls (never forget the balls.)')


        if 'goat' in str.lower():
            await message.channel.send(pastas.goat)

        if 'innit' in str.lower():
            await message.channel.send(pastas.innit)

        if 'kephrii' in str.lower():
            await message.channel.send(pastas.kephrii)

        if 'based' in str.lower()and message.channel.is_nsfw():
            await message.channel.send(pastas.based)

        if 'simp' in str.lower() and 'simple' not in str.lower():
            await message.channel.send(pastas.simp)

        if 'pee' in str.lower() and 'peepo' not in str.lower():
            await message.channel.send(pastas.pee)

        if 'furry' in str.lower():
            await message.channel.send(pastas.furry)

## commands
@client.command()
async def edit(ctx, *, source=None):
    if source == 'source':
        await ctx.send('Videos are sourced from this playlist here: https://www.youtube.com/playlist?list=PL-qDtdxHx3uLL7QVV3hXh08tKJU5PHy-5')
    else:
        vid_link = 'https://www.youtube.com/watch?v=' + str(random.choice(YoutubeAPI.vid_ids))
        await ctx.send(vid_link)

@client.command()
async def submit(ctx, code=None, link=None):
    msg = ctx.message.content
    if ctx.channel.id == 746754347764809869:
        if 'https' in link.lower() and code != None:
            await ctx.send('Thank you for your submission, a mod will approve/remove your frag shortly! Other members may vote by reacting to the submission with the corresponding emojis.')
            await ctx.message.add_reaction('✔️')
            await ctx.message.add_reaction('❌')
        else:
            await ctx.send(ctx.message.author.mention + ' Submit a frag by typing `.submit <replay code> <video link>`')


@client.command()
async def possum(ctx):
    await ctx.channel.send(file=File("./data/possum/" + random.choice(os.listdir("./data/possum"))))

@client.command()
async def floppa(ctx):
    await ctx.channel.send(file=File("./data/floppa/" + random.choice(os.listdir("./data/floppa"))))

@client.command()
async def cat(ctx):
    await ctx.channel.send(file=File("./data/cat/" + random.choice(os.listdir("./data/cat"))))

# for pics in picList:
#     @client.command()
#     async def pics(ctx):
#         await ctx.channel.send(file=File("./data/" + str(pics) + "/" + random.choice(os.listdir("./data/" + str(pics)))))

@client.command()
async def freestyle(ctx):
    await ctx.channel.send('Nvidia Freestyle in Overwatch guide https://github.com/snkykun/Overwatch-Freestyle')

@client.command()
@commands.has_role('Frag Approver')
async def approve(ctx):
    channel = client.get_channel(790682495167234080)
    await channel.send(ctx.message.reference.resolved.content[7:] + " hit by " + ctx.message.reference.resolved.author.mention)




# @client.listen()
# @commands.has_role('Frag Approver')
# async def on_message(msg):
#   if msg.author.id != 801119721407119411 and msg.channel.id == 803087684779114516:
#       await msg.channel.send('1')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

client.run(botkey.key)
