"""The stockTunes program

This is a script that will act as the MediaPlayer
It is the heart of the program and will handle the event management
"""

__author__ =  'Eli Katz'
__version__=  '1.0'

import time, random
import pyglet
import Player
import StockManager


class MediaPlayer():
    """
    Media Player Class
    It uses Event Managers to essentially recursively call changes on itself
    It handles errors by forwarding to the next song
    """
    def __init__(self, flag):
        """Constructor takes a test flag and then creates the Players and Stock Manager
        """
        self.happyplayer = Player.Player('happy')
        self.sadplayer = Player.Player('sad')
        self.clockTime = 30
        self.test = flag
        self.stocks = StockManager.StockManager()
        
    def playHappy(self):
        """Plays the Happy Playlist
        It calls the scheduler of pyglet to make sure
        that the check is called during the app.run
        """
        self.sadplayer.pause()
        self.happyplayer.play()
        pyglet.clock.schedule_once(self.check, self.clockTime)
        pyglet.app.run()
        
    def playSad(self):
        """Plays the Sad Playlist
        It calls the scheduler of pyglet to make sure
        that the check is called during the app.run
        """
        self.happyplayer.pause()
        self.sadplayer.play()
        pyglet.clock.schedule_once(self.check, self.clockTime)
        pyglet.app.run()
        
    def check(self, dt):
        """Checks for changes in the condition. A positive change will trigger
        the happy playlist while a negative change will trigger a sad playlist
        In the event of an error it will attempt to play the next song
        """
        if (self.playCond()):
            try:
                print "Positive Change"
                pyglet.app.exit()
                pyglet.clock.unschedule(self.check)
                self.playHappy()
            except:
                print "Happy Song Error - Next Song"
                self.happyplayer.loadSongs()
                self.happyplayer.next()
                pyglet.app.exit()
                pyglet.clock.unschedule(self.check)
                self.playHappy()
        else:
            try:
                print "Negative Change"
                pyglet.app.exit()
                pyglet.clock.unschedule(self.check)
                self.playSad()
            except:
                print "Sad Song Error - Next Song"
                self.sadplayer.loadSongs()
                self.sadplayer.next()
                pyglet.app.exit()
                pyglet.clock.unschedule(self.check)
                self.playSad()
        
    def playCond(self):
        """
        Test the condition of the change whether the stock change or through a random
        number
        """      
        if (self.test):
            return (random.randint(-5, 5) >= 0) 
        else:
            return (self.stocks.getChange >= 0)
        
            
    def start(self):
        """Start the media player
        """
        self.check(1)