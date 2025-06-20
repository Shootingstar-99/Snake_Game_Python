from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.color('white')
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.refresh()

    def game_start(self):
        self.goto(0,0)
        self.write('''Welcome: Press space to start!''', align=ALIGNMENT, font=FONT)
        self.goto(0,260)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", "w") as file:
                file.write(str(self.current_score))
        self.current_score = 0
        self.refresh()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER! Click to exit!", align= ALIGNMENT, font= FONT)
        self.goto(0,-20)
        self.write("Press enter to replay!", align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"SCORE: {self.current_score} HIGH SCORE: {self.high_score}", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.current_score += 1
        self.refresh()