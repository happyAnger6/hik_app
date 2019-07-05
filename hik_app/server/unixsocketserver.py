import os
import socket
import select

from threading import Thread

from hik_app.utils.epoll import EpollServer

class UnixSocketServer(EpollServer, Thread):
    def __init__(self, path):
        self._path = path

    def run(self):
        if os.path.exists(self._path):
            os.remove(self._path)
        self._server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        self._server.bind(self._path)
        self._server_fd = self._server.fileno()
        self.add_epoll_fd(self._server_fd, select.EPOLLIN)
        self.run_forever()
