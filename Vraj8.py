import random
import time
def guess_count():
     guess_count=0
     
     while True:
          print('You have five passwords to choose from, said down below:')
          print('Vraj')
          print('Rubix')
          print('easy')
          print('definition')
          print('Earth')
          time.sleep(1)

          pass_guess = str(input("Get in the bank, and figure out the password"))

          guess_count += 1

          WORD = ('Vraj', 'Rubix', 'easy', 'definition', 'Earth') 
          WORDS= random.choice(WORD)
          correct_pass = WORDS
          
          if pass_guess == correct_pass:
              print("You are correct")

          elif pass_guess != correct_pass:
               if guess_count >= 3:
                    print("Sorry, you are incorrect")

          time.sleep(1)
          
game = input("Do You want to Guess the password, Type the password that allows you to go in")

correct = "password"

if game == correct:
    while True:
        guess_count()

if game != correct:
    print ("Sorry you are not allowed to enter the game, Try Again")               
