import tkinter as tk

from modules.Controller import ActionsController


def main():
    root = tk.Tk()

    WIDTH, HEIGHT = 1280, 720
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.title("GAMESCORER")
    app = ActionsController(root)
    root.mainloop()

if __name__ == "__main__":
    main()