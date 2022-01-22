# GENIUS_API_TOKEN = 'D3mUUdRX6pUml4AjLZT6WBOw2JmH95cioffqaz4TZLiNIu8SJVr5DSrwiHXkFzjc'
import re
import requests
import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup
import search as sh# other Python file with functions

######################################################################
########### Main file to run everything #############################
#####################################################################

# Constants
base = "https://api.genius.com"
client_access_token ='D3mUUdRX6pUml4AjLZT6WBOw2JmH95cioffqaz4TZLiNIu8SJVr5DSrwiHXkFzjc'

def connect_lyrics(song_id):
    '''Constructs the path of song lyrics.'''
    url = "songs/{}".format(song_id)
    data = sh.get_json(url)
    # print(data)

    # Gets the path of song lyrics
    path = data['response']['song']['path']
    print(path)
    return path


def retrieve_lyrics(song_id):
    '''Retrieves lyrics from html page.'''
    path = connect_lyrics(song_id)

    URL = "http://genius.com" + path
    # print(URL)
    page = requests.get(URL)
    # html_doc=page.text
    # r'window\.__INITIAL_STATE__ = ({.*});', html_data).group(1)
    # data = re.search(r"window.__PRELOADED_STATE__ = JSON.parse({.*?});", html_doc).group(1)
    # print(data)
    # data = json.loads(data)
    # # pretty print the data:
    # print(json.dumps(data, indent=4))
    # Extract the page's HTML as a string
    html = BeautifulSoup(page.content, "html.parser")
    # print(html)
    # Scrape the song lyrics from the HTML
    # print(song_id)
    lyrics = html.select_one('div[class^="Lyrics__Container"], .lyrics').get_text(strip=True, separator='\n')
    print(lyrics)
    # # print(html.find("div", attrs={'class':'lyrics'}))
    # # if html.find("div", class_="lyrics") is not None:
    # #     lyrics = html.find("div", class_="lyrics").getText()
    # #     print(lyrics)
    return lyrics


def get_song_id(artist_id):
    '''Get all the song id from an artist.'''
    current_page = 1
    next_page = True
    songs = [] # to store final song ids

    while next_page:
        path = "artists/{}/songs/".format(artist_id)
        params = {'page': current_page} # the current page
        data = sh.get_json(path=path, params=params) # get json of songs

        page_songs = data['response']['songs']
        # print(page_songs)
        if page_songs:
            # Add all the songs of current page
            songs += page_songs
            # Increment current_page value for next loop
            current_page += 1
            print("Page {} finished scraping".format(current_page))
            # If you don't wanna wait too long to scrape, un-comment this
            # if current_page == 2:
            #     next_page = False
        else:
            # If page_songs is empty, quit
            next_page = False

    print("Song id were scraped from {} pages".format(current_page))

    # Get all the song ids, excluding not-primary-artist songs.
    # songs_ = [song["title"] for song in songs
    #         if song["primary_artist"]["id"] == artist_id]
    songs_id = [song["id"] for song in songs
            if song["primary_artist"]["id"] == artist_id]
    print(len(songs_id))
    return songs_id

def main():
    # Example searches
    term = 'Daite Tank (!)'

    # artist_id = 1417031
    artist_id = 1417031
    # sh.search_artist(artist_id)

    # Grabs all song id's from artist
    songs_ids = get_song_id(1417031)

    # Get meta information about songs
    #song_list = get_song_information(songs_ids)
    count=1
    # Scrape lyrics from the songs
    for song_id in songs_ids:
        print('###'*10)
        # print(count)
        retrieve_lyrics(song_id)

    # Gets information regarding the artist themself
    # followers = search_artist(artist_id)

    # Shows some random songs from arist and lyrics
    #search(term)


if __name__ == "__main__":
    main()
