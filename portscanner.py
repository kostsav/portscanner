import socket
import threading
from queue import Queue

target = input("IP Address: ")
queue = Queue()
open_ports = []


def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True

    except:
        return False


def fill_queue(port_list):
    for port in port_list:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f"Port {port} is open!")
            open_ports.append(port)


start_port = int(input("Give start port: "))
end_port = int(input("Give end port: "))
port_list =  range(start_port, end_port+1)
fill_queue(port_list)
thread_list = []

for t in range(100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

if open_ports:
    print(f"Open ports: {open_ports}")
else:
    print(f"No open ports from {start_port} to {end_port}.")
