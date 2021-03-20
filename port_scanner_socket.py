import socket

ip = '192.168.0.28'
port_list = [20, 21, 22, 25, 26, 80, 8080, 23, 139, 445]

for port in port_list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip, port))

    if result == 0:
        print('-' * 60)
        print('Port: ', port, 'open')
        print('-' * 60)
    else:
        print('Port: ', port, 'close')
