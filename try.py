import socket
 import sys


def socket_service_data():

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.bind(('2001:da8:270:2020:f816:3eff:fecf:ea39', 6666))  


        s.listen(10)

    except socket.error as msg:

        print(msg)

        sys.exit(1)

 

    print("Wait for Connection..................")

 

    while True:

        sock, addr = s.accept()

        buf = sock.recv(1024)  

        buf = buf.decode()  

        print("The data from " + str(addr[0]) + " is " + str(buf))

        print("Successfully")

        # return buf

        # sock.close()

if __name__ == '__main__':

    socket_service_data()
