import turtle
import time

turtle.colormode(255)

t = turtle.Turtle()
t.speed(1)

class SpheroMock():
	def __init__(self):
		return

	def set_rgb_led(self, r, g, b):
		t.pencolor((r, g, b))

	def move(self, direction):
		t.setheading(direction)
		t.forward(50)

	def wait(self, s):
		time.sleep(s)

	def done(self):
		turtle.done()

def connect():
	return SpheroMock()
