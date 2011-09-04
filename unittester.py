import stockTunes
import unittest
import MediaPlayer
import Player
import StockManager
import ystockquote

class TestSequenceFunctions(unittest.TestCase):
    
    def setUp(self):
        self.symbol = "AAPL"
        self.stock = "Apple"
        self.s = StockManager.StockManager()
        self.p = Player.Player('happy')
        self.m = MediaPlayer.MediaPlayer(True)

    def test_Cond(self):
        self.assertTrue(self.m.playCond())
        
    def test_isvalid(self):
        self.assertTrue(self.s.isValid(self.symbol))
        
    def test_addQueue(self):
        self.assertTrue(self.p.loadSongs())
        
    def test_getChange(self):
        lv = self.getChange()
        self.assertEqual(lv, self.s.getChange()) 
        
    def test_getSongPath(self):
        self.assertEqual('happy', self.p.name)
        
        
if __name__ == '__main__':
    unittest.main()