###########################################################
# ========ROCK , PAPER, SCISSOR PYGAME(MINIGAME) =========#
###########################################################



# rock.paper,scissor game between user and computer:

# importing modules to randomly generate the computers choice
import random


comp_wins = 0
user_wins = 0


def choose_option():
    user_choice = input("Choose rock , paper or scissor : ")
    if user_choice in ["rock" ,"Rock","r", "R"]:
        user_choice = "r"
    elif user_choice in ["paper","Paper","p", "P"]:
        user_choice = "p"
    elif user_choice in ["scissor","Scissor","s", "S"]:
        user_choice = "s"
    else:
        print("Wrong Input..")

    return user_choice


def computer_option():

    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    elif comp_choice == 3:
        comp_choice = "s"

    return comp_choice



#
# # Game starts here....................
#


def rps_game():

    global comp_wins,user_wins

    while True:
        # There will be two players
        user_choice = choose_option()
        comp_choice = computer_option()

        if user_choice == "r":
            if comp_choice == "r":
                print("You chose rock. Computer chose rock .Tie!")

            elif comp_choice == "p":
                print("You chose rock. Computer chose paper . You lose!")
                comp_wins += 1

            elif comp_choice == "s":
                print("You chose rock. Computer chose scissor . You win!")
                user_wins += 1

        elif user_choice == "p":
            if comp_choice == "r":
                print("You chose paper. Computer chose rock .You win!")
                user_wins += 1

            elif comp_choice == "p":
                print("You chose paper. Computer chose paper . Tie!")

            elif comp_choice == "s":
                print("You chose paper. Computer chose scissor . You Lose!")
                comp_wins += 1

        elif user_choice == "s":
            if comp_choice == "r":
                print("You chose scissor. Computer chose rock .You lose!")
                comp_wins += 1

            elif comp_choice == "p":
                print("You chose scissor. Computer chose paper . You win!")
                user_wins += 1

            elif comp_choice == "s":
                print("You chose scissor. Computer chose scissor . Tie!")


        print()
        print("**********************")
        print("* Score Board: ")
        print("* User wins ",user_wins)
        print("* Computer wins ",comp_wins)
        print("**********************")
        print()
        cc = input("Do you want to play again?(y/n) ")
        if cc in ["y","Y","yes","Yes"]:
            pass
        else:
            break


rps_game()
