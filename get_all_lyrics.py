import lyricsgenius
import os
import sys

def get_genius_api_credentials():
"""
Output: Returns a dictonary containing the 'client_id', 'client_secret', and
'client_token'.


Explanation of function: Reads the api credentials from a secrets.txt file on
 my local machine (if you see secrets.txt in this repo, please let me know I am
 an idiot for exposing my API key")

The secrets.txt file has the information stored in the following format:

client_id:XXXXXXXXX
client_secret:XXXXXXXXX
client_token:XXXXXXXXXX

This function reads the file into a list containing each of the lines.

Then, the function creates a dictionary to store the content in and processes
each line by removing the newline character at the end of each line, then splits
each line on ':'. This gives us each line as a tuple, with the actual information
being stored in [1] for each.

Finally, it creates a key-value pair for each entry in the secrets dictionary,
and returns the dictionary
"""
    files = os.listdir()

    try:
        with open('secrets.txt') as f:
            print('Loading Genius API credentials...')
            data = f.readlines()
            secrets = {}

            secrets['client_id']  = data[0].strip('\n').split(':')[1]
            secrets['client_secret'] = data[1].strip('\n').split(':')[1]
            secrets['client_token'] = data[2].strip('\n').split(':')[1]

            print('... Done')

            return secrets

    except FileNotFoundError:
        print("File 'secrets.txt' not detected!")

def main(artist_name):

    secrets = get_genius_api_credentials()

    token = secrets['client_token']

    genius = lyricsgenius.Genius(secrets['client_token'])

    artist = genius.search_artist(artist_name, sort='title', include_features=False)
    print('Saving data')
    artist.save_lyrics()
    print("Data saved successfully!")




    artist.save_lyrics()


if __name__ == '__main':
    args = sys.argv[1:]
    print(main())
    artist_name = args[-1]
    main(artist_name)
