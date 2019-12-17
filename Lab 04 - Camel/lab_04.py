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
            natives_distance += num
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


main()
