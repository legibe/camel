from  platin.language.validate import Validate
from directive import Directive

class Renderable(Directive):

    def render(self,width,height):
        return []

class IsRenderable(object):

    def __call__(self, schemas, keyword, value, request):
        for x in value:
            if not isinstance(x,Renderable):
                raise TypeError('Expecting a Renderable object in %s, received %s instead' % (keyword,type(x)))
        return value

Validate.register('is-renderable', IsRenderable)
