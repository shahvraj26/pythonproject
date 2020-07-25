def guess_count():
    print("Basic Python Code: let us average 3 numbers")
    

    x = int(input("Please enter your first number"))
        
    y = int(input("Please enter your second number"))
 
    z = int(input("Please enter your third number"))

    str = x+y+z
    print (float (str/3.0))

game = input("Do You want to Average 3 numbers, Type the password that allows you to go in")

correct = "password"

if game == correct:
    while True:
        guess_count()

if game != correct:
    print ("Sorry you are not allowed to enter the game, Try Again")  




