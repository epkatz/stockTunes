"""The stockTunes program

This is a script that will act as the stockTunes main
It doesn't contain a class itself but rather calls on Media Player
You can optionally pass a -t flag to trigger test mode when not
using during trading hours.
"""

__author__ =  'Eli Katz'
__version__=  '1.0'
    
import MediaPlayer 
import os, getopt, sys    
        
def playbackStart(flag):
    """Creates a new Media player and then calls start
    """
    m = MediaPlayer.MediaPlayer(flag)
    m.start()
    
    
def main(options):
    """main takes the flags, parses them and then calls the playbackStart
    """
    try:
        opt, args = getopt.getopt(options, ":t", ["test"])
    except getopt.GetoptError, err:
        print str(err)
        sys.exit(2)
    for o, a in opt:
        if o in ("-t", "--test"):
            flags['Test'] = True
               
    playbackStart(flags['Test'])
    
#flags controls whether it is in testing mode or not
flags = {'Test':False}

if __name__ == "__main__":
    main(sys.argv[1:])