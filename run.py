from plot import *

d = Document(
    orientation = "landscape",
    debug = True,
    pages = [
        Page(
            layout = [2,2],
            layout_tiles = [[1,1,2,3],[2,1,3,2],[2,2,3,3]],
            contents = [
                BarPlot(
                    contents=1,
                    categoryAxis = CategoryAxis(
                        labels = Label(angle = -15)
                    )
                ),
                BarPlot(contents=1),
                BarPlot(contents=1),
            ]),
        ]
)
print d
d.render()
