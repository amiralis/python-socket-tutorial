# Amirali Sanatinia amirali@ccs.neu.edu
# Network Security Java Socket Programming Demo

import socket
import threading
import time

MAX_UDP = 65507  # Maximum UDP size

""" We want to send each UDP packet in one thread
this is not exactly the correct or smart way of doing
things. It's just for demo purposes on how to use
threading and socket programming """


class UDPClient(threading.Thread):

    def __init__(self, thread_number, server_ip, server_port):
        threading.Thread.__init__(self)
        self.thread_number = thread_number
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_ip = server_ip
        self.server_port = server_port

    def run(self):
        print "Thread %d sent a packet" % (self.thread_number, )
        self.client_socket.sendto("Hello There", (self.server_ip, self.server_port))


if __name__ == '__main__':
    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 9999

    # Create new threads
    i = 0
    while True:
        UDPClient(i, SERVER_IP, SERVER_PORT).start()
        time.sleep(0.5)
        i += 1