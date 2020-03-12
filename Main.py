#Intergration Project
#Emily McCue
#Canadian Quiz

next_question = ("\nPress enter to continue...")
#short cut as I add this after every question
print("Welcome to the Canadian Quiz!")
name = input("\nWhat is your name?\n")

print("Hi", name + "!\n\nLet's start off simple,")
simple_math = int(input("\nwhat does 1 + 1 equal?\n"))
if (simple_math == 2):
    print("Good job!\n\nyou are on the right track!")
else:
    print("Oh no... not off to a great start.")
print(next_question)
input()

maple_syrup = input("Do you like maple syrup? yes or no\n")
if (maple_syrup == "no"):
    print("I am sorry that you have broken tastebuds....")
else:
    print("Congratulations! You have some Canadian in you!")
print(next_question)
input()

print("Next question is a doozy...")
toque_count = int(input("\nType the number of toques you own.\n"))
ski_count = int(input("And now type how often do you go sledding in a year?\n"))
toque_count += ski_count
if (toque_count < 15):
    print("A total of",toque_count, "is much too low for a real Canadian...\nmaybe if you add 10 to those numbers and make it", toque_count + 10, "then it would be respectable...")
else:
    print("A total of",toque_count, "is perfect! I know you really love the snow!\n\nthis year try to double those to", toque_count * 2, "and you'd basically be in the winter games!")
print(next_question)
input()

sorry_count = int(input('How many times do you say "sorry" in an average day?'))
if (sorry_count <= 20):
    print("Wow, someone is a little rude. That'll definitely knock some points off...")
else:
    print("Good job! I'm sorry I even asked you!")
print(next_question)
input()

print('''What is the capital of Canada?

1. Montreal
2. Ottawa
3. Edmonton
4. Vancouver

Enter the correct number''')
montreal = int(1)
ottawa = int(2)
edmonton = int(3)
vancouver = int(4)
canada_capital = int(input())
if (canada_capital == montreal):
    print("False!")
elif (canada_capital == ottawa):
    print("Correct! You are the best!")
elif (canada_capital == edmonton):
    print("False!")
elif (canada_capital == vancouver):
    print("False!")
else:
    print("I don't ever think you're even trying.")
print(next_question)
input()

print("Okay, last few questions...\n\nI believe in you!")
print(next_question)
input()

canadian_citizenship = input("Are you a Canadian citizen?\n\nyes or no")
if (canadian_citizenship == "yes"):
    print("Heck yes, the results are in, you are a Canadian!")
elif (canadian_citizenship == "no"):
    print("Do you want to become Canadian?\n\nyes or no")
    canadian_cit_question = input()
    if (canadian_cit_question == "yes"):
        print("Heck yeah! Welcome to the party, you are now officially Canadian!!")
    else:
        print("Well, you are definitely not Canadian at heart, that's too bad for you.")
print("\nThe end!")
