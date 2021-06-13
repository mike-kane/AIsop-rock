import lyricsgenius
import os
import sys
import json

# def get_genius_api_credentials():
#     """Output: Returns a dictonary containing the 'client_id', 'client_secret', and
#     'client_token'.
#
#     Explanation of function: Reads the api credentials from a secrets.txt file on
#      my local machine (if you see secrets.txt in this repo, please let me know I am
#      an idiot for exposing my API key")
#
#     The secrets.txt file has the information stored in the following format:
#
#     client_id:XXXXXXXXX
#     client_secret:XXXXXXXXX
#     client_token:XXXXXXXXXX
#
#     This function reads the file into a list containing each of the lines.
#
#     Then, the function creates a dictionary to store the content in and processes
#     each line by removing the newline character at the end of each line, then splits
#     each line on ':'. This gives us each line as a tuple, with the actual information
#     being stored in [1] for each.
#
#     Finally, it creates a key-value pair for each entry in the secrets dictionary,
#     and returns the dictionary"""
#     with open('secrets.txt') as f:
#         print('Loading Genius API credentials...')
#         data = f.readlines()
#         secrets = {}
#
#         secrets['client_id']  = data[0].strip('\n').split(':')[1]
#         secrets['client_secret'] = data[1].strip('\n').split(':')[1]
#         secrets['client_token'] = data[2].strip('\n').split(':')[1]
#
#         print('... Done')
#
#         return secrets

def main(artist_name):
    """
    OUTPUT: Writes a JSON file containing all the of the song information from the artist
     from the genius API.


    Explanation of function:

    Uses the get_genius_api_credentials function to get credentials needed
    for lyricsgenius object.

    Gets all artist song information using the lyricsgenius library and the
    Genius API.
     """


    with open('secrets.json') as json_data:
        secrets = json.load(json_data)
    token = secrets['client_token']

    genius = lyricsgenius.Genius(secrets['client_token'])

    artist = genius.search_artist(artist_name, sort='title', include_features=False)
    print('Saving data')
    artist.save_lyrics()
    print("Data saved successfully!")

def write_lyrics_to_files():
    with open('Lyrics_AesopRock.json') as json_data:
        data = json.load(json_data)

    # List of songs with duplicate content but different titles
    songs_to_remove = ['Странные люди (Strange people)', 'Странные люди (Strange people) (2nd version)',
                       'Zero Dark Thirty Single Art', 'The Tugboat Complex Pt. 3',
                       'Orphanage Freestyle Part 1 (Atmosphere Freestyle)', 'One of Four (Thank You)',
                      'Cycles To Gehenna (Zavala Remix)', 'Coffee', '11:35 (feat. Mr. Lif) / Ketamine U.S.A. Interlude']

    song_counter = 0
    for song in data['songs']:
        lyrics = song['lyrics']
        title = song['title']

        # Only write the songs that haven't been flagged for removal
        if title not in songs_to_remove:
            song_filename = "aesop_rock_{}.txt".format(song_counter)
            file_path = 'data/' + song_filename

            # write each song to a text file, including title at the top in a way that's easy to identify and remove later
            with open(file_path, 'w') as f:
                file_text = "[Song Title] {} \n\n {}".format(title, lyrics)
                f.write(file_text)

            song_counter += 1


# main("aesop rock")
write_lyrics_to_files()
