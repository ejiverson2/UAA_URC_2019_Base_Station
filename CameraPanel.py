import wx
import MPembed1 as mp

class CameraPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=42)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.whnd = self.GetHandle()
                
    def StartPlayer(self):
        self.player = mp.MPembed(self.whnd, ["R\\LuckyStarOp.mp4"])