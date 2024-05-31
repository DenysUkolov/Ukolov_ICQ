import socket
import threading
from client_gui import ClientGUI

class Client:
    def __init__(self, gui):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 3320))

        self.gui = gui
        self.gui.set_send_message_callback(self.send_message)

        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.daemon = True
        self.receive_thread.start()

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if not message:
                    break
                self.gui.display_message(message)
            except:
                print("An error occurred.")
                self.client.close()
                break

    def send_message(self, message, user_name):
        self.client.send(f"{user_name}: {message}".encode('utf-8'))

if __name__ == "__main__":
    gui = ClientGUI()
    client = Client(gui)
    
    gui.run()


