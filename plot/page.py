from reportlab.platypus import PageBreak, PageTemplate, Frame
from directive import Directive

class Page(Directive):

    order = 0

    def render(self):
        contents = []
        coords = 0
        for item in self['contents']:
            if coords < len(self._coords):
                contents += item.render(self._coords[coords][2],self._coords[coords][3])
            coords += 1
        return contents

    def pageTemplate(self,document,pageID):
        self._frames, self._coords = self.tiles(document)
        return PageTemplate(id=pageID,frames=self._frames)

    def tiles(self,document):
        layout = self['layout']
        layout_tiles = self['layout_tiles']
        if not len(layout_tiles):
            layout_tiles = self.make_layout_tiles(layout)
        tilew = (document.width / layout[0])
        tileh = (document.height / layout[1])
        tiles = []
        coords = []
        for tile in layout_tiles:
            w = tilew * (tile[2] - tile[0])
            h = tileh * (tile[3] - tile[1])
            x = (tile[0] - 1) * tilew
            y = document.height - (tile[3]-1) * tileh
            self.order += 1
            frame = Frame(document.leftMargin + x, document.bottomMargin + y, w, h, id='tile%d' % self.order)
            tiles.append(frame)
            coords.append([document.leftMargin + x, document.bottomMargin + y, w, h])
        return tiles, coords

    def make_layout_tiles(self,layout):
        tiles = []
        y = 1
        for i in range(layout[1]):
            x = 1
            for j in range(layout[0]):
                d = [x,y,x+1,y+1]
                x += 1
                tiles.append(d)
            y += 1
        return tiles
