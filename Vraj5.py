import time

numbers=input("How many numbers do you want to calculate")
grade_list = []

def evalute():
    for i in range (numbers):
        grades=float(input("Pick a number between 1-10000"))
        while grades < 0 or grades > 10000:
            print("the number" +  str(grades)  + "is not in range")
            grades=float(input("Please enter the amount of numbers you want to average"))
        grade_list.append(grades)
    average = sum(grade_list)/numbers
    if (average >= 2500):
        print(str(average))
    if (average <= 2500):
        print(str(average))

    time.sleep(3)

try:
    numbers=int(numbers)
    evalute()
except:
    while True:
        try:
            numbers=int(numbers)
            evalute()
            break
        except:
            print("Sorry" +  str(numbers)  + "is not a number,Try Again")
            numbers=input("How many numbers do you want to calculate")

#Credits to stackoverflow.com for teaching me and i tweaked some things         


