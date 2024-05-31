import tkinter as tk
from tkinter import ttk, simpledialog, scrolledtext
from ttkthemes import ThemedTk

class ClientGUI:
    def __init__(self):
        self.send_message_callback = None

        self.root = ThemedTk(theme="breeze")
        self.root.title("Client")

        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=True, fill='both')

        # Left frame for user list
        self.user_list_frame = ttk.Frame(self.main_frame, width=200)
        self.user_list_frame.pack(side='left', fill='y')

        self.user_list_label = ttk.Label(self.user_list_frame, text="Users", anchor="center")
        self.user_list_label.pack(fill='x')

        self.user_listbox = tk.Listbox(self.user_list_frame)
        self.user_listbox.pack(expand=True, fill='y')

        # Right frame for chat
        self.chat_frame = ttk.Frame(self.main_frame)
        self.chat_frame.pack(side='left', expand=True, fill='both')

        self.chat_text_area = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD)
        self.chat_text_area.pack(expand=True, fill='both')
        self.chat_text_area.config(state='disabled')

        self.entry_frame = ttk.Frame(self.chat_frame)
        self.entry_frame.pack(fill='x')

        self.entry = ttk.Entry(self.entry_frame)
        self.entry.pack(side='left', expand=True, fill='x', padx=5, pady=5)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = ttk.Button(self.entry_frame, text="Send", command=self.send_message)
        self.send_button.pack(side='left', padx=5, pady=5)

        self.user_name = simpledialog.askstring("Input", "Enter your user name:")

    def set_send_message_callback(self, callback):
        self.send_message_callback = callback

    def send_message(self, event=None):
        message = self.entry.get()
        if message:
            self.entry.delete(0, 'end')
            self.display_message(f"You: {message}\n")
            if self.send_message_callback:
                self.send_message_callback(message, self.user_name)

    def display_message(self, message):
        self.chat_text_area.config(state='normal')
        self.chat_text_area.insert('end', message)
        self.chat_text_area.config(state='disabled')
        self.chat_text_area.yview('end')

    def add_user(self, user_name):
        self.user_listbox.insert('end', user_name)

    def run(self):
        self.root.mainloop()
