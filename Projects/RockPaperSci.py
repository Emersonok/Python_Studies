import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
get_images = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n "))
print(get_images[player])

#rock(0) wins scissors(2)
#scissors(2) wins paper(1)
#paper(1) wins rock(0)

computer = random.randint(0, 2)
print("Computer choose: ")
print(computer)
print(get_images[computer]) #using the value [0, 1, 2] as index

rock_win = 2
scissors_win = 3
paper_win = 1
decision = player + computer

if decision == rock_win and player < computer:
  print("You win")
elif decision == scissors_win and player > computer:
  print("You win")
elif decision == paper_win and player > computer:
  print("You win")

elif decision == rock_win and player > computer:
  print("You lose")
elif decision == scissors_win and player < computer:
  print("You lose")
elif decision == paper_win and player < computer:
  print("You lose")
elif player == computer:
  print("Draw game")

