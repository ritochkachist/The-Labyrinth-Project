#Peyton Reese and Margarita Chistiakova
#11/14/22
#THE LABYRINTH

#Random  
import random
#Function
def randGame(number):
  return (f"The random number was {number}\n")
  
#Lists and loops
#Picking Player
print("Welcome to the Labyrinth!")
print("We have several characters to play for: ")
playerOptions = ['Knight', 'Dwarf', 'Princess', 'Vampire', 'Human']
for players in playerOptions:
  print(f"* {players} ")
print("Please choose your player: ")

player = input()
print(f"You are playing as a {player}. Let's start the game!\n")


# Which Door?
print("You see three doors in front of you.")
print("Which one will you choose? Door #1, door #2 or door #3?")

door = input("> ")

if door == "1":
  print("There is a huge hungry bear.")
  print("What will you do?")
  print("1. Feed the bear with honey.")
  print("2. Feed the bear with stones.")
  print("3. Scream at the bear.")
# If Statements
  bear = input("> ")
  if bear == "1":
    print("The bear eats honey and falls asleep. You can continue walking.\n")
  elif bear == "2":
    print("The bear eats the stones and dies. You can continue walking.\n")
  else:
    print("Bear attacks you. You die. Game over.\n")
    exit()

if door == "2":
  print("There is a wicked Baba Yaga. She offers you to eat and sleep in her hut.")
  print("What will you do?")
  print("1. Eat and sleep in the hut of Baba Yaga.")
  print("2. Show her a trick.")
  print("3. Scream at her.")

  babaYaga = input("> ")
  if babaYaga == "1":
    print("Baba Yaga poisons you. You die. Game over.\n")
    exit()
  elif babaYaga == "2":
    print("Baba Yaga likes your trick! She will help you to get out of the Labyrinth! You can continue walking!\n")
  else:
    print("Baba Yaga turns you into a frog. Game over.\n")
    exit()

if door == "3":
  print("""You open the door and you see a purple magic light! You decide to follow it and it leads you to a sunny road.\n""")

print("...")
input()

  
#Rock, Paper, Scissors
print("Upon your walk of the labyrinth, you come across a Rockman... He challenges you to a quick game of Rock, Paper, Scissors.")
print("What would you like to throw? Type 'R'' for Rock, 'P' for Paper, or 'S' for Scissors.")

shoot = input("> ")
answer = ["R", "P", "S"]
rm_shoot = random.choice(answer)
print('Rock, Paper, Scissors SHOOT!')
print(f'You threw {shoot} and Rockman threw {rm_shoot}')
if shoot == rm_shoot:
  print(f'You both threw {shoot}. It is a tie! You have proved equally as smart as Rockman, he lets you pass!\n')
elif shoot == "R":
  if rm_shoot == "S":
    print('Rock beats Scissors! You Win! You can continue on!\n')
  else:
    print('Paper beats Rock! Rockman Wins! You get turned to rock and die!\n')
    exit()
elif shoot == "P":
  if rm_shoot == "R":
    print('Paper beats Rock! You Win! You can continue on!\n')
  else:
      print('Scissors beats paper! Rockman Wins! You get turned to rock and die!\n')
      exit()
elif shoot =="S":
  if rm_shoot == "P":
    print('Scissors beats Paper! You Win! You can continue on!\n')
  else:
    print('Rock beats Scissors! Rockman wins! You get turned to rock and die!\n')
    exit()
else:
    print("Oops! You messed with the game and now its broken... please restart!")
    exit()

print("...")
input()

#Maze
print("""As you continue on, you approach a maze. The maze opens up to the left, right, and straight.
You will need to guess the correct order of direction to navigate through the maze...
Please enter 'L' to go left, 'R' to go right, and 'S' to go straight... you will enter 6 times. (Case sensitive so use uppercase letters) *HINT- Think of a London Rail System*\n""")

# Directions
print("Enter a direction...")
direction1 = input("> ")
if direction1 == "L":
  print("You guessed the first direction right! Continue!")
else:
  print("You guessed wrong and got lost, you starved and died.")
  exit()

direction2 = input("> ")
if direction2 == "R":
  print("You guessed the second direction correct! Continue straight on!")
else:
  print("You guessed wrong and got lost, you starved and died.")
  exit()

direction3 = input("> ")
if direction3 == "S":
  print("Right! Right! Right! Boom! You guessed three directions!")
  print("Enter the next direction...")
else:
  print("You guessed wrong and got lost, you starved and died.")
  exit()

direction4 = input("> ")
if direction4 == "R":
  print("You are smart! Continue!")
else:
  print("You guessed wrong and got lost, you starved and died.")
  exit()

direction5 = input("> ")
if direction5 == "R":
  print("You are very smart! Please choose the last direction!")
else:
  print("You guessed wrong and got lost, you starved and died.")
  exit()

direction6 = input("> ")
if direction6 == "R":
  print("""You made it out of the maze. Congratulations! 
You see a magic broom of Baba Yaga! You decide to sit on it and it delivers you straight to the finish of the Labyrinth!\n""")
else: 
  print("You guessed wrong and got lost, you starved and died.")
  exit()

print("...")
input()

#Random Number Game
print("Your last challenge is guessing a random number. Choose wisely!")

evenList=[0, 2, 4]
randNumber = random.choice(evenList)

number = int(input("Please Enter a number from 0 to 5: \n> "))
if number % 2 == 0:
  print("Congratulations! You guessed the number!")
else:
  print("Unfortunately, your choice was wrong. You are stuck in Labyrinth forever.")
  exit()

answer = randGame(number)
print(answer)
  
#Ending
print(f"The {player} takes their first steps out of the labyrinth. The air smells fresh and there is a feeling of releif come over the {player}. There is a horse nearby and the {player} saddles up and rides off into the horizon, in victory!")