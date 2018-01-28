
class Closeable(object):

    def __init__(self, closeable):
        self.closeable = closeable

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        self.closeable.close()

