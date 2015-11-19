import cgi
from directive import Directive
from renderable import Renderable

class HTMLTable(Renderable):

    __schema__ = 'table'

    def render(self,width,height):
        alternate = []
        if 'alternate_row' in self:
            alternate = self['alternate_row']
        rendered = []
        if 'title' in self:
            rendered.append('<p class="table-title">%s<p>' % (cgi.escape(self['title'])))
        rendered.append('<table>')
        trs = ['tr'] * len(self['data_'])
        _id = 0
        for tr,row in enumerate(self['data_']):
            attr = ''
            if len(alternate):
                attr = 'id="%s" ' % alternate[_id]
                _id += 1
                if _id == len(alternate):
                    _id = 0
            rendered.append('<%s %s>' % (trs[tr],attr))
            for td,column in enumerate(row):
                tds = ['td'] * len(row)
                if self['has_header'] and self['header_position'] == 'left':
                    tds[0] = 'th'
                elif tr == 0 and self['has_header'] and self['header_position'] == 'top':
                    tds = ['th'] * len(row)
                rendered.append('<%s>%s</%s>' % (tds[td],cgi.escape(str(column)),tds[td]))
            rendered.append('</%s>' % trs[tr])
        rendered.append('</table>')
        return '\n'.join(rendered)
