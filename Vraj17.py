import datetime
import time

def ti():
    t = datetime.datetime.now()
    d = time.strftime("%x")
    i = time.strftime("%X")
    m = time.strftime("%B")
    l = time.strftime("%A")
    k = time.strftime("%c")
    z = time.strftime("%Z")

    print("Current date and time = " + k)

    CY = "Current Year"
    CM = "Current Month"
    CD = "Current Day"
    WN = "Weekday Name"
    CDD = "Current Date"
    CH = "Current Hour"
    CMM = "Current Minute"
    CS = "Current Second"
    CT = "Current Time"
    TZN = "Time Zone Name"

    print ("========================")
    print (CY)
    print ("------------------------")
    print (CM)
    print ("------------------------")
    print (CD)
    print ("------------------------")
    print (WN)
    print ("------------------------")
    print (CDD)
    print ("------------------------")
    print (CH)
    print ("------------------------")
    print (CMM)
    print ("------------------------")
    print (CS)
    print ("------------------------")
    print (CT)
    print ("------------------------")
    print (TZN)
    print ("========================")


    print("*Note* In Python you will have to type in exactly the same words, you can just copy and paste the above details that you want to play below...")

    s = input("Pick what you want to see in detail from above...")

    if s == CY:
        print ("Current Year = %s " %t.year)

    elif s == CM:
        print ("Current Month = " + m)

    if s == CD:
        print ("Current Day = %s " %t.day)

    elif s == WN:
        print ("Weekday Name = " + l)

    if s == CDD:
        print ("Current Date = " + d)

    elif s == CH:
        print ("Current Hour (Military Time)= %s " %t.hour)

    if s == CMM:
        print ("Current Minute = %s " %t.minute)

    elif s == CS:    
        print ("Current Second = %s " %t.second)

    if s == CT:
        print ("Current Time = " + i)

    if s == TZN:
        print ("Time Zone Name = " +z)

    time.sleep(5)

game = input("Do You want to Find the detail Time, Type the password that allows you to go in")

correct = "password"

if game == correct:
    while True:
        ti()

if game != correct:
    print ("Sorry you are not allowed to enter the compilation")
        
time.sleep(5)




