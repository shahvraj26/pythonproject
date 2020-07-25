import time

def answer():
    import random
    learn = random.randint(1,100)
    while True:
        learn2 = int(input("Guess the number 1-100"))

        if learn2 > learn:
            print('Number is too high')
        elif learn2 < learn:
            print('Number is too low')

        else:
            print('you won a million dollars')

            time.sleep(3)
       
game = input("Do You want to play Guess the number game, Type the password that allows you to go in")

correct = "password"

if game == correct:
    while True:
        answer()

if game != correct:
    print ("Sorry you are not allowed to enter the game")
        

    
              
