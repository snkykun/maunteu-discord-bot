# maunteu-discord-bot [![Discord](https://img.shields.io/discord/743941628020129853.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/EXuG82n)

A small discord bot that uses the [YoutubeAPI](https://developers.google.com/youtube/v3/quickstart/python) to return video game edits at random

![Image](/images/demo.gif)
#### [_click to add the bot to your discord_](https://discord.com/api/oauth2/authorize?client_id=833057810849202218&permissions=2147867712&scope=bot)

### Commands (prefix is $)
`$edit`   Sends a random edit from the Edit museum

`$clips` Sends a random video with "clips in desc"

`$refresh` refreshes video id lists in the event the playlist is updated

`$servers` lists how many servers maunteu is in

### Playlist Sources:
- [Edit museum](https://www.youtube.com/playlist?list=PL-qDtdxHx3uLL7QVV3hXh08tKJU5PHy-5)
- [Clips in desc](https://www.youtube.com/playlist?list=PLrT1rCQzYiy6GgXecOT90ICkSeRDTTx8z)



### Self-hosting

clone the repository with `git clone`

place your API keys into `botkeys_EXAMPLE.py` and rename to `botkeys.py`
> Information on how to get your Youtube API key [here](https://www.youtube.com/watch?v=th5_9woFJmk)


`cd maunteu-discord-bot`

`pip install -r requirements.txt`

`python3 bot.py`
