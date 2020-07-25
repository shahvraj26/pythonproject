#There is no game
import time
import sys

def game1():
    print("There is no game")
    time.sleep(1)
    print("Please go")
    time.sleep(1)
    print("Please go there is no game")
    time.sleep(2)

    game =input("Please, Please, Please go THERE is no game")

    game1 = "there"

    if game == game1:
        print("Uh, Uh, Uh you found a game")
        time.sleep(1)
        print("No, No, No there is no game this is just asking for your information")
        name = input("What is your name")
        age = input("What is your age")
        print("I told you", name, "It is just information now please go there is no", age, "year old allowed in here, Please go, There is no game")

    friend = input("Oh no the glitches Please go, Please just WIN")

    friend1 = "win"

    if friend == friend1:
        print("Uh please just go you are disturbing me and breaking my stuff")
        time.sleep(1)
        print("Uh you really like to break stuff now here you go")
        time.sleep(3)
        print("Your now gonna have to start over my friend")
        time.sleep(4)

    awesome = input("Are you my friend, (yes/no)")

    awesome1 = "yes"

    awesome2 = "no"

    if awesome == awesome1:
        print("Great, now we are friends so get out of here")
        time.sleep(1)
        print("Now to be clear, THERE IS NO GAME")
        sys.exit()
        
    if awesome == awesome2:
        print("Shut up, and you will pay for this my friend")
        time.sleep(1)
        print("I will make you start over this game,")
        time.sleep(2)
        print("Wait I meant no game, Yeah I totally meant that, uh wahtever just get out")
        sys.exit()
    
game = input("Do You want to play There is no game, Type the password that allows you to go in")

correct = "password"

if game == correct:
    while True:
        game1()

if game != correct:
    print ("Sorry you are not allowed to enter the game")
        




