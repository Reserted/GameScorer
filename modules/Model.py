class Actions:
    def __init__(self):
        self.number1 = 0
        self.number2 = 0
        self.number3 = 0
        self.number4 = 0
        self.num = 0
        self.time_left = 1800  # 30 minutes in seconds
        self.update_timer = None
        self.quarter = 1

    def clicked_1(self, increment_amount: int) -> int:
        self.number1 += increment_amount
        return self.number1

    def clicked_2(self, num):
        self.number2 += num
        return self.number2

    def soccerClicked_1(self,num):
        self.number3 += num
        return self.number3

    def quarterClicked(self,num):
        if self.quarter < 4:
            self.quarter += num
        return self.quarter
    def soccerClicked_2(self,num):
        self.number4 += num
        return self.number4

    def get_winner_basketball(self):
        if self.number1 > self.number2:
            return "Team 1 wins"
        elif self.number2 > self.number1:
            return "Team 2 2 wins"
        else:
            return "It's a draw, we go overtime"
    def get_winner_soccer(self):
        if self.number3 > self.number4:
            return "Team 3 wins"
        elif self.number4 > self.number3:
            return "Team 4 wins"
        else:
            return "It's a draw, we go overtime"
    def countdown(self):
        if self.time_left > 0:
            return self.time_left - 1
        else:
            return None


if __name__ == "__main__":
    app = Actions()
    print(app.clicked_2(9))