import socket
from struct import pack

#Create a UDP socket
class UDP_Socket:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = host #192.168.178.186 is adress pi, 192.168.178.178 is pc
        self.port = port 
        self.server_address = (host, port)
        
    def pack_float(self, dist_frnt, dist_lft, dist_rght, odometry, end):
        msg = pack('5f', dist_frnt, dist_lft, dist_rght, odometry, end)
        self.sock.sendto(msg, self.server_address)
        
    def pack_end_message(self, x):
        msg = pack('1i', x)
        self.sock.sendto(msg, self.server_address)
        
if __name__ == "__main__":
    pass