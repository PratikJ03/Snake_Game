from turtle import Turtle
STARTING_POSITIONS =[(0,0),(-20,0),(-30,0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.crete_snake()
        self.head=self.segments[0]

    def crete_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        snake = Turtle()
        snake.up()
        snake.shape("square")
        snake.color("white")
        self.segments.append(snake)
        snake.goto(position)

    def extend(self):
        #grow the snake
        self.add_segment(self.segments[-1].position())


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

