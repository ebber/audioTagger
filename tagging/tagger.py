from model.song import Song
from tagging.identifier import spotifyMetaRetriever

class Tagger():

    spotifyRetriever = spotifyMetaRetriever()

    def __init__(self):
        pass

    def tag_song(self, song):
       return self.tag_spotify(song)

    def tag_spotify(self, song):
        try:
            query = song.filename.replace(".mp3", "");
            result = self.spotifyRetriever.smartSpotifyQuery(query)
            metaData = self.spotifyRetriever.extractBasicMetadata(result)
            song.fillMetadta(metaData)
            return 0
        except:
            print "Failed to tag: ", song.filename
            return -1
