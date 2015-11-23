from directive import Directive

class Label(dict):
    pass

class ValidLabel(Directive):
    __schema__ = 'label'
