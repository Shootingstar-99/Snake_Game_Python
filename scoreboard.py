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
        self.refresh()

    def game_start(self):
        self.goto(0,0)
        self.write('''Welcome: Press space to start!''', align=ALIGNMENT, font=FONT)
        self.goto(0,260)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER! Click to exit!", align= ALIGNMENT, font= FONT)

    def refresh(self):
        self.clear()
        self.write(f"SCORE: {self.current_score}", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.current_score += 1
        self.refresh()