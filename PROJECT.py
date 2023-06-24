//Image Drawing System Using Turtle Library

import turtle
def circle_1():
	h = str(input("1.Animated \n2.Normal"))
	if h=="1":
		turtle.pencolor("red")
		turtle.circle(100)
	elif h=="2":
		a=int(input("Enter no of rows: "))
		f=int(input("Enter no of columns: "))
		sym = str(input("Enter the symbol you want to use to draw figure: "))
		for i in range(0,a,1):
			for j in range(0,f,1):
				if (((i == 0 or i == a - 1) and (j > 0 and j < f - 1))):
					print((sym), end='')
				elif ((j == 0 or j == f - 1) and (i != 0 and i != a - 1)):
					print((sym), end="")
				else:
					print(end=" ")
			print()

def square_2():
	h=str(input("1.Filled OR 2.Hollow?: OR 3.Animated:"))
	if h=="1":
		a=int(input("Enter number of rows and columns"))
		sym = str(input("Enter the symbol you want to use to draw figure: "))
		for i in range(0,a,1):
			print((sym+" ")*a)
	elif h=="2":
		a = int(input("Enter number of rows and columns:"))
		sym = str(input("Enter the symbol you want to use to draw figure: "))
		for i in range(0,a,1):
			for j in range(0,a,1):
				if (i==0 or i==a-1 or j==0 or j==a-1):
					print((sym+" "),end="")
				else:
					print(" ",end=" ")
			print()
	elif h=="3":
		for i in range(4):
			turtle.pencolor("blue")
			turtle.forward(300)  # Forward turtle by s units
			turtle.left(90)

def triangle_3():
	b=print("Which triangle you want to draw.\n1.Right angle Triangle\n2.Equilateral Triangle/Pyramid\n3.Reverse Pyramid")
	c=int(input("Press 1,2 or 3 to select triangle."))
	if c==1:
		h = str(input("1.Filled OR 2.Hollow?: OR Animated: "))
		if h=="1":
			n=10
			a=int(input("Enter Number Of Rows: "))
			sym = str(input("Enter the symbol you want to use to draw figure: "))
			for i in range(0,a+1,1):
				print(" "*n, end="")
				print((sym+" ") * i)
		elif h=="2":
			n = 10
			a = int(input("Enter Number Of Rows:"))
			sym = str(input("Enter the symbol you want to use to draw figure: "))
			for i in range(0,a):
				for j in range(0,a):
					if j==0 or i==a-1 or i==j :
						print((sym),end=" ")
					else:
						print(" ",end=" ")
				print()
		elif h=="3":
			turtle.pencolor("red")
			turtle.forward(175)
			turtle.left(150)
			turtle.pencolor("blue")
			turtle.forward(200)
			turtle.right(-120)
			turtle.pencolor("green")
			turtle.forward(120)
	elif c==2:
		h = str(input("1.Filled OR 2.Hollow?: OR Animated: "))
		if h == "1":
			n=10
			a=int(input("Enter Number Of Rows:"))
			sym = str(input("Enter the symbol you want to use to draw figure: "))
			for i in range(0,a+1,1):
				print(" "*n,end=" ")
				print((sym+" ") * i)
				n=n-1
		elif h=="2":
			n = 10
			a = int(input("Enter Number Of Rows:"))
			sym = str(input("Enter the symbol you want to use to draw figure: "))
			for i in range(0,a,1):
				print(" "*n,end="")
				for j in range(0, a,1):
					if j == 0 or i == a-1 or i == j:
						print((sym), end=" ")
					else:
						print(" ", end=" ")
				n=n-1
				print()
		elif h=="3":
			turtle.pencolor("blue")
			turtle.forward(300)
			turtle.left(120)
			turtle.pencolor("red")
			turtle.forward(300)
			turtle.left(120)
			turtle.pencolor("yellow")
			turtle.forward(300)
	elif c == 3:
		h = str(input("1.Filled OR 2.Hollow?: OR Animated: "))
		if h == "1":
			n=10
			a = int(input("Enter Number Of Rows:"))
			sym = str(input("Enter the symbol you want to use to draw figure: "))
			for i in range(a, 0, -1):
				print(" " * n, end=" ")
				print((sym+" ") * i)
				n = n + 1
		if h=="2":
			n = 10
			a = int(input("Enter Number Of Rows"))
			sym = str(input("Enter the symbol you want to use to draw figure: "))
			for i in range(0,a+1,1):
				print(" " * n, end="")
				for j in range(0,(a*2)+1,1):
					if (i==0 and j%2!=0) or i == j or i+j==a*2 :
						print((sym), end=" ")
					else:
						print(" ", end=" ")
				print()
		if h=="3":
			turtle.pencolor("red")
			turtle.forward(300)
			turtle.right(120)
			turtle.pencolor("green")
			turtle.forward(300)
			turtle.right(120)
			turtle.pencolor("blue")
			turtle.forward(300)

def rectangle_4():
	h = str(input("1.Filled OR 2.Hollow?: OR Animated: "))
	if h == "1":
		n=10
		l = int(input("Enter Number Of Rows: "))
		w= int(input("Enter Number Of Columns"))
		sym = str(input("Enter the symbol you want to use to draw figure: "))
		for i in range(l):
			print(" "*n,end=" ")
			print((sym+" ")*w)
	if h=="2":
		n=10
		l = int(input("Enter Number Of Rows: "))
		w = int(input("Enter Number Of Columns:"))
		sym = str(input("Enter the symbol you want to use to draw figure: "))
		for i in range(0,l):
			print(" "*n,end=" ")
			for j in range(0,w):
				if i==0 or i==l-1 or  j==0 or j==w-1:
					print((sym),end=" ")
				else:
					print(" ",end=" ")
			print()
	if h=="3":
		turtle.pencolor("red")
		turtle.forward(250)
		turtle.left(90)
		turtle.pencolor("yellow")
		turtle.forward(150)
		turtle.left(90)
		turtle.pencolor("green")
		turtle.forward(250)
		turtle.left(90)
		turtle.pencolor("blue")
		turtle.forward(150)

def diamond_5():
	h = str(input("1.Filled OR 2.Hollow?: OR Animated: "))
	if h == "1":
		n = 20
		a = int(input("Enter Number Of Rows"))
		sym = str(input("Enter the symbol you want to use to draw figure: "))
		for i in range(0, a + 1, 1):
			print(" " * n, end="")
			print((sym+" ") * i)
			n = n - 1
		for j in range(a - 1, 0, -1):
			print(" " * n, end="  ")
			print((sym+" ") * j)
			n = n + 1
	if h=="2":
		n = 10
		a = int(input("Enter Number Of Rows"))
		sym = str(input("Enter the symbol you want to use to draw figure: "))
		for i in range(1,a+1):
			print(" " * n, end="")
			for j in range(1, 2*a):
				if i+j ==a+1  or j-i == a-1:
					print((sym), end=" ")
				else:
					print(" ", end=" ")
			print()
		for i in range(1,a+1 ):
			print(" " * n, end="")
			for j in range(1, 2*a):
				if i == j or  i+j== a*2:
					print((sym), end=" ")
				else:
					print(" ", end=" ")
			print()
	if h=="3":
		turtle.pencolor("blue")
		turtle.left(115)
		turtle.forward(200)
		turtle.pencolor("green")
		turtle.right(-130)
		turtle.forward(200)
		turtle.pencolor("yellow")
		turtle.right(-50)
		turtle.forward(200)
		turtle.pencolor("red")
		turtle.left(130)
		turtle.forward(200)




q=1
while q>0:
	print("Hello User.\nHere is the list of Figures you can Draw:\n1.Circle\n2.Square\n3.Triangle\n4.Rectangle\n5.Diamond")
	inp=input(print("Enter Index Number Of Figure from the following:"))
	if inp=="1":
		circle_1()
	elif inp== "2":
		square_2()
	elif inp == "3":
		triangle_3()
	elif inp== "4":
		rectangle_4()
	elif inp== "5":
		diamond_5()
	elif inp=="0":
		break
q=q+1
