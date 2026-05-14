import random

def yes_no(question):
    """Checks user response to a questin is yes / no (y/), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says yes / no / Y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")

def instructions():
    """prints instructions"""

    print("""
**** Instructions ****

you'll be asked questions about different rectangles 
you'll be asked about their area or perimeters 
Answer correctly 

Good Luck ! 
    """)

def int_check(question, exit_code=None):



    while True:
        response = input(question).lower()

        # check for infinite mode / exit mode
        if exit_code is not None and response == exit_code:
            return response

        try:
            response = int(response)

            return response


        except ValueError:
            print("Please enter a number")

# Main Routine Starts here

# game variables
mode = "regular"
questions_asked = 0
end_quiz = "no"

answered_wrong = 0
quiz_history = []

guess = ""


print()
print("Area and Perimeters!")
print()

# ask if the user wants instructions
want_instructions = yes_no("Do you want to read the instructions? ")
# check user enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()
if want_instructions == "no":
    print("OK! No instructions it is!")
print()

# ask the user how many rounds they would like. <enter for infinite>
num_of_questions = int_check("How many questions would you like to answer ? <enter for infinite> ", exit_code="")
if num_of_questions == "":
    mode = "infinite"
    num_of_questions = 5
    print("♾️you have picked infinite mode!♾️")
else:
    print(f"❓you have picked [{num_of_questions}] rounds!❓")

# rounds
while questions_asked < num_of_questions:

    # Question heading
    if mode == "infinite":
        rounds_heading = f"\n♾️️️♾️️️♾️️️ Question {questions_asked + 1} (Infinite Mode) ♾️️️♾️️️♾️️️"
    else:
        rounds_heading = f"\n❓❓❓ Question {questions_asked + 1} of {num_of_questions} ❓❓❓"
    print(rounds_heading)
    if mode == "infinite":
        num_of_questions += 1

    # generate the numbers and whether it's area or perimeters at random
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)

    # calculate the answer
    area = num1 * num2
    perimeters = num1 + num2 + num1 + num2

    # pick randomly between area and perimeters
    area_or_perimeters = random.randint(1, 2)
    if area_or_perimeters == 1:
        area_or_perimeters = "area"
    else:
        area_or_perimeters = "parameters"

    # answer matched up with the right one (area or perimeters)
    if area_or_perimeters == "area":
        answer = area
    else:
        answer = perimeters

    # round starts here

    # print("Spoiler Alert!!!", answer)       # remove this line after testing !!!

    # print question
    if area_or_perimeters == "area":
        guess = int_check(f"A rectangle has a base of {num1}cm and a height of {num2}cm, what is the AREA in cm²? : ", "xxx")
    else:
        guess = int_check(f"A rectangle has a base of {num1}cm and a height of {num2}cm, what is the PERIMETERS in cm? : ", "xxx")

    # allow user to exit game
    if guess == "xxx":
        end_quiz = "yes"
        break

    # if the user answer right, tell them. if wrong, also tell them, and add to the wong tally
    if guess == answer:
            feedback = "✅✅✅ Yes! that is Correct! good job ✅✅✅"
    else:
        feedback = f"❌❌❌ NO! that is wrong! the answer is [{answer}cm]! ❌❌❌"
        answered_wrong += 1

    # print feedback to user
    print(feedback)

    # round ends here

    # if user has entered exit code, end game!!
    if end_quiz == "yes":
        break

    questions_asked += 1

    # calculate statistics
    rounds_correct = questions_asked - answered_wrong
    percent_correct = rounds_correct / questions_asked * 100
    percent_lost = answered_wrong / questions_asked * 100

    # add round result to game history
    history_feedback = f"\nRound {questions_asked}: {feedback}"
    quiz_history.append(history_feedback)

# history
if questions_asked > 0:
    # calculate statistics
    rounds_correct = questions_asked - answered_wrong
    percent_correct = rounds_correct / questions_asked * 100
    percent_lost = answered_wrong / questions_asked * 100

    # output game statistics
    print()
    print("📊📊📊Game Statistics📊📊📊")
    print(f"👍Correct: {percent_correct: .2f} \t "
          f"😢Wrong: {percent_lost:.2f} \t ")

    # Ask user if they want to see their game history output if it requested
    see_history = yes_no("\nDo you want to see your Game History? ")
    if see_history == "yes":
        for item in quiz_history:
            print(item)

        print()
        print(f"📈📈📈 You got {rounds_correct} correct and {answered_wrong} wrong 📉📉📉")

else:
    print()
    print("No History is available")

print()
print("🍏 Thanks for using this quiz that I, Kris, made ! 🍏")
print()
