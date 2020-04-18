"""
The Canadian Quiz / Integration Project
"""
__author__ = "Emily McCue"


def next_question(total_positive_points):
    """
    defining a shortcut to move between questions as I use this after
    every question.
    """
    print("\nYour running score is", str(total_positive_points) +
          "/6")
    input("Press enter to continue...\n")
    return total_positive_points


def positive_points(points):
    """
    How I am calculating the points throughout my quiz
    """
    points += 1
    return points


def canadian_percentage_score(total_positive_points):
    """
    This is used to calculate the percentage each person is based off of
    their score
    """
    total_positive_points = int((total_positive_points / 6)
                                * 100)
    total_positive_points = str(total_positive_points)
    return total_positive_points


def main():
    """
    The main file for my Integration project which includes the questions
    and possible answers to the quiz.
    """
    total_positive_points = 0
    # This is the base for calculating positive points and builds each time
    # the person answers a question correctly

    name = input("\nWelcome to the Canadian Quiz! This is a quiz designed to "
                 "test anyone's Canadian spirit! Let's get started!\n\n"
                 "What is your name?\n")
    print("Hi", name + "! Let's start off simple,")
    simple_math = input("What does 1 + 1 equal?\n")
    while simple_math != "2":
        simple_math = input("Oh no, you are not off to a great start. "
                            "Please try again.\nWhat does 1 + 1 "
                            "equal?\n")
    if simple_math == "2":
        total_positive_points = positive_points(total_positive_points)
    next_question(total_positive_points)

    maple_syrup = str.lower(input("Do you like maple syrup? yes or no\n"))
    while "no" != maple_syrup != "yes":
        maple_syrup = str.lower(input("Error: invalid answer, try again.\nDo "
                                      "you like maple syrup? yes or no\n"))
    if maple_syrup == "no":
        print("I am sorry that you have broken tastebuds....")
    elif maple_syrup == "yes":
        print("Congratulations! You have some Canadian in you!")
        total_positive_points = positive_points(total_positive_points)
    next_question(total_positive_points)

    print("Next question is a doozy...")
    toque_count = input("Enter the number of toques you own.\n")
    while not toque_count.isnumeric():
        toque_count = input("Error: please enter a numeric value.\nEnter the"
                            " number of toques you own.\n")
    toque_count = int(toque_count)
    ski_count = input("And now enter how often do you go tobogganing in "
                      "a year?\n")
    while not ski_count.isnumeric():
        ski_count = input("Error: please enter a numeric value.\nEnter the "
                          "number of toques you own.\n")
    ski_count = int(ski_count)
    winter_activities_count = toque_count + ski_count
    if winter_activities_count < 15:
        print("A total of", winter_activities_count,
              "is much too low for a real Canadian...\nMaybe make it",
              winter_activities_count + 10, "and then it would be "
                                            "respectable...")
    else:
        print("A total of", winter_activities_count,
              "is perfect! I know you really love the snow!\nThis year try "
              "to double those to", winter_activities_count * 2,
              "and you'll basically be in the winter games!")
        total_positive_points = positive_points(total_positive_points)
    next_question(total_positive_points)

    sorry_count = input('How many times do you say "sorry" in an average '
                        'day?\n')
    while not sorry_count.isnumeric():
        sorry_count = input('Error: please enter a numeric value.\nHow many '
                            'times do you say "sorry" in an average day?\n')
    sorry_count = int(sorry_count)
    if sorry_count <= 20:
        print("Wow, someone is a little rude. That'll definitely knock some "
              "points off...")
    else:
        print("Yay! I'm sorry I even asked you!")
        total_positive_points = positive_points(total_positive_points)
    next_question(total_positive_points)

    print("What is the capital of Canada?\n")
    possible_capitals = ["1. Montreal", "2. Ottawa", "3. Edmonton",
                         "4. " "Vancouver"]
    for x in possible_capitals:
        print(x)
    canada_capital = input("\nEnter the correct number\n")
    while not canada_capital.isnumeric():
        print("Error: please the enter the numeric value correlating to the "
              "correct answer.\nWhat is the capital of Canada?\n")
        for x in possible_capitals:
            print(x)
        canada_capital = input("\nEnter the correct number\n")
    canada_capital = int(canada_capital)
    montreal = int(1)
    ottawa = int(2)
    edmonton = int(3)
    vancouver = int(4)
    if canada_capital == montreal:
        print("False! A true Canadian would know the capital is Ottawa.")
    elif canada_capital == ottawa:
        print("Correct! You are the best!")
        total_positive_points = positive_points(total_positive_points)
    elif canada_capital == edmonton:
        print("False! A true Canadian would know the capital is Ottawa.")
    elif canada_capital == vancouver:
        print("False! A true Canadian would know the capital is Ottawa.")
    else:
        print("I don't think you're even trying.")
    next_question(total_positive_points)

    print("Okay, last few questions... I believe in you!")
    next_question(total_positive_points)

    canadian_citizenship = str.lower(input("Are you a Canadian citizen?\n"
                                           "yes or no\n"))
    while "no" != canadian_citizenship != "yes":
        canadian_citizenship = str.lower(input("Error: invalid answer, try "
                                               "again. Are you a Canadian "
                                               "citizen?\nyes or no\n"))
    if canadian_citizenship == "yes":
        print("Heck yes, go Canada!")
        total_positive_points = positive_points(total_positive_points)
        print("Good job! You are on the right track!\nyour running score is",
              str(total_positive_points) + "/6")
    elif canadian_citizenship == "no":
        canadian_cit_question = str.lower(input("Do you want to become "
                                                "Canadian?\nyes or no\n"))
        while "no" != canadian_cit_question != "yes":
            canadian_cit_question = str.lower(input("Error: invalid answer, "
                                                    "try again. Do you want to"
                                                    " become Canadian?\nyes "
                                                    "or no\n"))
        if canadian_cit_question == "yes":
            print("Heck yeah! I love the enthusiasm!")
            total_positive_points = positive_points(total_positive_points)
            print("Good job! You are on the right track!\n"
                  "your running score is", str(total_positive_points) + "/6")
        else:
            input("Well, you are definitely not Canadian at heart, that's "
                  "too bad for you.\nPress enter to continue...")

    input("\nYou have reached the end of the quiz\nPress enter to find out "
          "if you are Canadian!\n")

    if total_positive_points != 6:
        if 5 == total_positive_points:
            print(name + ", congratulations! You got",
                  canadian_percentage_score(total_positive_points) +
                  "% of the questions correct, you're probably half Canadian "
                  "or more!")
        elif 4 == total_positive_points:
            print(name + ", good job! you got",
                  canadian_percentage_score(total_positive_points) +
                  "% of the questions correct, you are on your way to becoming"
                  " a true Canadian!")
        elif 3 == total_positive_points:
            print(name + ", you passed! you got",
                  canadian_percentage_score(total_positive_points) +
                  "% of the questions correct, with some hard work, I am "
                  "sure you can become a Canadian.")
        elif 2 >= total_positive_points:
            print(name + ", unfortunately, you did not pass the quiz as you "
                         "got",
                  canadian_percentage_score(total_positive_points) +
                  "% and that is below the passing score of 50%.")
    else:
        print("6/6\n\nWow, that's",
              canadian_percentage_score(total_positive_points) +
              "!", name + ", the results are in and you are definitely "
                          "Canadian!")

    print("\nThe end!")


main()
