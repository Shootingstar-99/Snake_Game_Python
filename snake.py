from turtle import Turtle
STARTING_POSITIONS = [(10,0), (-20,0), (-40,0), (-60,0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape('classic')
        self.head.color('red')
        self.head.shapesize(stretch_len= 3, stretch_wid= 2)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('circle')
        new_segment.shapesize(stretch_wid=1.3, stretch_len= 1.3)
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.head.forward(MOVE_DISTANCE)

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