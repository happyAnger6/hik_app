class BaseField(object):
    def __init__(self,
                 name=None,
                 **kwargs):
        self.name = name
        self.__dict__.update(kwargs)


    def __set__(self, instance, value):
        instance.add_field(self.name, value)
        instance.__dict__[self.name] = value

class Typed(BaseField):
    expected_type = type(None)
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected type' + str(self.expected_type))

        super(Typed, self).__set__(instance, value)

class UintField(Typed):
    expected_type = int
    def __set__(self, instance, value):
        if value < 0:
            raise TypeError('Expected unsigned value' + str(self.value))

        super(UintField, self).__set__(instance, value)

class DoubleField(Typed):
    expected_type = float

class StringField(Typed):
    expected_type = str

class EnumField(BaseField):
    expected_type = int

class GroupField(BaseField):
    pass
