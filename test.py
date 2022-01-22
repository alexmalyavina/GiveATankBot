from lyrics_extractor import SongLyrics
api='AIzaSyC3cz3_NHX_zXzZ2q6ErLfM1RVgLIpyySs'
GCS_ENGINE_ID='0e47b640b6a4cdcae'
extract_lyrics = SongLyrics(api, GCS_ENGINE_ID)
with open('list_of_songs.txt') as f:
    lines=f.readlines()
items=[line.rstrip() for line in lines]
check='Дайте'
run=0
for item in items:
    data = extract_lyrics.get_lyrics(item)
    print('success')
    for data_item in data:
        print(data_item)
        if check in data_item['title']:
                print(data_item['lyrics'])
