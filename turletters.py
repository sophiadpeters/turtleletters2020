import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
	    pass
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":
	    pass		
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	    pass
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":
	tur.penup()
	tur.forward(10)
	tur.right(90)	
	tur.forward(25)
	tur.pendown()
	tur.circle(10, 490)
	tur.right(70)
	tur.forward(5)
	tur.right(180)
	tur.forward(15)
	#letter completed and returned to position
	tur.penup()
	tur.right(60)
	tur.forward(28)
	tur.right(90)
	tur.forward(22)
    elif letter == "R":
	tur.penup()
	tur.forward(13)
	tur.right(90)
	tur.forward(10)
	tur.pendown()
	tur.forward(40)
	tur.right(180)
	tur.forward(20)
	tur.right(90)
	tur.circle(10,180)
	tur.left(90)
	tur.forward(20)
	tur.left(45)
	tur.forward(30)
	#letter completed and returned to position
	tur.penup()
	tur.left(45)
	tur.forward(6)
	tur.left(90)
	tur.forward(51)
	tur.right(90)
    elif letter == "S":
	    pass
    elif letter == "T":
	tur.penup()
	tur.forward(13)
	tur.right(90)
	tur.forward(15)
	tur.left(90)
	tur.pendown()
	tur.forward(14)
	tur.right(180)
	tur.forward(7)
	tur.left(90)
	tur.forward(30)
	#letter completed and returned to position
	tur.penup()
	tur.left(90)
	tur.forward(20)
	tur.left(90)
	tur.forward(45)
	tur.right(90)
    elif letter == "U":
	tur.penup()
	tur.forward(10)
	tur.right(90)
	tur.forward(10)
	tur.pendown()
	tur.forward(20)
	tur.circle(10,180)
	tur.forward(21)
	#letter completed and returned to position
	tur.penup()
	tur.forward(9)
	tur.right(90)
	tur.forward(10)
    elif letter == "V":
	    pass
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(40)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(1)
    #turtleLetter("box",tur)
    turtleLetter("A",tur)


    window.exitonclick()
