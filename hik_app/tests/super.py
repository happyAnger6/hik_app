class A:
    def __init__(self):
        print('A init')


class B(A):
    pass

if __name__ == "__main__":
    b = B()
