import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host # server IP address
        self.port = port # server port number
        self.clients = {} # dictionary to keep track of connected clients and their addresses

    def start(self):
        # create a TCP/IP socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind the socket to a specific address and port
        self.socket.bind((self.host, self.port))
        # listen for incoming connections
        self.socket.listen()
        print(f"Server listening on {self.host}:{self.port}...")

        while True:
            # wait for a new client to connect
            client_socket, address = self.socket.accept()
            print(f"New client connected from {address[0]}:{address[1]}")
            # add the client's socket and address to the dictionary of connected clients
            self.clients[client_socket] = address
            # create a new thread to handle the client's messages
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()

    def broadcast(self, message, sender_socket):
        # send the message to all connected clients except the sender
        for client_socket, address in self.clients.items():
            if client_socket != sender_socket:
                client_socket.send(message)

    def handle_client(self, client_socket):
        # get the client's address from the dictionary of connected clients
        client_address = self.clients[client_socket]
        self.broadcast(bytes(f"{client_address[0]}:{client_address[1]} has connected", 'utf-8'), client_socket)
        while True:
            try:
                # receive a message from the client
                message = client_socket.recv(1024)
                if message and message.decode('utf-8').lower() != 'quit':
                    # add the sender's address to the message
                    message_with_address = f"{client_address[0]}:{client_address[1]} says: {message.decode('utf-8')}"
                    # broadcast the message to all connected clients except the sender
                    self.broadcast(bytes(message_with_address, 'utf-8'), client_socket)
                else:
                    # if there's no message, remove the client from the list of connected clients and close its socket
                    print(f"{client_address[0]}:{client_address[1]} has disconnected")
                    self.broadcast(bytes(f"{client_address[0]}:{client_address[1]} has disconnected", 'utf-8'), client_socket)
                    del self.clients[client_socket]
                    client_socket.close()
                    break
            except:
                # if there's an error, remove the client from the list of connected clients and close its socket
                del self.clients[client_socket]
                client_socket.close()
                break

if __name__ == "__main__":
    # create a new server object and start listening for connections
    server = Server("localhost", 56234)
    server.start()
