Readme 
Elliot Katz
epk2102


Required Libraries:
Pyglet - http://www.pyglet.org/download.html
AVBin - http://code.google.com/p/avbin/

It also uses ystockquote which is included as a source file


To Run:
Place several mp3 files in both the happy and sad folders
python stockTunes.py

You can use optional flag -t or --test when the stock market is closed to get random
values for the stockTunes program to test it.

I've changed the class structure from the original assignment. Song and SongList wasn't
enough of a data structure to warrant its own class. Stocks are just a List.

The complexity of the project is the media playing. The songs are triggered through the 
event handeling. The process cannot check for a condition while it is still playing but
we don't want to stop the playing while checking. We use scheduling to stop and start the
check and playback without the user noticing.

Classes:
Player - Both Happy and Sad Players
StockManager - Encapsulates the ystockquote
MediaPlayer - Controls the basic playback