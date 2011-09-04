"""The stockTunes program

This is a script that will act as Player class
There are two Players, happy and sad
"""

__author__ =  'Eli Katz'
__version__=  '1.0'

import os, sys
import pyglet

class Player():
    """The player class encapsulates basic player options
    and it also loads songs
    """
    player = pyglet.media.Player()
    name = ""
    
    def __init__(self, path):
        """
        Constructor takes a path to happy and sad folders
        """
        self.player = pyglet.media.Player()
        self.name = path
        self.loadSongs()
        
    def loadSongs(self):
        """
        Load Songs into the queue
        This will search the directory and load all songs
        """
        try:
            path = self.name
            SongFolder = os.listdir(path)
            for song in SongFolder:
                self.player.queue(pyglet.media.load(os.path.join(path, song)))
        except:
            print "There is a non-song file in the folder"
            sys.exit(2)
        
    def play(self): 
        """Play"""
        self.player.play()
        
    def pause(self):
        """Pause"""
        self.player.pause()
    
    def next(self):
        """Next"""
        self.player.next()