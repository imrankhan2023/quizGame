print("Welcome to my quiz game! ")

playing = input("Do you want to play ?\n")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play:) ")
score = 0

answer = input("Which keyword is used to define the function in python?\n")

if answer.lower() == "Def":
    print("Well done! You are correct.")
    score += 1
    
else:
    print("Incorrect!")
    
answer = input("Why we use import keyword in python?\n")

if answer.lower() == "To import modules":
    print("Well done! You are correct.")
    score += 1
    
else:
    print("Incorrect!")
    
answer = input("Which keyword is used to take input in python?\n")

if answer.lower() == "input":
    print("Well done! You are correct.")
    score += 1
    
else:
    print("Incorrect!")
    
answer = input("What does GUI stands for?\n")

if answer.lower() == "Graphical user interface":
    print("Well done! You are correct.")
    score += 1
    
else:
    print("Incorrect!")
    
print("You got " + str(score) +   "Questions correct")
print("You got " + str((score / 4) * 100) + "%.")