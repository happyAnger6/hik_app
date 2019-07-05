import ctypes

class CLibWrap:
    def __init__(self, name):
        self.name = name
        self.handle = ctypes.cdll.LoadLibrary(name)

    def __getattr__(self, item):
        return self.handle.__getattr__(item)

    def __getitem__(self, item):
        return self.handle.__getitem__(item)

class CLib:
    def __init__(self):
        self.libs = {}

    def __getattr__(self, name):
        def check_lib_name(name):
            if name.startswith('__') and name.endswith('__'):
                raise AttributeError(name)

        check_lib_name(name)
        lib = self.__getitem__(name)
        return lib

    def __getitem__(self, item):
        if item not in self.handles:
            libname = "lib%s.so" % item
            self.libs[item] = CLibWrap(libname)

        return self.libs[item]

clib = CLib()
