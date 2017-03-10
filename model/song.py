import taglib

class Song:
  def __init__(self, FileName):
    self.song = taglib.File(FileName);

  def fillMetadta(self, basicMeta):
    print basicMeta
    self.setTitle(basicMeta["TITLE"][0])
    self.setArtist(basicMeta["ARTIST"][0])
    self.setAlbum(basicMeta["ALBUM"][0])
    self.save()

  def setTitle(self, newTitle):
    try:
      self.song.tags["TITLE"] = [newTitle]
    except:
      return -1
    return 1;

  def getTitle(self):
    return self.song.tags["TITLE"]


  def setArtist(self, newArtist):
    try:
      self.song.tags["ARTIST"] = [newArtist]
    except:
      return -1
    return 1;

  def getArtist(self):
    return self.song.tags["ARTIST"]

  def setAlbum(self, newAlbum):
    try:
      self.song.tags["ALBUM"] = [newALbum]
    except:
      return -1
    return 1;

  def getAlbum(self):
    return self.song.tags["ALBUM"]

  def save(self):
    return self.song.save();

  

  def printTags(self):
    print(self.song.tags)
