import wx
import json
import threading

"""
A wxPython Frame that serves to show motes' positions
"""
class Topology(wx.Frame):

    def __init__(self, *args, **kw):
        super(Topology, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetTitle("Network topology")
        self.SetSize((650, 400))
        self.Centre()

    def _drawTopology(self):

        dc = wx.PaintDC(self)
        dc.SetBrush(wx.Brush('#777'))
        dc.SetPen(wx.Pen("#777"))

        # Retrieve positions from a json file
        with open('D:\Recherche\Tools\\6tisch-misbehavior\\bin\positions.json') as pos:
            locations = json.load (pos)

        # x-axis and y-axis unit in the frame
        x_unit = 50
        y_unit = 50

        # Draw motes as circles in the corresponding positions on the frame
        for location in locations:
            dc.DrawCircle(location[0]* x_unit, location[1]* y_unit, 15)

    def OnPaint(self, e):
        self._drawTopology()

"""
A thread that allows non-blocking frame
"""
class FrameThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        app = wx.App()
        ex = Topology(None)
        ex.Show()
        app.MainLoop()

"""
Define positions of motes
"""
# Positions are set to form a tree
# currentLevelIds holds the IDs of one level of the three
# allIds holds the IDs of all levels

def motesLocations(motesIds):
    currentIndex = 0
    currentLevelSize = 1
    currentLevelIds = []
    allIds = []

    for i in range(len(motesIds)):
        if currentIndex < currentLevelSize:
            currentLevelIds.append(motesIds[i])
            currentIndex = currentIndex + 1
        else:
            currentLevelSize = currentLevelSize + 1
            e = list(currentLevelIds)
            allIds.append(e)
            del currentLevelIds [:]
            currentIndex = 0
            currentLevelIds.append(motesIds[i])
            currentIndex = currentIndex + 1

    e = list(currentLevelIds)
    allIds.append(e)
    print (allIds)

    # Position of the tree (the root)
    x_base = len(allIds) + 1
    y_base = 0

    # Deduce positions from the list allIds
    locations = []
    for i in range(len(allIds)):
        for j in range(len(allIds[i])):
            locations.append((x_base - i + j * 2 , y_base + i + 1))

    return locations