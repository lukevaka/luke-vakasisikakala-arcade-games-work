import random


def main():
    print("Welcome to The Pacific!")
    print("You have stolen a boat to make your way across the great Pacific Ocean in search of a new island.")
    print("The natives want their boat back and are chasing you down! Survive your")
    print("ocean trek and out boat the natives.\n")

    distance = 0
    thirst = 0
    tiredness = 0
    natives_distance = -20
    canteen = 3
    d_diff = 0

    done = False
    while not done:
        print('\nA. Drink from your canteen.')
        print('B. Ahead moderate speed.')
        print('C. Ahead full speed.')
        print('D. Stop for the night.')
        print('E. Status check.')
        print('Q. Quit\n')

        d_diff = (distance - natives_distance) - 10

        user_choice = input('What is your choice? ')
        if user_choice.upper() == "Q":
            done = True
            print("The game has ended")
        elif user_choice.upper() == "E":
            print('Miles traveled: ' + str(distance))
            print('Drinks in canteen: ' + str(canteen))
            print('The natives are ' + str(d_diff) + ' miles away')
        elif user_choice.upper() == "D":
            tiredness = 0
            print('You are well rested')
            num = random.randrange(7, 14)
            natives_distance += num
        elif user_choice.upper() == "C":
            num = random.randrange(10, 20)
            distance += num
            print('You have traveled ' + str(num) + ' miles')
            thirst += 1
            tiredness += random.randrange(1, 3)
            num = random.randrange(7, 14)
            natives_distance += num
            oasis = random.randrange(1, 20)
            chance = random.randrange(1, 20)
            if chance == oasis:
                print('You have found an oasis!')
                canteen = 3
                thirst = 0
                tiredness = 0
        elif user_choice.upper() == "B":
            num = random.randrange(5, 12)
            distance += num
            print('You have traveled ' + str(num) + ' miles')
            thirst += 1
            tiredness += 1
            num = random.randrange(7, 14)
            d_diff += (distance - natives_distance)
            oasis = random.randrange(1, 20)
            chance = random.randrange(1, 20)
            if chance == oasis:
                print('You have found an oasis!')
                canteen = 3
                thirst = 0
                tiredness = 0
        elif user_choice.upper() == "A":
            if canteen != 0:
                canteen -= 1
                thirst = 0
                print('You are no longer thirsty')
            else:
                print('There is no more drank my guy')
        if thirst > 6:
            print('You died of thirst!')
            done = True
        elif thirst > 4:
            print('You are thirsty.\n')
        if tiredness > 8:
            print('You have died of exhaustion!')
            done = True
        elif tiredness > 5:
            print("You are getting tired")
        if natives_distance >= distance:
            print("The natives caught you!")
            done = True
        elif d_diff <= 15:
            print('The natives are getting close!')
        if distance >= 200:
            print('You have won! Welcome to your new island!')
            done = True


main()
