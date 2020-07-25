import time

def guess_count():
     print("Welcome to the Language Arts Grammer Quiz, One Sentence")
     print("------------------------------------------------------------------------------------------------------------")
     print("Directions-Read the sentence given and then figure out what part of speech is each word.")
     print("------------------------------------------------------------------------------------------------------------")
     print("Sentence-A small snail climbed over the slippery log and inched slowly toward the nearby fields.")
     print("------------------------------------------------------------------------------------------------------------")
     print("Part of speeches to use-Noun, Determiner, Adjective, Verb, Adverb, Conjuction, and Preposition ::Write down your answer the same way up here::")
     print("------------------------------------------------------------------------------------------------------------------------------------------------------")

     guess_count=0

     correct_pass= 'Determiner'

     while True:
          pass_guess = str(input("A="))

          guess_count += 1

          if pass_guess == correct_pass:
              print("You are correct")
              break

          elif pass_guess != correct_pass:
                    print("Sorry, the real answer is Determiner")
                    break

     guess_count=0

     correct_pass= 'Adjective'

     while True:
          pass_guess = str(input("Small="))

          guess_count += 1

          if pass_guess == correct_pass:
              print("You are correct")
              break

          elif pass_guess != correct_pass:
                    print("Sorry, the real answer is Adjective")
                    break

     guess_count=0

     correct_pass="Noun"

     while True:
          pass_guess = str(input("Snail="))

          guess_count += 1

          if pass_guess == correct_pass:
              print("You are correct")
              break

          elif pass_guess != correct_pass:
                    print("Sorry, the real answer is Noun")
                    break



     guess_count=0

     correct_pass="Verb"

     while True:
          pass_guess = str(input("Climbed="))

          guess_count += 1

          if pass_guess == correct_pass:
              print("You are correct")
              break

          elif pass_guess != correct_pass:
                    print("Sorry, the real answer is Verb")
                    break


     guess_count=0

     correct_pass= 'Preposition'

     while True:
          pass_guess = str(input("over="))

          guess_count += 1

          if pass_guess == correct_pass:
              print("You are correct")
              break

          elif pass_guess != correct_pass:
                    print("Sorry, the real answer is Preposition")
                    break

     guess_count=0

     correct_pass= 'Determiner'

     while True:
          pass_guess = str(input("The="))

          guess_count += 1

          if pass_guess == correct_pass:
              print("You are correct")
              break

          elif pass_guess != correct_pass:
                    print("Sorry, the real answer is Determiner")
                    break

     guess_count=0

     correct_pass="Adjective"

     while True:
          pass_guess = str(input("Slippery="))

          guess_count += 1

          if pass_guess == correct_pass:
              print("You are correct")
              break

          elif pass_guess != correct_pass:
                    print("Sorry, the real answer is Adjective")
                    break



     guess_count=0

     correct_pass="Noun"

     while True:
          pass_guess = str(input("log="))

          guess_count += 1

          if pass_guess == correct_pass:
              print("You are correct")
              break

          elif pass_guess != correct_pass:
                    print("Sorry, the real answer is Noun")
                    break

     guess_count=0

     correct_pass= 'Conjuction'

     while True:
          pass_guess = str(input("And="))

          guess_count += 1

          if pass_guess == correct_pass:
              print("You are correct")
              break

          elif pass_guess != correct_pass:
                    print("Sorry, the real answer is Conjuction")
                    break

     guess_count=0

     correct_pass= 'Verb'

     while True:
          pass_guess = str(input("Inched="))

          guess_count += 1

          if pass_guess == correct_pass:
              print("You are correct")
              break

          elif pass_guess != correct_pass:
                    print("Sorry, the real answer is Verb")
                    break

     guess_count=0

     correct_pass="Adverb"

     while True:
          pass_guess = str(input("Slowly="))

          guess_count += 1

          if pass_guess == correct_pass:
              print("You are correct")
              break

          elif pass_guess != correct_pass:
                    print("Sorry, the real answer is Adverb")
                    break



     guess_count=0

     correct_pass="Preposition"

     while True:
          pass_guess = str(input("Toward="))

          guess_count += 1

          if pass_guess == correct_pass:
              print("You are correct")
              break

          elif pass_guess != correct_pass:
                    print("Sorry, the real answer is Preposition")
                    break

     guess_count=0

     correct_pass= 'Determiner'

     while True:
          pass_guess = str(input("The="))

          guess_count += 1

          if pass_guess == correct_pass:
              print("You are correct")
              break

          elif pass_guess != correct_pass:
                    print("Sorry, the real answer is Determiner")
                    break

     guess_count=0

     correct_pass= 'Adjective'

     while True:
          pass_guess = str(input("Nearby="))

          guess_count += 1

          if pass_guess == correct_pass:
              print("You are correct")
              break

          elif pass_guess != correct_pass:
                    print("Sorry, the real answer is Adjective")
                    break

     guess_count=0

     correct_pass="Noun"

     while True:
          pass_guess = str(input("Fields="))

          guess_count += 1

          if pass_guess == correct_pass:
              print("You are correct")
              break

          elif pass_guess != correct_pass:
                    print("Sorry, the real answer is Noun")
                    break

game = input("Do You want to do Language Arts, Type the password that allows you to go in")

correct = "password"

if game == correct:
    while True:
        guess_count()

if game != correct:
    print ("Sorry you are not allowed to enter the game")
        




time.sleep(2)
