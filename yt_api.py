import os
import random
import botkeys
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.discovery import build

youtube = build('youtube', 'v3', developerKey=botkeys.yt_api_key)

clips_vid_ids = []
edit_vid_ids = []
def clipsplaylistUpdate():
    if len(clips_vid_ids) > 0:
        list.clear(clips_vid_ids)
    nextPageToken = None
    while True:
        request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId='PLrT1rCQzYiy6GgXecOT90ICkSeRDTTx8z',
                maxResults=50,
                pageToken=nextPageToken

            )
        response = request.execute()

        for items in response['items']:
            clips_vid_ids.append(items['contentDetails']['videoId'])

        nextPageToken = response.get('nextPageToken')

        if not nextPageToken:
            break
def editplaylistUpdate():
    if len(edit_vid_ids) > 0:
        list.clear(edit_vid_ids)
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
            edit_vid_ids.append(items['contentDetails']['videoId'])

        nextPageToken = response.get('nextPageToken')

        if not nextPageToken:
            break

# playlistUpdate()
# print(len(vid_ids))
