import select
import errno

class EpollServer:
    def __init__(self):
        self._shutdown = False
        self.epoll = select.epoll()
        self.fds = {}

    def shutdown(self):
        self._shutdown = True

    def add_epoll_fd(self, fd, events, callback = None):
        self.epoll.register(fd, events)
        self.fds[fd] = callback

    def del_epoll_fd(self, fd):
        if fd in self.fds:
            self.epoll.unregister(fd)
            del self.fds[fd]

    def run_forever(self):
        def _eintr_retry(func, *args):
            while True:
                try:
                    return func(*args)
                except OSError as e:
                    if e.errno == errno.EINTR:
                        raise

        while not self._shutdown:
            events = self.epoll.poll(1)
            for fd, event in events:
                if fd in self.fds:
                    try:
                        self.fds[fd].callback(fd, event)
                    except Exception as e:
                        pass



