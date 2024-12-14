import tkinter as tk
from modules.Model import Actions
from modules.View import View
from pubsub import pub


class ActionsController:
    def __init__(self, parent):
        self.parent = parent
        self.model = Actions()
        self.view = View(parent)
        self.view.setup()
        self.update_timer = None

        try:
            var = [pub.subscribe(self.handle_score_update_1, "SCORE1"),
                   pub.subscribe(self.handle_score_update_2, "SCORE2"),
                   pub.subscribe(self.handle_reset_score_basketball, "RESET"),
                   pub.subscribe(self.handle_reset_score_soccer, "RESETSOCCER"),
                   pub.subscribe(self.handle_endgame_canvas, "ENDGAME"),
                   pub.subscribe(self.handle_startgame_canvas, "STARTBASKETBALL"),
                   pub.subscribe(self.handle_startgame_canvas, "STARTSOCCER"),
                   pub.subscribe(self.handle_soccer_canvas, "ENDSOCCER"),
                   pub.subscribe(self.handle_score_update_3,"SCORE3"),
                   pub.subscribe(self.handle_score_update_4,"SCORE4"),
                   pub.subscribe(self.handle_start_program,"STARTPROGRAM"),
                   pub.subscribe(self.handle_quarter_time, "ADDQUARTER")]

            print("Successfully subscribed to SCORE1 topic.")
            print("Successfully subscribed to SCORE2 topic.")
            print("Successfully subscribed to RESET topic.")
        except Exception as e:
            print(f"Error subscribing to SCORE1: {e}")

    def handle_quarter_time(self, message):
        self.view.BasketballCanvas.itemconfigure(self.view.quarterNumber, text=str(self.model.quarterClicked(eval(message))))

    def handle_start_program(self,message):
        self.view.StartProgramCanvas.place_forget()
        self.view.switch_canvas("StartScreenCanvas")

    def handle_soccer_canvas(self,message):
        print(self.model.get_winner_soccer())
        self.view.SoccerCanvas.place_forget()
        self.handle_reset_score_soccer("tried")
        self.view.switch_canvas("StartScreenCanvas")

    def handle_endgame_canvas(self,message):
        print(message)
        print(self.model.get_winner_basketball())
        self.handle_reset_score_basketball("tried")
        self.model.quarter = 1
        self.view.BasketballCanvas.itemconfigure(self.view.quarterNumber,
                                                 text=str(self.model.quarter))
        self.view.BasketballCanvas.place_forget()
        self.view.switch_canvas("StartScreenCanvas")


    def handle_startgame_canvas(self, message):
        print(message)
        self.view.StartScreenCanvas.place_forget()
        if message == "STARTBASKETBALL":self.view.switch_canvas("BasketballCanvas")
        if message == "STARTSOCCER": self.view.switch_canvas("SoccerCanvas")


    def handle_score_update_1(self, message):
        try:
            # Parse the incoming message (assuming it's a JSON string)
            parsed_message = self.model.clicked_1(eval(message))  # Note: Use json.loads() instead of eval() in production
            self.model.number1 = parsed_message

            if self.model.number1 is not None:
                # Update the view with the new score
                self.view.update_score_basketball(self.view.score1, self.model.number1)
                print(f"Updated score1: {self.model.number1}")
            else:
                print("Invalid message format. No 'score' field found.")
        except Exception as e:
            print(f"Error processing message: {e}")
    def handle_score_update_2(self, message):
        try:
            # Parse the incoming message (assuming it's a JSON string)
            parsed_message = self.model.clicked_2(eval(message))  # Note: Use json.loads() instead of eval() in production
            self.model.number2 = parsed_message

            if self.model.number2 is not None:
                # Update the view with the new score
                self.view.update_score_basketball(self.view.score2, self.model.number2)
                print(f"Updated score2: {self.model.number2}")
            else:
                print("Invalid message format. No 'score' field found.")
        except Exception as e:
            print(f"Error processing message: {e}")
    def handle_score_update_3(self, message):
        try:
            # Parse the incoming message (assuming it's a JSON string)
            parsed_message = self.model.soccerClicked_1(eval(message))  # Note: Use json.loads() instead of eval() in production
            self.model.number3 = parsed_message

            if self.model.number3 is not None:
                # Update the view with the new score
                self.view.update_score_soccer(self.view.score3, self.model.number3)
                print(f"Updated score3: {self.model.number3}")
            else:
                print("Invalid message format. No 'score' field found.")
        except Exception as e:
            print(f"Error processing message: {e}")
    def handle_score_update_4(self, message):
        try:
            # Parse the incoming message (assuming it's a JSON string)
            parsed_message = self.model.soccerClicked_2(eval(message))  # Note: Use json.loads() instead of eval() in production
            self.model.number4 = parsed_message

            if self.model.number3 is not None:
                # Update the view with the new score
                self.view.update_score_soccer(self.view.score4, self.model.number4)
                print(f"Updated score4: {self.model.number4}")
            else:
                print("Invalid message format. No 'score' field found.")
        except Exception as e:
            print(f"Error processing message: {e}")

    def handle_reset_score_basketball(self,message):
        print(message)
        self.model.number1 = 0
        self.model.number2 = 0
        try:
            self.view.reset_scores_basketball(self.view.score1, self.view.score2, self.model.number2)

        except AttributeError as e:
            print(f"Error resetting scores: {e}")
            print("Make sure score1 and score2 are properly initialized in the View class.")
    def handle_reset_score_soccer(self,message):
        print(message)
        self.model.number3 = 0
        self.model.number4 = 0
        try:
            self.view.reset_scores_soccer(self.view.score3, self.view.score4, self.model.number3)

        except AttributeError as e:
            print(f"Error resetting scores: {e}")
            print("Make sure score1 and score2 are properly initialized in the View class.")





if __name__ == "__main__":
    root = tk.Tk()
    WIDTH, HEIGHT = 1280, 720
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.title("Open CV")

    app = ActionsController(root)
    root.mainloop()
