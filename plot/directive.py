import os
from platin.language.language import Language

class Directive(dict):

    _debug = False

    def __init__(self,*args,**kwargs):
        if 'schema_path' in kwargs:
            self._schema_path = kwargs['schema_path']
        else:
            self._schema_path = os.path.join(os.path.dirname(__file__),'schema')
        super(Directive,self).__init__(*args,**kwargs)
        self._schema = self.__class__.__name__.lower()
        if hasattr(self,'__schema__'):
            self._schema = self.__schema__
        self.validate()

    @classmethod
    def debug(self,newvalue=None):
        if newvalue is not None:
            self._debug = newvalue
        return self._debug

    def validate(self):
        l = Language(self._schema,self._schema_path)
        for k,i in self.items():
            if isinstance(i,Directive):
                i.validate()
        new = l.validate(self)
        self.clear()
        self.update(new)

    def __cleanstr__(self,data,level):
        """ Keeping it just in case, but json.dumps does a better job """
        contents = []
        tab = ' ' * (level * 4)
        keys = sorted(data.keys())
        for k in keys: 
            key = str(k)
            key = tab + key + ': '
            posttab = ' ' * (14 - len(k)) + ' '
            if k[-1] == '_':
                value = '<blob>'
            else:
                i = data[k]
                if isinstance(i,dict):
                    key += ' {\n'
                    value = self.__cleanstr__(i,level+1) + '\n' + tab + '}'
                elif isinstance(i,list):
                    key += ' [\n'
                    rows = []
                    for x in i:
                        if isinstance(x,dict):
                            rows.append(tab + '{\n' + self.__cleanstr__(x,level+1) + '\n' + tab + '}')
                        else:
                            rows.append(' ' * (len(key)-len(tab)) + str(x))
                    value = ',\n'.join(rows)
                    value += '\n' + tab + ']'
                else:
                    value = str(i)
            contents.append('%s%s' % (key,value))
        return '\n'.join(contents)

    def substitute_hidden(self,struct):
        new = {}
        for k, i in struct.items():
            if k[-1] == '_':
                new[k] = '<blob>'
            elif isinstance(i,Directive):
                new[k] = self.substitute_hidden(i)
            elif isinstance(i,list):
                nn = []
                for e in i:
                    if isinstance(e,dict):
                        nn.append(self.substitute_hidden(e))
                    else:
                        nn.append(e)
                new[k] = nn
            else:
                new[k] = i
        return new
    
    def __str__(self):
        d = self.substitute_hidden(self)
        import json
        return json.dumps(d,indent=4)
