from turtle import Turtle


class Line:
    def __init__(self):
        self.line_seg = []
        self.create_line()

    def create_line(self):
        for y in range(300, -350, -50):
            self.add_segment(y)


    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.shapesize(stretch_len=0.2, stretch_wid=1)
        new_segment.penup()
        new_segment.goto(0, position)
        self.line_seg.append(new_segment)



