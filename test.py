from turtle import Turtle


amy = Turtle()

amy.shape("circle")
for i in range(50):
	amy.left(50)
	for i in range(4):
		amy.left(30)
		amy.forward(50)
	amy.penup()
	amy.forward(50)
	amy.pendown()
	for i in range(4):
		amy.left(25)
		amy.forward(50)

# amy.forward(80)
# amy.left(90)
# amy.forward(80)
# amy.left(90)
# amy.forward(80)

