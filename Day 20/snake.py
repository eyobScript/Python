from turtle import Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            segment = Turtle('square')
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)


    def up(self):
        self.head.heading() != DOWN and self.head.setheading(UP)
    def down(self):
        self.head.heading() != UP and self.head.setheading(DOWN)
    def left(self):
        self.head.heading() != RIGHT and self.head.setheading(LEFT)
    def right(self):
        self.head.heading() != LEFT and self.head.setheading(RIGHT)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
