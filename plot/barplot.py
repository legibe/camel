from reportlab.lib import colors
from reportlab.graphics.charts.barcharts import HorizontalBarChart,VerticalBarChart
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.legends import Legend
from renderable import Renderable
from plot import Plot
from categoryaxis import ValidCategoryAxis
from valueaxis import ValidValueAxis
from label import ValidLabel

class BarPlot(Renderable):

    exclude = set(['debug'])

    def setAttributes(self,target,obj):
        for k,i in obj.items():
            if not k in self.exclude:
                setattr(target,k,i)
    
    def render(self,width,height):
        contents = []
        ten_percent_width = width * 0.1
        ten_percent_height = height * 0.1
        g_width = width - ten_percent_width
        g_height = height - ten_percent_height
        drawing = Plot(g_width, g_height)
        horizontal = self['orientation'] == 'horizontal'
        axes = {}
        if horizontal:
            bar = HorizontalBarChart()
        else:
            bar = VerticalBarChart()

        bar.x = ten_percent_width
        bar.y = ten_percent_height
        bar.width = g_width - ten_percent_width
        bar.height = g_height - ten_percent_height
        bar.data = [[1,4,8,5,7],[2,6,4,8,1],[4,2,7,4,4],[4,2,7,1,2]]
        barColors = [0x50626F,0xFA7F36,0x42A7CA,0x1EBAA6]
        for i in range(len(bar.data)):
            bar.bars[i].fillColor = colors.HexColor(barColors[i])
        #bar.categoryAxis.style = 'stacked'

        vaxis = ValidValueAxis(self.get('valueAxis',{}))
        self.setAttributes(bar.valueAxis,vaxis)
        bar.valueAxis.valueMin = 0
        bar.valueAxis.valueMax = 9
        self.setAttributes(bar.valueAxis.labels,ValidLabel(self.get('labels',{})))

        bar.categoryAxis.labels.dx = 0
        bar.categoryAxis.labels.boxAnchor = 'ne'
        if horizontal:
            bar.categoryAxis.labels.dx = -8
        else:
            bar.categoryAxis.labels.dx = 8
        bar.categoryAxis.labels.dy = -2
        bar.categoryAxis.labels.angle = 15
        bar.categoryAxis.labels.fontSize = 8
        bar.categoryAxis.labels.fontName = 'Helvetica'
        bar.categoryAxis.categoryNames = ['May','Jun','Jul','Aug','Sep']
        bar.barLabels.nudge = 7

        bar.barLabels.fontName = 'Helvetica'
        bar.barLabels.fontSize = 6

        drawing.add(bar)
        contents.append(drawing)

        return contents
