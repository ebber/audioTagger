
from metadataChanger import Song
from identifier import metaRetriever

import os

id = metaRetriever();

def tagDir():
  print("tagging")
  songFailed=[];
  for file in os.listdir("."):
    if file.endswith(".mp3"):
      if tagFile(file)==-1:
	songFailed.append(file);

  print "\n\nThe following songs failed:"
  for song in songFailed:
    print song

  print "Total failures: ", len(songFailed)
  return songFailed


def groupFailedSons(failedSongs):
  failedDir="./failedTag"
  if not os.path.exists(failedDir):
    print "creating folder for failed songs"
    os.makedirs(failedDir)

  for songFile in failedSongs:
    os.rename("./"+songFile, "./"+failedDir+"/"+songFile)

def tagFile(fileName):
  #make robust if fails 
  print "\n"
  try:
    query= fileName.replace(".mp3","");
    result = id.smartSpotifyQuery(query)
    metaData = id.extractBasicMetadata(result)
    song = Song(fileName)
    song.fillMetadta(metaData)
    return 0
  except:
    print "Failed to tag: ", fileName
    return -1

failedSongs = tagDir();
groupFailedSons(failedSongs)
