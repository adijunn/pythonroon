# author: adijunn
import turtle

sides = 6
#count = 0;
length = 60
angle = 180 - 180*(sides - 2) / sides
numbers = range(0, sides)
adi = turtle.Turtle()

#while count < 10: 

	#adi.forward(length)
	#adi.left(36)
	#count = count + 1
	
	
for number in numbers: 
	
	adi.forward(length)
	adi.left(angle)
	