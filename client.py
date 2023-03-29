import socket
import threading
import base64

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
                # if the user enters "quit", send a message to the server and exit the loop
                self.socket.send(bytes(message, 'utf-8'))
                # close the client socket
                self.socket.close()
                break
            else:
                # encode the message using base64
                encoded_message = base64.b64encode(bytes(message, 'utf-8'))
                # send the encoded message to the server
                self.socket.send(encoded_message)

    def receive(self):
        while True:
            # wait for a message from the server
            message = self.socket.recv(1024)
            if message:
                # decode the message using base64
                decoded_message = base64.b64decode(bytes(message,'utf-8').decode('utf-8'))
                # print the message
                print(decoded_message)

if __name__ == "__main__":
    # get the user's username
    username = input("Enter your username: ")
    # create a new client object and start sending messages to the server
    client = Client("localhost", 56234)
    client.start()
