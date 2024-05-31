import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from ttkthemes import ThemedTk

class ServerGUI:
    def __init__(self):
        self.root = ThemedTk(theme="breeze")
        self.root.title("Server")

        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=True, fill='both')

        self.chat_frame = ttk.Frame(self.main_frame)
        self.chat_frame.pack(expand=True, fill='both', side='left')

        self.text_area = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both')
        self.text_area.config(state='disabled')

        self.users_frame = ttk.Frame(self.main_frame)
        self.users_frame.pack(fill='y', side='right')

        self.users_listbox = tk.Listbox(self.users_frame)
        self.users_listbox.pack(fill='y')

    def display_message(self, message):
        self.text_area.config(state='normal')
        self.text_area.insert('end', message + '\n')
        self.text_area.config(state='disabled')
        self.text_area.yview('end')

    def add_user(self, user_name):
        self.users_listbox.insert('end', user_name)

    def run(self):
        self.root.mainloop()
