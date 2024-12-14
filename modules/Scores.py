import tkinter as tk
from PIL import Image, ImageTk

def create_canvas(container):
    canvas = tk.Canvas(
        container,
        bg="#F3F3F3",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    return canvas

def create_score_text(canvas):
    score1 = canvas.create_text(
        257.0,
        264.0,
        anchor="nw",
        text=0,
        fill="#000000",
        font=("NeueHaasDisplay Light", 150 * -1)
    )
    score2 = canvas.create_text(
        733.0,
        264.0,
        anchor="nw",
        text="0",
        fill="#000000",
        font=("NeueHaasDisplay Light", 150 * -1)
    )
    return score1, score2

def create_button_image(file_path):
    return ImageTk.PhotoImage(Image.open(file_path))

def create_button(canvas, image, command):
    button = tk.Button(canvas, image=image, borderwidth=0, highlightthickness=0, command=command, relief="flat")
    return button
