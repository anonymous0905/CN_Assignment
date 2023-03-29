import socket
import threading

class Client:
    def __init__(self, host, port):
        self.host = host # server IP address
        self.port = port # server port number

    def start(self):
        # create a TCP/IP socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect to the server
        self.socket.connect((self.host, self.port))
        print(f"Connected to server {self.host}:{self.port}")
        # start a thread to receive messages from the server
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        while True:
            # wait for the user to enter a message
            message = input()
            if message.lower() == 'quit':
                try:
                    # send the message to the server
                    self.socket.send(bytes(message, 'utf-8'))
                    self.socket.close()
                    exit(0)
                except:
                    self.socket.close()
                    exit(0)
                break
            else:
                # send the message to the server
                self.socket.send(bytes(message, 'utf-8'))

    def receive(self):
        while True:
            # wait for a message from the server
            message = self.socket.recv(1024)
            if message:
                # print the message
                print(message.decode('utf-8'))

if __name__ == "__main__":
    # create a new client object and start sending messages to the server
    client = Client("localhost", 56234)
    client.start()

#init push