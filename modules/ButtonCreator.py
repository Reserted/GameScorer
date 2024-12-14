import tkinter as tk
from PIL import ImageTk, Image
from pubsub import pub
class ButtonAbstraction:
    def __init__(self, master, image_path_content_root, command,message):
        self.master = master
        self.image_path = image_path_content_root
        self.command = command
        self.button_image = None
        self.button = None
        self.message = message


    def create_button(self):
        self.button_image = ImageTk.PhotoImage(Image.open(self.image_path))
        self.button = tk.Button(self.master,
                                image=self.button_image,
                                borderwidth=4,
                                highlightthickness=4,
                                command=lambda: self.execute_command(),
                                relief="flat")
        return self.button

    def execute_command(self):

        pub.sendMessage(self.command,message=self.message)