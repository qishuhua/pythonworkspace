# coding =utf-8
from socket import *
from threading import Thread


def main():
    server_sock = socket(AF_INET, SOCK_STREAM)

    address = ('127.0.0.1', 8000)
    server_sock.bind(address)


    server_sock.listen(5)

    try:
        while True:
            client_sock, addr = server_sock.accept()



            thread = Thread(target=work, args=(client_sock, addr,))
            thread.start()
    finally:
        server_sock.close()


def work(sock, addr):
    while True:
        data = sock.recv(1024)
        if len(data) > 0:
            print('recv:', data)
        else:
            print('client%s closed' % str(addr))
            break


if __name__ == '__main__':
    main()


