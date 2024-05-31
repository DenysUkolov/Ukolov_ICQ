import socket
import threading
from server_gui import ServerGUI

class Server:
    def __init__(self, gui):
        self.clients = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('127.0.0.1', 3320))
        self.server.listen()

        self.gui = gui

    def accept_clients(self):
        while True:
            client, addr = self.server.accept()
            self.clients.append(client)
            self.gui.add_user(f"{addr}")
            threading.Thread(target=self.handle_client, args=(client,)).start()

    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if not message:
                    break
                self.broadcast(message, client)
                self.gui.display_message(message)
            except:
                self.clients.remove(client)
                client.close()
                break

    def broadcast(self, message, sender_client):
        for client in self.clients:
            if client != sender_client:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    client.close()
                    self.clients.remove(client)

if __name__ == "__main__":
    gui = ServerGUI()
    server = Server(gui)
    
    accept_thread = threading.Thread(target=server.accept_clients)
    accept_thread.daemon = True
    accept_thread.start()
    
    gui.run()
