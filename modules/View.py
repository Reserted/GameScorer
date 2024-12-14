import os
import tkinter as tk
from pathlib import Path

from modules.ButtonCreator import ButtonAbstraction
from modules.Scores import create_score_text


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(fr"{os.getcwd()}\assets\frame0")

class View:
    def __init__(self, parent):
        self.all_canvases = {}
        self.container = parent
        self.current_canvas = None
        self.top_frame = None
        self.number1 = 0
        self.number2 = 0

    def setup(self):
        self.create_all_canvases()
        # self.create_widgets()
        self.setup_layout()
    def create_all_canvases(self):



        self.SoccerCanvas = self.create_canvas("SoccerCanvas")
        self.BasketballCanvas = self.create_canvas("BasketballCanvas")
        self.StartScreenCanvas = self.create_canvas("StartScreenCanvas")
        self.StartProgramCanvas = self.create_canvas("StartProgramCanvas")

        self.create_start_program_widgets(self.StartProgramCanvas)
        self.create_start_screen_widgets(self.StartScreenCanvas)
        self.create_basketball_widgets(self.BasketballCanvas)
        self.create_soccer_screen_widget(self.SoccerCanvas)

        self.all_canvases["StartScreenCanvas"] = self.StartScreenCanvas
        self.all_canvases["BasketballCanvas"] = self.BasketballCanvas
        self.all_canvases["SoccerCanvas"] = self.SoccerCanvas
        self.all_canvases["StartProgramCanvas"] = self.StartProgramCanvas
        self.current_canvas = "StartProgramCanvas"

    def create_canvas(self, canvas_name):
        canvas = tk.Canvas(
            self.container,
            bg="#F3F3F3",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        return canvas

    def switch_canvas(self, canvas_name):
        if canvas_name not in self.all_canvases:
            print(f"Invalid canvas name: {canvas_name}")
            return

        # Hide the current canvas
        if self.current_canvas:
            self.all_canvases[self.current_canvas].place_forget()

        # Show the selected canvas
        self.all_canvases[canvas_name].place(x=0, y=0)
        self.update_button_layout()

        # Update the current canvas reference
        self.current_canvas = canvas_name

    def update_button_layout(self):
        if self.current_canvas == "StartScreenCanvas":
            # Update positions for StartScreenCanvas buttons
            self.button_1_1.place(x=589.0, y=599.0, width=102.0, height=72.0)
            self.button_1_2.place(x=73.0, y=156.0, width=532.0, height=430.0)
            self.button_1_3.place(x=652.0, y=156.0, width=532.0, height=430.0)
        elif self.current_canvas == "BasketballCanvas":
            # Update positions for BasketballCanvas buttons
            self.button_place_basketball()
        elif self.current_canvas == "StartProgramCanvas":
            self.button_1_1.place(relx=0.5, rely=0.5, anchor='center')


    def button_place_basketball(self):
        self.button_1.place(x=123.0, y=469.0, width=106.0, height=72.0) #1
        self.button_2.place(x=250.0, y=469.0, width=106.0, height=72.0) #2
        self.button_3.place(x=377.0, y=469.0, width=106.0, height=72.0) #3

        self.button_7.place(x=123.0, y=557.0, width=106.0, height=72.0) #1
        self.button_8.place(x=250.0, y=557.0, width=106.0, height=72.0) #2
        self.button_9.place(x=377.0, y=557.0, width=106.0, height=72.0) #3

        self.button_4.place(x=601.0, y=469.0, width=106.0, height=72.0) #-1
        self.button_5.place(x=729.0, y=469.0, width=106.0, height=72.0) #-2
        self.button_6.place(x=857.0, y=469.0, width=106.0, height=72.0) #-3

        self.button_10.place(x=601.0, y=557.0, width=106.0, height=72.0)
        self.button_11.place(x=729.0, y=557.0, width=106.0, height=72.0)
        self.button_12.place(x=857.0, y=557.0, width=106.0, height=72.0)

        self.button_13.place(x=481.0, y=384.0, width=124.0, height=53.0)
        self.button_14.place(x=917.0, y=92.0, width=115.0, height=53.0)
        #self.button_15.place(x=917.0, y=156.0, width=115.0, height=53.0)
        self.button_16.place(x=1043.0, y=156.0, width=115.0, height=53.0)
        self.button_17.place(x=1043.0, y=92.0, width=114.0, height=53.0)
        #self.button_18.place(x=485.0, y=227.0, width=117.0, height=22.0)
    def button_place_soccer(self):
        self.button_2_1.place(
            x=169.0,
            y=466.0,
            width=106.0,
            height=72.0
        )
        self.button_2_2.place(
            x=348.0,
            y=466.0,
            width=106.0,
            height=72.0
        )

        self.button_2_3.place(
            x=632.0,
            y=466.0,
            width=106.0,
            height=72.0
        )

        self.button_2_4.place(
            x=811.0,
            y=466.0,
            width=106.0,
            height=72.0
        )

        self.button_2_5.place(
            x=481.0,
            y=384.0,
            width=124.0,
            height=53.0
        )

        self.button_2_6.place(
            x=917.0,
            y=92.0,
            width=115.0,
            height=53.0
        )

        self.button_2_9.place(
            x=1043.0,
            y=92.0,
            width=114.0,
            height=53.0
        )

    def setup_layout(self):
        self.StartProgramCanvas.place(x=0, y=0)
        self.button_1_1.place(relx=0.5, rely=0.5, anchor='center')

        self.SoccerCanvas.place(x=0,y=0)
        self.button_place_soccer()
        self.BasketballCanvas.place(x=0, y=0)
        self.button_place_basketball()


        self.StartScreenCanvas.place(x=0, y=0)
        self.button_1_2.place(
            x=73.0,
            y=156.0,
            width=532.0,
            height=430.0
        )
        self.button_1_3.place(
            x=652.0,
            y=156.0,
            width=532.0,
            height=430.0
        )

    def update_score_basketball(self, widget_id, value):
        try:
            self.BasketballCanvas.itemconfigure(widget_id, text=str(value))
        except AttributeError:
            print(f"Warning: Widget {widget_id} not found. Score not updated.")
    def update_score_soccer(self, widget_id, value):
        try:
            self.SoccerCanvas.itemconfigure(widget_id, text=str(value))
        except AttributeError:
            print(f"Warning: Widget {widget_id} not found. Score not updated.")


    def reset_scores_basketball(self, widget_id1,widget_id2, value):
        self.value = value
        try:
            self.BasketballCanvas.itemconfigure(widget_id1, text=str(value))
            self.BasketballCanvas.itemconfigure(widget_id2, text=str(value))

        except AttributeError:
            print(f"Warning: Widget {widget_id1,widget_id2} not found. Score not updated.")
    def reset_scores_soccer(self, widget_id1,widget_id2, value):
        self.value = value
        try:
            self.SoccerCanvas.itemconfigure(widget_id1, text=str(value))
            self.SoccerCanvas.itemconfigure(widget_id2, text=str(value))

        except AttributeError:
            print(f"Warning: Widget {widget_id1,widget_id2} not found. Score not updated.")

    def create_soccer_screen_widget(self, SoccerCanvas):
        self.SoccerCanvas = SoccerCanvas
        self.score3, self.score4 = create_score_text(self.SoccerCanvas)

        self.SoccerCanvas.create_rectangle(
            233.0,
            209.0,
            374.0,
            253.0,
            fill="#F95454",
            outline="")
        self.SoccerCanvas.create_rectangle(
            712.0,
            206.0,
            853.0,
            250.0,
            fill="#0D92F4",
            outline="")

        self.SoccerCanvas.create_text(
            243.0,
            209.0,
            anchor="nw",
            text="Team 1",
            fill="#000000",
            font=("NeueHaasDisplay Bold", 36 * -1)
        )

        self.SoccerCanvas.create_text(
            722.0,
            206.0,
            anchor="nw",
            text="Team 2",
            fill="#000000",
            font=("NeueHaasDisplay Bold", 36 * -1)
        )
        button_abstraction_1_1 = ButtonAbstraction(self.SoccerCanvas, "modules/assets/frame0/a_button_7.png", "SCORE3",
                                                 "1")
        button_abstraction_1_2 = ButtonAbstraction(self.SoccerCanvas, "modules/assets/frame0/a_button_6.png", "SCORE3",
                                                 "-1")
        button_abstraction_1_3 = ButtonAbstraction(self.SoccerCanvas, "modules/assets/frame0/a_button_7.png", "SCORE4",
                                                 "1")
        button_abstraction_1_4 = ButtonAbstraction(self.SoccerCanvas, "modules/assets/frame0/a_button_8.png", "SCORE4",
                                                 "-1")
        button_abstraction_1_5 = ButtonAbstraction(self.SoccerCanvas, "modules/assets/frame0/a_button_5.png", "RESETSOCCER",
                                                 "2")
        button_abstraction_1_6 = ButtonAbstraction(self.SoccerCanvas, "modules/assets/frame0/a_button_4.png", "STARTTIMERSOCCER",
                                                 "3")

        button_abstraction_1_9 = ButtonAbstraction(self.SoccerCanvas, "modules/assets/frame0/a_button_1.png", "ENDSOCCER",
                                                 "-3")
        self.button_2_1 = button_abstraction_1_1.create_button()
        self.button_2_2 = button_abstraction_1_2.create_button()
        self.button_2_3 = button_abstraction_1_3.create_button()
        self.button_2_4 = button_abstraction_1_4.create_button()
        self.button_2_5 = button_abstraction_1_5.create_button()
        self.button_2_6 = button_abstraction_1_6.create_button()

        self.button_2_9 = button_abstraction_1_9.create_button()

    def create_start_screen_widgets(self, StartScreenCanvas):
        self.StartScreenCanvas = StartScreenCanvas

        self.StartScreenCanvas.create_text(
            330.0,
            27.0,
            anchor="nw",
            text="Choose Sport",
            fill="#1E1E1E",
            font=("NeueHaasDisplay Bold", 96 * -1)
        )

        button_abstraction_1_2 = ButtonAbstraction(self.StartScreenCanvas, "modules/assets/frame0/button_1_2.png",
                                                   "STARTBASKETBALL", "STARTBASKETBALL")
        self.button_1_2 = button_abstraction_1_2.create_button()
        button_abstraction_1_3 = ButtonAbstraction(self.StartScreenCanvas, "modules/assets/frame0/button_1_3.png",
                                                   "STARTSOCCER", "STARTSOCCER")
        self.button_1_3 = button_abstraction_1_3.create_button()
    def create_start_program_widgets(self, StartProgramCanvas):

        self.StartProgramCanvas = StartProgramCanvas
        button_abstraction_1_1 = ButtonAbstraction(self.StartProgramCanvas, "modules/assets/frame0/button_1_1.png",
                                                   "STARTPROGRAM", "1")
        self.button_1_1 = button_abstraction_1_1.create_button()



    def create_basketball_widgets(self, BasketballCanvas):
        self.BasketballCanvas = BasketballCanvas
        self.score1, self.score2 = create_score_text(self.BasketballCanvas)
        self.BasketballCanvas.create_rectangle(
            449.0,
            136.0,
            637.0,
            216.0,
            fill="#78B7D0",
            outline="")

        self.quarterNumber = self.BasketballCanvas.create_text(
            526.0,
            299.0,
            anchor="nw",
            text="1",
            fill="#000000",
            font=("NeueHaasDisplay Black", 64 * -1)
        )

        self.BasketballCanvas.create_text(
            477.0,
            264.0,
            anchor="nw",
            text="Quarter",
            fill="#000000",
            font=("NeueHaasDisplay Black", 36 * -1)
        )

        self.BasketballCanvas.create_rectangle(
            233.0,
            209.0,
            374.0,
            253.0,
            fill="#F95454",
            outline="")
        self.BasketballCanvas.create_rectangle(
            712.0,
            206.0,
            853.0,
            250.0,
            fill="#0D92F4",
            outline="")

        self.BasketballCanvas.create_text(
            243.0,
            209.0,
            anchor="nw",
            text="Team 1",
            fill="#000000",
            font=("NeueHaasDisplay Bold", 36 * -1)
        )

        self.BasketballCanvas.create_text(
            722.0,
            206.0,
            anchor="nw",
            text="Team 2",
            fill="#000000",
            font=("NeueHaasDisplay Bold", 36 * -1)
        )

        button_abstraction_1 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_1.png", "SCORE1",
                                                 "1")
        button_abstraction_2 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_2.png", "SCORE1",
                                                 "2")
        button_abstraction_3 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_3.png", "SCORE1",
                                                 "3")
        button_abstraction_4 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_4.png", "SCORE2",
                                                 "1")
        button_abstraction_5 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_5.png", "SCORE2",
                                                 "2")
        button_abstraction_6 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_6.png", "SCORE2",
                                                 "3")
        button_abstraction_7 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_7.png", "SCORE1",
                                                 "-1")
        button_abstraction_8 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_8.png", "SCORE1",
                                                 "-2")
        button_abstraction_9 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_9.png", "SCORE1",
                                                 "-3")
        button_abstraction_10 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_10.png",
                                                  "SCORE2", "-1")
        button_abstraction_11 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_11.png",
                                                  "SCORE2", "-2")
        button_abstraction_12 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_12.png",
                                                  "SCORE2", "-3")
        button_abstraction_13 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_13.png", "RESET",
                                                  "Game reset")
        button_abstraction_14 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_14.png",
                                                  "timerbasketball", "starttimerbasketball")
        button_abstraction_15 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_15.png",
                                                  "ENDGAME", "DESTROY")
        button_abstraction_16 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_16.png",
                                                  "ADDQUARTER", "1")
        button_abstraction_17 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_17.png",
                                                  "ENDGAME", "1")
        button_abstraction_18 = ButtonAbstraction(self.BasketballCanvas, "modules/assets/frame0/button_18.png",
                                                  "ENDGAME", "DESTROY")

        self.button_1 = button_abstraction_1.create_button()
        self.button_2 = button_abstraction_2.create_button()
        self.button_3 = button_abstraction_3.create_button()
        self.button_4 = button_abstraction_4.create_button()
        self.button_5 = button_abstraction_5.create_button()
        self.button_6 = button_abstraction_6.create_button()
        self.button_7 = button_abstraction_7.create_button()
        self.button_8 = button_abstraction_8.create_button()
        self.button_9 = button_abstraction_9.create_button()
        self.button_10 = button_abstraction_10.create_button()
        self.button_11 = button_abstraction_11.create_button()
        self.button_12 = button_abstraction_12.create_button()
        self.button_13 = button_abstraction_13.create_button()
        self.button_14 = button_abstraction_14.create_button()
        self.button_15 = button_abstraction_15.create_button()
        self.button_16 = button_abstraction_16.create_button()
        self.button_17 = button_abstraction_17.create_button()
        self.button_18 = button_abstraction_18.create_button()



if __name__ == "__main__":
    root = tk.Tk()
    WIDTH, HEIGHT = 1280, 720
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.title("Game Controller")

    view = View(root)
    view.setup()
    root.mainloop()