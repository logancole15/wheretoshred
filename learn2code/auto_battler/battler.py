from super_pet import Pokemon
from super_pet import Ability
import random

weaknesses = {
    "fire":"water",
    "water":"earth",
    "earth":"water",
}

def start_game():

    #Choose 1 of 3 pokemons
    pokes = [
        Pokemon("charmander", 3, 2, [
            Ability("fireball", "hurls a fireball", "fire"),
            Ability("scratch", "scratches with claws", "normal"),
            ], "fire"),
        Pokemon("squirtle", 3, 3, [
            Ability("squirt", "squirts water","water"),
            Ability("heal", "calls upon the holy spirit within to heal", "normal"),
            ], "water"),
        Pokemon("bulbasaur", 2, 4, [
            Ability("vine whip", "whips a sharp vine", "earth"),
            Ability("block", "blocks with leaf", "normal"),
            ], "earth"),
    ]

    
    Pokemon.__str__()
    for poke in pokes:
        print(poke)

    player_poke = input("Choose your pokemon!")

    # x = input("Choose your pokemon: 1 for "+ pokes[0].name + ", " + pokes[1].name + ", " + pokes[2].name + ": ").lower()
    # player_choice = pokes[x]



    # print("You chose " + player_choice.name)
    # #Computer chooses opponent

    # computer_choice = random.choice(pokes.values)

    # computer_choice = pokes[random.randint(0,2)]

    # while computer_choice.name == player_choice.name: 
    #     computer_choice = random.choice(pokes.values)
    # print("Your opponent chose " + computer_choice.name)

    # #Choose from list of abilities - pre turn
    # ability_choice = input("Choose which " + player_choice + " ability you would like to use: " + player_choice.A)


    # Battle phase
        # Your ability
        # Opponent's ability
        # Result of battle

    # Play again?




if __name__ == "__main__":
    start_game()