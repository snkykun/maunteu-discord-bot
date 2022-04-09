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

def kyyViewCount():

    kyy_viewCounts = 0
    kyy_nextPageToken = None

    while True:

        # kyy_viewCounts
        kyy_request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId='PL5XH1T5EYkawLWSWS4H0WzBE6pn6M1QTY',
                maxResults=50,
                pageToken=kyy_nextPageToken

            )
        kyy_response = kyy_request.execute()
        kyy_nextPageToken = kyy_response.get('nextPageToken')
        for items in kyy_response['items']:
            try:
                kyy_request = youtube.videos().list(
                    part='statistics',
                    id=items['contentDetails']['videoId']
                )
                kyy_response = kyy_request.execute()
                kyy_viewCounts = kyy_viewCounts + int(kyy_response['items'][0]['statistics']['viewCount'])
            except:
                print('failed to process https://www.youtube.com/watch?v=' + str(items['contentDetails']['videoId']) + ' its probably private')

        if not kyy_nextPageToken:
            break
    return format(kyy_viewCounts, ",d")

print(kyyViewCount())

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
# print(len(edit_vid_ids))
