import random
lst = ['s','w','g']

chance = 10
no_of_chances = 0
computer_point = 0
human_point = 0

print("\t \t \t \t Snake, Water, Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")

#making the game in while
while no_of_chances < chance:
    _input = input('Snake,Water,Gun:')
    _random = random.choice(lst)

    if _input == _random:
        print('Tie, 0 point to both \n')

    # if user enter s
    elif _input == 's' and _random == 'g':
        computer_point = computer_point +1
        print(f"Your guess is {_input} and computer guess is {_random} \n")
        print("Computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == 's' and _random == 'w':
        human_point = human_point +1
        print(f"Your guess is {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter w
    elif _input == 'w' and _random == 's':
        computer_point = computer_point + 1
        print(f"Your guess is {_input} and computer guess is {_random} \n")
        print("Computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == 'w' and _random == 'g':
        human_point = human_point + 1
        print(f"Your guess is {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter g
    elif _input == 'g' and _random == 'w':
        computer_point = computer_point + 1
        print(f"Your guess is {_input} and computer guess is {_random} \n")
        print("Computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == 'g' and _random == 's':
        human_point = human_point + 1
        print(f"Your guess is {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    else:
        print("You have input wrong \n")

    no_of_chances = no_of_chances +1
    print(f"{chance - no_of_chances} is left out of {chance} \n")

print('Game over')

if computer_point == human_point:
    print('Tie')

elif computer_point > human_point:
    print('Computer won you loose')

else:
    print('You win and computer loose')

print(f"Your point is {human_point} and computer point is {computer_point}")

# Snake Water Gun Game in python
# THe snake drinks the water, the gun shoots the snake, and gun has no effect on water.
