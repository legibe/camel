from reportlab.lib import colors
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.legends import Legend
from renderable import Renderable
from plot import Plot

class BarPlot(Renderable):
    
    def render(self,width,height):
        contents = []
        g_width = width * 0.85
        g_height = height * 0.90
        p_width = g_width
        p_height = g_height
        drawing = Plot(g_width-20, g_height-10)
        bar = VerticalBarChart()
        bar.x = 20
        bar.y = 0
        bar.width = g_width - 20
        bar.height = g_height - 10
        bar.data = [[1,4,8,5,7],[2,6,4,8,1],[4,2,7,4,4],[4,2,7,1,2]]
        bar.valueAxis.valueMin = 0
        bar.valueAxis.valueMax = 9
        #barColors = ['#50626F','#FA7F36','#42A7CA','#1EBAA6']
        #for i in range(len(bar.data)):
        #    bar.bars[i].fillColor = barColors[i]
        #bar.categoryAxis.style = 'stacked'

        bar.valueAxis.visibleGrid = True
        bar.valueAxis.labels.fontSize = 8
        bar.valueAxis.labels.fontName = 'Helvetica'
        bar.valueAxis.labelTextFormat = format
        bar.categoryAxis.labels.boxAnchor = 'ne'
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
