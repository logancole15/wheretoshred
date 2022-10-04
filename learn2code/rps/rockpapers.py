import random

options = ["Rock","Paper","Scissors"]
player_input = input("Enter " + options[0] + ", " + options[1] + ", or "+ options[2] + ": ")

def rps(player_input):
    
    rematch_options = ["Yes","No"]
    play_again = rematch_options[0]
    win_score = 0
    lose_score = 0 

    while play_again == rematch_options[0]:

        computer_input = random.choice(options)

        if player_input == computer_input:
            print("The computer chose " + computer_input + ", tie!")
        elif player_input == options[0] and computer_input == options[1]:
            lose_score += 1
            print("The computer chose " + computer_input + ", you lose!")
        elif player_input == options[1] and computer_input == options[2]:
            lose_score += 1
            print("The computer chose " + computer_input + ", you lose!")
        elif player_input == options[2] and computer_input == options[0]:
            lose_score += 1
            print("The computer chose " + computer_input + ", you lose!")
        else:
            win_score += 1
            print("The computer chose " + computer_input + ", you win!")

        print("The score is " + str(win_score) + " to " + str(lose_score) + "\nWould you like to play again?")

        play_again = input("Enter Yes or No: ")

        if play_again == rematch_options[0]:
            player_input = input("Enter " + options[0] + ", " + options[1] + ", or "+ options[2] + ": ")
        else:
            print("The final score is " + str(win_score) + " to " + str(lose_score))
        
rps(player_input)
