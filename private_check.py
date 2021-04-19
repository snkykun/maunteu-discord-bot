import os
import random
import botkeys
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.discovery import build
import yt_api

youtube = build('youtube', 'v3', developerKey=botkeys.yt_api_key)


def clipschoose():
    while True:

        vid_id = random.choice(yt_api.clips_vid_ids)
        vid_link = 'https://www.youtube.com/watch?v=' + str(vid_id)

        clips_request = youtube.videos().list(
                part='status',
                id=vid_id
        )
        clips_response = clips_request.execute()

        # if video is unavaliable
        if clips_response['items'] != []:
            break
    return vid_link


def editchoose():
    while True:

        vid_id = random.choice(yt_api.edit_vid_ids)
        vid_link = 'https://www.youtube.com/watch?v=' + str(vid_id)

        edit_request = youtube.videos().list(
                part='status',
                id=vid_id
        )
        edit_response = edit_request.execute()

        # if video is unavaliable
        if edit_response['items'] != []:
            break
    return vid_link

# yt_api.playlistUpdate()
# print(clipschoose())
