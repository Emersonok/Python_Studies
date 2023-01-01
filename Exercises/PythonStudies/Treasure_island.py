print("WELCOME TO TREASURE ISLAND \nYour mission is to find the treasure.")

name = input("What is your name? ")
cross_road = input("You are at a crossroad. Where do you want to go? left or right? ")


if cross_road == "left":
    lake = input("You come to a lake. \nThere is an island in the middle of the lake. \nType 'wait' to wait for a boat. Type 'swim' to swim across ")
    if lake == "wait":
        island = input("You arrive at the island unharmed. \nThere is a house with 3 doors. \nOne red. one yellow and one blue. Which color do you choose? ")
        if island == "blue":
            print("You enter a room of beasts. Game Over")
        if island == "red":
            print("You enter a room of beasts. Game Over")

        if island == "yellow":
            print(f"Congratulations {name}! You found the treasure")
        
          
    elif lake == "swim":
        print("You Lose! Game Over")
elif  cross_road == "right":
    print("You Lose! Game Over")