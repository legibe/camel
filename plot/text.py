from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from renderable  import Renderable

class Text(Renderable):
    
    def render(self,width,height):
        styles=getSampleStyleSheet()
        contents = []
        paragraphs = self['contents'].split('\n')
        for paragraph in paragraphs:
            contents.append(Paragraph(paragraph,styles['Normal']))
        return contents
