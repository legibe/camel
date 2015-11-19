from reportlab.graphics.shapes import Drawing

class Plot(Drawing):

    def __init__(self,*args,**kwargs):
        Drawing.__init__(self,*args,**kwargs)
