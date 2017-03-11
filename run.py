import os

import config
from model.song import Song
from tagging.tagger import Tagger

tagger = Tagger()

#goes through all songs in the directory, calls tagFile
def tagDir(dir=config.DIR_UNTAGGED):
    print("tagging songs")
    for filename in os.listdir(dir):
        if filename.endswith(".mp3"):
            song = Song(dir, filename)
            if tagger.tag_song(song) == -1:
                song.save(config.DIR_FAILED_TAG)
            else: #song was succesfully tagged move it to completed songs
                song.save(config.DIR_TAGGED)


def rip_playlist(playlist_url):
    #youtube-dl  --extract-audio --yes-playlist --audio-format mp3 -o '%(playlist)s/%(title)s.%(ext)s'
    args = ["--extract-audio", "--yes-playlist", "--audio-format mp3", "-o 'songs/untaggedSongs/%(title)s.%(ext)s'", playlist_url]
    command = "youtube-dl"
    for arg in args:
        command += " " + arg
    print(command)
    os.system(command)

def print_prompt():
    help_text = "help"
    print(help_text)


os.system("youtube-dl")

while True:
    input_cmd = raw_input("What do you want to do?")
    print(input_cmd)
    cmd= input_cmd.rstrip().split(" ")
    if '?' == cmd[0]:
        print_prompt()
    elif "tag" == cmd[0]:
        tagDir(config.DIR_UNTAGGED)
    elif "rip" == cmd[0]:
        rip_playlist(cmd[1])
    elif 'q' == cmd[0]:
        break
    else:
        print_prompt()