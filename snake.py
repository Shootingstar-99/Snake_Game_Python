from turtle import Turtle
STARTING_POSITIONS = [(10,0), (-20,0), (-40,0), (-60,0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.edit_head()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def edit_head(self):
        head = self.segments[0]
        head.shape('classic')
        head.color('red')
        head.shapesize(stretch_len=3, stretch_wid=2)
        return head

    def add_segment(self, position):
        new_segment = Turtle('circle')
        new_segment.shapesize(stretch_wid=1.3, stretch_len= 1.3)
        new_segment.color('lime')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.edit_head()

    def extend_snake(self):
        position_x = self.segments[-1].xcor()
        position_y = self.segments[-1].ycor()
        position = (position_x, position_y)
        self.add_segment(position)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)