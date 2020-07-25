import time
import random
def name():
    name = input("What is your name? ")

    print ("Hello, " + name, "Time to play BASIC hangman!")

    print ("")

    time.sleep(1)

    print ("Start guessing...")
    time.sleep(0.5)

    words = ("Hello", 'Earth', 'phone', 'keyboard', 'laptop')
    correct2 = random.choice(words)
    word = correct2

    guesses = ''

    turns = 10

    while turns > 0:         
        failed = 0             
        for char in word:      
            if char in guesses:    
                print ("correct"),    
            else:
                print ("_",)     
                failed += 1    

        if failed == 0:        
            print ("You won")  
            break              

        guess = input("guess a character:") 
        guesses += guess                    
        if guess not in word:  
            turns -= 1        
            print ("Wrong")    
            print ("You have", + turns, 'more guesses')
            if turns == 0:           
                print ("You Lost")


game = input("Do You want to play Hangman, Type the password that allows you to go in")

correct = "password"

if game == correct:
    while True:
        name()

if game != correct:
    print ("Sorry you are not allowed to enter the game")

time.sleep(5)

