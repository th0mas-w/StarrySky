import turtle, random
t = turtle.Turtle() # setup
turtle.Screen().bgcolor("black")
t.speed(1000) 
t.ht()
cords,cycle = [],0
t.color("White")
t.dot(7)

t.up() # Draw moon
t.goto(-300,200)
t.color('white')
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(-250,200)
t.color('black')
t.begin_fill()
t.circle(70)
t.end_fill()

while True: # Main loop
    cycle += 1
    print(cycle) # Cycle count
    xCord,yCord = random.randint(-300,300),random.randint(-300,300)
    cords.append([xCord,yCord])
    t.color("white") # Draw star
    t.up()
    t.setpos(xCord,yCord)
    t.down()
    t.dot(5)
    if random.randint(0,100) == 100: # Draw pan constellation
        print("Drawing pan")
        x,y=-350,-50
        coordinates=((x,y),(x+135,y+1),(x+220,y-50),(x+330,y-105),(x+344,y-188), (x+470,y-209), (x+500,y-123))
        for x in coordinates:
            t.up()
            t.setpos(x)
            cords.append(x)
            t.dot(6)
            t.down()
    if random.randint(1,4) == 1 and len(cords) > 3: # Clear stars
        amount = 7
        if len(cords) < 7:
            amount = len(cords)
        for x in range(random.randint(1,amount)):
            print("clense",len(cords)) # How many stars currently on screen
            t.color("black")
            t.up()
            t.setpos(cords[0][0],cords[0][1])
            t.down()
            t.dot(6)   
            cords.pop(0)