# Amirali Sanatinia amirali@ccs.neu.edu
# Network Security Java Socket Programming Demo

import socket

MAX_UDP = 65507  # Maximum UDP size


class ServerSocket():
    def __init__(self, ip, port):
        self.server_socket = socket.socket(socket.AF_INET,
                                           socket.SOCK_DGRAM)  # UDP
        self.server_socket.bind((ip, port))

    def start(self):
        while True:
            data, addr = self.server_socket.recvfrom(MAX_UDP)
            print "%s sent %s" % (addr, data)


if __name__ == '__main__':
    UDP_server_socket = ServerSocket('127.0.0.1', 9999)
    UDP_server_socket.start()