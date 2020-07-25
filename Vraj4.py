import time
hp = 30 


def name():
    name = input("What is your name")
    print ("Thank You for playing", name, "I hope you enjoy")

    print("You have too pick from four rooms Which one do you pick 1, 2, 3 or 4")
    door = input("> ")

    if door == "1":
        print("You have entered a door with a lion in it")
        print("What number do you want to choose")
        print("#1. get connected with the lion")
        print("#2. get a rock")

        lion = input('> ')

        if lion == "1":
            print("And so we are all connected in the great circle of life, you have died")


        elif lion == "2":
            print("You get a rock and beat the lion until he dies, Well done you have survived")

        else:
            print("You have died")

    elif door == "2":
        print("You pull out a mechanical pencil, Ms.Harris walks to you slowly in class")
        print("What would you do")
        print("#1 run away")
        print("#2 chuck lead in her face")

        Harris = input("> ")
        

        if Harris == "1":
            print("Ms. Harris chases after you and never chatches you because she gets dizzy and falls and no one comes after her to save her, so you win")

        elif Harris == "2":
            print("She can't see, but you get expelled from school and she is happy forever")
        
    else:
        print("You are in big trouble")


    if door == "3":
        print("You have entered a door with a phone in it")
        print("What would you do")
        print("#1 steal phone")
        print("#2 play games but you don't steal it")

        Phone = input("> ")

        if Phone == "1":
            print("the phone blows up so you die when you try to steal it")

        elif Phone == "2":
            print("you have 2 minutes to play games and if you don't finish in two minutes a ninja will come and kill you")

        else:
            print("You did not pick a number so you will be blowed up by the cave")

    elif door == "4":
        print("You have entered a room with a lawn mover in it")
        print("what would you do")
        print("#1 run away")
        print("#2 cut the grass")

        lawnmover = input(">")

        if lawnmover == "1":
            print("you have succesfully came out but one day the lawn mover will come and cut you")

        elif lawnmover == "2":
            print("There is no grass in the room so the lawn mover malfunctions and cuts you up")

    else:
        print("You have picked the wrong door you will not work with us anymore you are fired")


game = input("Do You want to play Choose your own adventure book, Type the password that allows you to go in")

correct = "password"

if game == correct:
    while True:
        name()

if game != correct:
    print ("Sorry you are not allowed to enter the game")






time.sleep(5)
