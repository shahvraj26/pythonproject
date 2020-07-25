import random
import time

rock = "rock"
paper = "paper"
scissors = "scissors"

print("rock")
time.sleep(1)
print("paper")
time.sleep(1)
print("scissors")
time.sleep(1)
print("shoot")
time.sleep(1)

print("WELCOME TO ROCK, PAPER, SCISSORS; NEXT line tells you what you would like to play; The computer will respond with its play and say if YOU won, lost, or tied.")
time.sleep(2)
guess = input("Please tell us what you would like to play: rock, paper, or scissors")
learn = ["rock", "paper", "scissors"]

if guess == rock:
    computer = random.choice(learn)

    if computer == rock:
        print(computer)
        time.sleep(1)
        print("Its a Freaking Tie: *RUN PROGRAM AGAIN*")
        time.sleep(1)
        exit()

    if computer == paper:
        print(computer)
        time.sleep(1)
        print("You Lose HaHaHa")
        time.sleep(1)
        exit()

    if computer == scissors:
        print(computer)
        time.sleep(1)
        print("You Win Good Job UwU")
        time.sleep(1)
        exit()

if guess == paper:
    computer2 = random.choice(learn)

    if computer2 == rock:
        print(computer2)
        time.sleep(1)
        print("You Are The Winner!!!!! :)")
        time.sleep(1)
        exit()

    if computer2 == paper:
        print(computer2)
        time.sleep(1)
        print("Tie, Darn it; Next Time I will win HAHAHAHA :) ;)")
        time.sleep(1)
        exit()

    if computer2 == scissors:
        print(computer2)
        time.sleep(1)
        print("You Lose *asdfaweafsdf* SCRUB, Try Again")
        time.sleep(1)
        exit()

if guess == scissors:
    computer3 = random.choice(learn)

    if computer3 == rock:
        print(computer3)
        time.sleep(1)
        print("You Are A LOSER,")
        time.sleep(1)
        print("You Are A LOSEr,")
        time.sleep(1)
        print("You Are A LOSer,")
        time.sleep(1)
        print("You Are A LOser,")
        time.sleep(1)
        print("You Are A Loser,")
        time.sleep(1)
        print("You Are A loser,")
        time.sleep(1)
        exit()

    if computer3 == paper:
        print(computer3)
        time.sleep(1)
        print("YOU are the WINNER, PLZ Call 1-800-543-1234 FOR Your MiLlIoN DolLaRS nOW...")
        time.sleep(1)
        exit()

    if computer3 == scissors:
        print(computer3)
        time.sleep(1)
        print("IT'S a TIE, CyA NeXt TimE...")
        time.sleep(1)
        exit()
