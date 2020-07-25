import random
learn = random.randint(1,100)
while True:
    learn2 = int(input("Guess the number 1-100"))

    if learn2 > learn:
        print('Number is too high')
    elif learn2 < learn:
        print('Number is too low')

    else:
        print('you won')
