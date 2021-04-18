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
def playlistUpdate():
    if len(clips_vid_ids) > 0 and len(edit_vid_ids) > 0:
        list.clear(clips_vid_ids)
        list.clear(edit_vid_ids)
    clips_nextPageToken = None
    edit_nextPageToken = None

    while True:

        # clips playlist
        clips_request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId='PLrT1rCQzYiy6GgXecOT90ICkSeRDTTx8z',
                maxResults=50,
                pageToken=clips_nextPageToken

            )
        clips_response = clips_request.execute()

        for items in clips_response['items']:
            clips_vid_ids.append(items['contentDetails']['videoId'])

        clips_nextPageToken = clips_response.get('nextPageToken')

        if not clips_nextPageToken:
            break

    while True:

        # edit playlist
        edit_request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId='PL-qDtdxHx3uLL7QVV3hXh08tKJU5PHy-5',
                maxResults=50,
                pageToken=edit_nextPageToken

            )
        edit_response = edit_request.execute()

        for items in edit_response['items']:
            edit_vid_ids.append(items['contentDetails']['videoId'])

        edit_nextPageToken = edit_response.get('nextPageToken')

        if not edit_nextPageToken:
            break
# def editplaylistUpdate():
#     if len(edit_vid_ids) > 0:
#         list.clear(edit_vid_ids)
#     nextPageToken = None
#     while True:
#         request = youtube.playlistItems().list(
#                 part='contentDetails',
#                 playlistId='PL-qDtdxHx3uLL7QVV3hXh08tKJU5PHy-5',
#                 maxResults=50,
#                 pageToken=nextPageToken
#
#             )
#         response = request.execute()
#
#         for items in response['items']:
#             edit_vid_ids.append(items['contentDetails']['videoId'])
#
#         nextPageToken = response.get('nextPageToken')
#
#         if not nextPageToken:
#             break

# playlistUpdate()
# print(len(clips_vid_ids))
# print(len(edit_vid_ids))
