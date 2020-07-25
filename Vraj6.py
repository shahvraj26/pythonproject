
def name():
    name=input("what is your name")
    print("hi" +  str(name))


    age=int(input("what is your age"))
    print(age)
    learn=input("is this the right age")

    if learn == 'yes':
        print(str("Ok"))
    
    else:
        age=int(input('What is your real age'))
        print("Thank You")


game = input("Do You want to play What's your name, Type the password that allows you to go in")

correct = "password"

if game == correct:
    while True:
        name()

if game != correct:
    print ("Sorry you are not allowed to enter the game")
        


