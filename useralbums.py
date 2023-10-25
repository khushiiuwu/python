def make_album(artist,title):
    album = {
            'artist_name': artist.title(),
            'album_title': title.title()
    }
    return album

artist_prompt = 'What is the name of the artist?'
title_prompt  = 'What is the title of the album?'

while True:
    artist = input(artist_prompt)
    if artist == 'quit':
        break
    title = input(title_prompt)
    if title == 'quit':
        break
    
    album = make_album(artist,title)
    print(album)
print('Thank you')   
    
    