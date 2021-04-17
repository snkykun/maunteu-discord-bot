import os
import random
import botkeys
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.discovery import build

youtube = build('youtube', 'v3', developerKey=botkeys.yt_api_key)

vid_ids = []
def playlistUpdate():
    if len(vid_ids) > 0:
        list.clear(vid_ids)
    nextPageToken = None
    while True:
        request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId='PL-qDtdxHx3uLL7QVV3hXh08tKJU5PHy-5',
                maxResults=50,
                pageToken=nextPageToken

            )
        response = request.execute()

        for items in response['items']:
            vid_ids.append(items['contentDetails']['videoId'])

        nextPageToken = response.get('nextPageToken')

        if not nextPageToken:
            break

# playlistUpdate()
# print(len(vid_ids))
