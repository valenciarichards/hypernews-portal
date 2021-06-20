# tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
#                       "On the Other Side": "Samara"},
#           "Cure": {"Disintegration": "Lovesong",
#                    "Wish": "Friday I'm in love"}}


def tracklist(**musicians):
    for musician, info in musicians.items():
        print(musician)
        for album, track in info.items():
            print(f"ALBUM: {album} TRACK: {track}")

# tracklist(**tracks)
