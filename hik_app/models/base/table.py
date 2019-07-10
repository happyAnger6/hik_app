from hik_app.models.base.fields import BaseField

class AutoFiledName(type):
    def __new__(cls, clsname, bases, methods):
        for k, v in methods.items():
            if isinstance(v, BaseField):
                v.name = k
                print(v.name)
        return type.__new__(cls, clsname, bases, methods)

class Table(object):

    def __init__(self):
        self._table_fileds = {}

    def add_field(self, key, value):
        self._table_fileds[key] = value

    def toXml(self):
        '''
        xml = ''
        for k, v in self._fields.items():
            xml += v.to_xml(self.json_str)
        if self.row_name:
            xml = '<{0!s}>{1!s}<0!s>'%(self.row_name, xml)
        return xml
        :return:
        '''
        xml = ''
        for k, v in self._table_fileds.items():
            xml += '<%s>%s<%s>'%(k, v, k)
        rowname = getattr(self, 'rowname', None)
        if rowname is not None:
           xml = '<%s>%s<%s>'%(rowname, xml, rowname)
        print(xml)
        return xml

    def toJson(self):
        '''

        :return:
        '''

    @classmethod
    def buildFromXml(cls, xml):
        '''

        :param xml:
        :return:
        '''
        for k, v in cls.__dict__.items():
            if isinstance(v, BaseField):
                print(k, v)

    @classmethod
    def buildFromJson(cls, json_obj):
        '''

        :return:
        '''
