class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("can't instantiate directly.")

class Spam():
    __metaclass__ = NoInstance
    @staticmethod
    def grok(x):
        print('Spam.grok')


if __name__ == "__main__":
    s = Spam()
