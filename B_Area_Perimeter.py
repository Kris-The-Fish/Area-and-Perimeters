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
rounds_played = 0
end_game = "no"
feedback = ""
rounds_lost = 0
game_history = []
guesses_allowed = 1
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

num_rounds = int_check("Rounds ? ", exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5
    print("♾️you have picked infinite mode!♾️")
else:
    print(f"💿you have picked [{num_rounds}] rounds!💿")

while rounds_played < num_rounds:

    # rounds heading
    if mode == "infinite":
        rounds_heading = f"\n♾️️️♾️️️♾️️️ Round {rounds_played + 1} (Infinite Mode) ♾️️️♾️️️♾️️️"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"
    print(rounds_heading)
    if mode == "infinite":
        num_rounds += 1


    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)

    area = num1 * num2
    perimeters = num1 + num2 + num1 + num2
    # round starts here

    a_p = random.randint(1, 2)
    if a_p == 1:
        a_p = "area"
    else:
        a_p = "parameters"

    if a_p == "area":
        answer = area
    else:
        answer = perimeters

    # print("Spoiler Alert!!!", answer)       # remove this line after testing !!!

    if a_p == "area":
        guess = int_check(f"A rectangle has a base of {num1}cm and a height of {num2}cm, what is the AREA in cm? : ", "xxx")
    else:
        guess = int_check(f"A rectangle has a base of {num1}cm and a height of {num2}cm, what is the PERIMETERS in cm? : ", "xxx")

    if guess == "xxx":
        end_game = "yes"
        break

    if guess == answer:
            feedback = "✅✅✅ Yes! that is Correct! good job ✅✅✅"
    else:
        feedback = f"❌❌❌ NO! that is wrong! the answer is [{answer}cm]! ❌❌❌"
        rounds_lost += 1

    # print feedback to user
    print(feedback)


    # round ends here

    # if user has entered exit code, end game!!
    if end_game == "yes":
        break

    rounds_played += 1

    # calculate statistics
    rounds_won = rounds_played - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100

    # add round result to game history
    history_feedback = f"\nRound {rounds_played}: {feedback}"
    game_history.append(history_feedback)

if rounds_played > 0:
    # calculate statistics
    rounds_won = rounds_played - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100

    # output game statistics
    print()
    print("📊📊📊Game Statistics📊📊📊")
    print(f"👍Won: {percent_won: .2f} \t "
          f"😢Lost: {percent_lost:.2f} \t ")

    # Ask user if they want to see their game history output if it requested
    see_history = yes_no("\nDo you want to see your Game History? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

else:
    print()
    print("No History is available")

print()
print("Thanks for playing !")