class BaseField:
    def __init__(self,
                 xml_field=None,
                 required=False,
                 **kwargs):
        self.xml_field = xml_field

        self.__dict__.update(kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance._data.get(self.name)
