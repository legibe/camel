import reportlab.lib.pagesizes as pageSizes
from reportlab.platypus import BaseDocTemplate, NextPageTemplate, PageBreak
from directive import Directive

class Document(Directive):

    def __init__(self,*args,**kwargs):
        super(Document,self).__init__(*args,**kwargs)
        Directive.debug(self['debug'])

    def render(self):
        document = BaseDocTemplate(
                self['filename'],
                pageSize = self.pageSize(),
                showBoundary=Directive.debug(),
                allowSplitting = False,
                **self.margins()
        )
        templates = []
        for i,page in enumerate(self['pages']):
            templates.append(page.pageTemplate(document,'page%d' % (i+1)))
        elements = []
        for i,page in enumerate(self['pages']):
            elements += page.render()
            if i < len(self['pages']) - 1:
                elements.append(NextPageTemplate('page%d' % (i+2)))
                elements.append(PageBreak())
        document.addPageTemplates(templates)
        document.build(elements)

    def pageSize(self):
        size = self['page_size']
        orientation = self['orientation']
        return getattr(pageSizes,orientation)(getattr(pageSizes,size))

    def margins(self):
        m = {}
        for k in self:
            if k.find('Margin') != -1:
                m[k] = self[k]
        return m
