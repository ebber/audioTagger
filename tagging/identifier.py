import spotipy
import pprint

#add auth
class spotifyMetaRetriever:
  def __init__(self):
    self.sp = spotipy.Spotify()

  def removeExtraneous(self, q):
    lower = q.lower();
    removedWords = ["official video", "official video", "music video"]
    for phrase in removedWords:
      lower.replace(phrase,"");

    return lower

  def smartSpotifyQuery(self, q):
    sQ = self.removeExtraneous(q)
    return self.spotifyQuery(sQ)


  def spotifyQuery(self, q):
    print "Querrying spotify with: ",q
    result = self.sp.search(q, type='track', limit=1)
    tracks= result["tracks"]["items"]
    if len(tracks)>0:
      return tracks[0]
    else:
      print "nothing returned from spotify",result
      return -1

    return result[0]

  def extractBasicMetadata(self, spotifyResult):
    basicData = {}
    basicData["TITLE"] = [spotifyResult['name']]
    artists = [artist["name"] for artist in spotifyResult["artists"]]
    basicData["ARTIST"] = artists
    basicData["ALBUM"] = spotifyResult["album"]["name"]
    return basicData


