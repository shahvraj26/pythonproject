import webbrowser
import time

def website1():
    website1 = "Amazon"
    website2 = "EdHelper"
    website3 = "Wings"
    website4 = "Schoology"
    website5 = "Coolmath"
    website6 = "Pbs Kids"
    website7 = "Vonage"
    website8 = "Walgreens|Employees Home"
    website9 = "Yahoo"
    website10 = "Youtube"
    website11 = "Best Buy Deals"
    website12 = "Fidelity Bank"
    website13 = "Google"
    website14 = "Stock Markets"
    website15 = "Wix"
    website16 = "Vraj Website | Portfolio"
    website17 = "Dayton Regional Stem School"
    website18 = "Dayton Raiders"
    website19 = "Gmail"
    website20 = "Python"

    time.sleep(2)
    
    print ("=======================")
    print (website1)
    print ("-----------------------")
    print (website2)
    print ("-----------------------")
    print (website3)
    print ("-----------------------")
    print (website4)
    print ("-----------------------")
    print (website5)
    print ("-----------------------")
    print (website6)
    print ("-----------------------")
    print (website7)
    print ("-----------------------")
    print (website8)
    print ("-----------------------")
    print (website9)
    print ("-----------------------")
    print (website10)
    print ("-----------------------")
    print (website11)
    print ("-----------------------")
    print (website12)
    print ("-----------------------")
    print (website13)
    print ("-----------------------")
    print (website14)
    print ("-----------------------")
    print (website15)
    print ("-----------------------")
    print (website16)
    print ("-----------------------")
    print (website17)
    print ("-----------------------")
    print (website18)
    print ("-----------------------")
    print (website19)
    print ("-----------------------")
    print (website20)
    print ("=======================")
    


    print("*Note* In Python you will have to type in exactly the same words, you can just copy and paste the website that you want to play below...")

    time.sleep(2)
    
    website = input("What website do you want to go to from above:")

    

    if website1 == website:
        time.sleep(2)
        webbrowser.open("https://smile.amazon.com/")
        print("I hope you had fun going to amazon using my code, Thank You")

    elif website2 == website:
        time.sleep(2)
        webbrowser.open("https://www.edhelper.com/")
        print("I hope you had fun going to EdHelper using my code, Thank You")

    elif website3 == website:
        time.sleep(2)
        webbrowser.open("https://wings.wright.edu/")
        print("I hope you had fun going to Wings using my code, Thank You")

    elif website4 == website:
        time.sleep(2)
        webbrowser.open("https://drss.schoology.com/")
        print("I hope you had fun going to Schoology using my code, Thank You")

    elif website5 == website:
        time.sleep(2)
        webbrowser.open("http://www.coolmath.com/")
        print("I hope you had fun going to Coolmath using my code, Thank You")

    elif website6 == website:
        time.sleep(2)
        webbrowser.open("http://pbskids.org/")
        print("I hope you had fun going to Pbs Kids using my code, Thank You")

    elif website7 == website:
        time.sleep(2)
        webbrowser.open("https://www.vonage.com/personal/customer")
        print("I hope you had fun going to Vonage using my code, Thank You")

    elif website8 == website:
        time.sleep(2)
        webbrowser.open("")
        print("I hope you had fun going to Walgreens|Employees Home using my code, Thank You")

    elif website9 == website:
        time.sleep(2)
        webbrowser.open("https://webapp2.walgreens.com/Walnet2/servlet/walgreens.portalframework.runtime.servletproxy.PortalFrameworkServletProxy/GatewayRH")
        print("I hope you had fun going to Yahoo using my code, Thank You")

    elif website10 == website:
        time.sleep(2)
        webbrowser.open("https://www.youtube.com/")
        print("I hope you had fun going to Youtube using my code, Thank You")

    elif website11 == website:
        time.sleep(2)
        webbrowser.open("https://deals.bestbuy.com/?category=featured+deals")
        print("I hope you had fun going to Best Buy Deals using my code, Thank You")

    elif website12 == website:
        time.sleep(2)
        webbrowser.open("https://www.fidelity.com/")
        print("I hope you had fun going to Fidelity Bank using my code, Thank You")

    elif website13 == website:
        time.sleep(2)
        webbrowser.open("https://www.google.com/")
        print("I hope you had fun going to Google using my code, Thank You")

    elif website14 == website:
        time.sleep(2)
        webbrowser.open("https://www.cnbc.com/")
        print("I hope you had fun going to Stock Markets using my code, Thank You")

    elif website15 == website:
        time.sleep(2)
        webbrowser.open("https://www.wix.com/")
        print("I hope you had fun going to Wix using my code, Thank You")

    elif website16 == website:
        time.sleep(2)
        webbrowser.open("http://vraj2003.wixsite.com/portfolio")
        print("I hope you had fun going to Vraj Website | Portfolio using my code, Thank You")
    
    elif website17 == website:
        time.sleep(2)
        webbrowser.open("http://www.daytonstemschool.org/")
        print("I hope you had fun going to Dayton Stem School using my code, Thank You")

    elif website18 == website:
        time.sleep(2)
        webbrowser.open("https://www.teamunify.com/Home.jsp?team=czosdrsc")
        print("I hope you had fun going to Dayton Raiders using my code, Thank You")

    elif website19 == website:
        time.sleep(2)
        webbrowser.open("https://www.google.com/gmail/")
        print("I hope you had fun going to Gmail using my code, Thank You")

    elif website20 == website:
        time.sleep(2)
        webbrowser.open("https://www.python.org/")
        print("I hope you had fun going to Python using my code, Thank You")



game = input("Do You want to find websites, Type the password that allows you to go in")

correct = "password"

if game == correct:
    while True:
        website1()

if game != correct:
    print ("Sorry you are not allowed to enter the game, Try Again") 
