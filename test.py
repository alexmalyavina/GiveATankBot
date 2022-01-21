from lyrics_extractor import SongLyrics
api='AIzaSyC3cz3_NHX_zXzZ2q6ErLfM1RVgLIpyySs'
GCS_ENGINE_ID='0e47b640b6a4cdcae'
extract_lyrics = SongLyrics(api, GCS_ENGINE_ID)
data = extract_lyrics.get_lyrics("Shape of You")
print(data)
