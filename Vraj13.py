intermission = True

def convert():
    convert = input ("Please input what operation you wish to perform. 1 for Fahrenheit to Celsius, 2 for Meters to Centimetres, 3 for Megabytes to Gigabytes, 4 for Feet to Yards, 5 for Miles to Feet")

    if convert == "1":
        f1 = input ("Please enter your fahrenheit temperature: ")
        f1 = int(f1)

        a1 = (f1 - 32) / 1.8
        a1 = str(a1)

        print (a1+" Celsius") 

    if convert == "2":
        m1 = input ("Please enter your meters")
        m1 = int(m1)
        m2 = (m1 * 100)
    
        m2 = str(m2)
        print (m2+" C")


    if convert == "3":
        mb1 = input ("Please enter your megabytes")
        mb1 = int(mb1)
        mb2 = (mb1 / 1024)

        mb3 = str(mb2)

        print (mb3+" GB")

    if convert == "4":
        feet = input ("Please enter your feet")
        feet = int(feet)
        yards = (feet * 3)
        yards = str(yards)

        print (yards+" yards")

    if convert == "5":
        mile = input("Please enter your mile")
        mile1 = int(mile)
        feet1 = (mile1 * 5280)
        feet3 = str(feet1)

        print (feet3+" feet")


game = input("Do You want to convert, Type the password that allows you to go in")

correct = "password"

if game == correct:
    while intermission:
        convert()

if game != correct:
    print ("Sorry you are not allowed to enter the top secret toolkit, Try Again")


