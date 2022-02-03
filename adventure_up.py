def thug(h):
    hit_points = h - 4
    print('You lose 4 Hit Points. You know have {0} Hit Points'.format(hit_points))
    return hit_points


def boss(h):
    hit_points = h - 6
    print('You lose 6 Hit Points. You know have {0} Hit Points'.format(hit_points))
    return hit_points


def medkit(h):
    hit_points = h + 6
    if hit_points > 20:
        hit_points = 20
    else:
        print('You now have {0} Hit Points'.format(hit_points))
    return hit_points


def bar():
    print('You rush in the bar, but quickly realize the mistake you made. '
          'In front of you are dozens of bandits, thieves, rogues and other ilk.')
    print('They swarm you and you are dead.')
    print('Would you like to play again?')

    choose = input("Yes or No? ")
    return choose


def store():
    print('Upon entering the convenience store, two of the bandits are holding up the clerk. '
          'She looks at you for aid, hoping you can save her.')
    print("Do you fight both bandits, or just one? 1 or 2")
    choose = input('1 or 2')
    return choose


hp = 20

bag = {'Medkit': 1}

cont = True
save = True

while cont:
    cont = True
    print('You are awoken one night by the sounds of screams outside of the little hut you are staying in.')
    print('Do you a: Pick up the small stick next to your bed to defend yourself?')
    print(' or b: Hide in the crawl space underneath the floorboards?')
    choice = input("Choice wisely, a or b. ")

    if choice == 'a' or choice == 'A':
        print('As you grab the stick next to your bed, half a dozen men burst into your hut '
              'holding knives, bats, and other pointy instruments of death. '
              'They swarm you and you are dead.')

        file = open('gamehistory.txt', 'a')
        file.write('In this game you fought bravely to protect your precious D20, but died.\n')
        file.close()

        print('Would you like to play again?')
        choice = input("Yes or No? ")
        if choice == 'yes' or choice == 'Yes':
            cont = True
        else:
            cont = False
    elif choice == 'b' or choice == 'B':

        while save:
            print('Ignoring the stick, you hurry to the hidden trap door in the floor. '
                  'You lay silently in the dirt while you feet pound the hard on the floor '
                  'boards above and men bark orders at each other.')
            print('What little furniture in is the hut, you hear gets slammed to the ground as the men turn them over '
                  'haphazardly. After a few minutes, the sounds cease as the men hurry out the door.')
            print('Waiting several minutes more, you emerge from under the floorboards. Your hut is a mess and your '
                  'backpack is open. Quickly, you examine it to see what was taken. NO! Your weighted D20.')
            print('How are you going to roll those crits now? The thieves must pay. You hurry out of the hut and '
                  'see the bandits riding out of town. Looking around you see a bicycle and a horse.')
            choice = input('Do you go for the bicycle on your left or the horse on your right? bicycle or horse ')

            if choice == 'bicycle' or choice == 'Bicycle':
                while save:
                    print('A couple hours later you pedal into the nearest city. You lost track of the bandits, '
                          'but what do bandits always do after a raid? Go drinking or rob a convenience store.')
                    choice = input('Go to the bar or convenience store? bar or store ')

                    if choice == 'bar' or choice == 'Bar':
                        choice = bar()

                        file = open('gamehistory.txt', 'a')
                        file.write('In this game you hid like a coward and rode a bike into the city. Sadly, you'
                                   ' entered the wrong bar.\n'
                                   'Death did not come swift.\n ')
                        file.close()

                        if choice == 'yes' or choice == 'Yes':
                            cont = True
                            save = False
                        else:
                            cont = False
                            save = False

                    elif choice == 'store' or choice == 'Store':
                        choice = store()

                        if choice == '1' or choice == 'one' or choice == 'One':
                            print('You rush the closest bandit and tackle him to the ground. He manages get off a '
                                  'lucky punch before you knock him out.')
                            hp = thug(hp)
                            bag['Medkit'] = 2
                            heal = input('Would you like to use a medkit? You have {0}.'
                                         ' yes or no'.format(bag['Medkit']))

                            if heal == 'yes' or heal == "Yes":
                                hp = medkit(hp)
                                bag['Medkit'] = 1

                            print('As you stand the other bandit drops his knife in fear of you and bolts for the'
                                  ' door.')
                            print('You chase him out of the store and down the street several blocks where he runs '
                                  'into an abandoned building. This must be their Hideout.')
                            choice = input('Do you sneak inside or rush the front door? sneak or rush')

                            if choice == 'sneak' or choice == 'Sneak':
                                print('Sneaking around to the side, you find an open window. Climbing inside '
                                      'you spy the guy from the store.')
                                print('You follow him via the catwalk in the rafters where you see him enter a room. '
                                      'Stealthily, you climb down to the main floor and enter the room.')
                                print('Inside, however, is not only the guy from the store but two of his buddies. '
                                      'They rush you as you prepare to defend yourself.')
                                hp = thug(thug(thug(hp)))

                                heal = input('Would you like to use a medkit? You have {0}.'
                                             ' yes or no'.format(bag['Medkit']))

                                if heal == 'yes' or heal == "Yes":
                                    if bag['Medkit'] == 1:
                                        hp = medkit(hp)
                                        bag['Medkit'] = 0
                                    else:
                                        hp = medkit(hp)
                                        bag['Medkit'] = 1

                                print('After defeating the three bandits, you search their bodies for your D20. '
                                      'DRAT! Its not there.')
                                choice = input('Do you proceed through the door at the back of the room, or'
                                               ' do you forget about it? You can always make another weighted D20.'
                                               ' door or escape')
                                if choice == 'door' or choice == 'Door':
                                    print('You burst through the door to see the Bandit Boss. He is sitting '
                                          'at his desk rolling YOUR dice. Glee sparkles in his eyes at the power '
                                          'he holds.')
                                    print('Angrily, you rush forward, "That is my dice!"')
                                    print('You and the Boss roll to the ground, a whirlwind of fists flying through'
                                          ' the air.')
                                    hp = boss(hp)

                                    if hp < 0:
                                        print('As you deliver the final blow, you feel a pain in your side. '
                                              'Looking down you see a dagger protruding from your side.')
                                        print('You reach to the desk, weakily you grab the dice. As you make your way'
                                              ' to the door, you drop to the floor.')
                                        print('Thanks for playing. You got your D20, but it cost you everything.'
                                              ' Should have used more Medkits.')

                                        file = open('gamehistory.txt', 'a')
                                        file.write(
                                            'In this game you hid like a coward and rode a bike into the city. You'
                                            ' stopped a couple bandits from robbing a store.\n One got away though'
                                            ' and you followed him to the hideout.\n You snuck in and fought a '
                                            'bunch of bandits and their boss.\n You died in the end though.\n')
                                        file.close()
                                        save = False
                                        cont = False

                                    else:
                                        print('Finally, you defeat the Boss. Grabbing your dice from the desk,'
                                              ' you hurry back out the way you came in.')
                                        print("You can once again kill your friends at will when DM'ing.")

                                        file = open('gamehistory.txt', 'a')
                                        file.write(
                                            'In this game you hid like a coward and rode a bike into the city. You'
                                            ' stopped a couple bandits from robbing a store.\n One got away though'
                                            ' and you followed him to the hideout.\n You snuck in and fought a '
                                            'bunch of bandits and their boss.\n In the end you were victorious and'
                                            ' got back your precious D20.\n')
                                        file.close()
                                        save = False
                                        cont = False

                                elif choice == 'escape' or choice == 'Escape':
                                    print('You realize that it is easy to make another weighted D20 and all '
                                          'of this has been a waste of time.')
                                    print('Not to mention all the cuts and bruises your have. Going back out the way '
                                          'you came in, you head to the game store.')
                                    print('Time to get a new D20.')

                                    file = open('gamehistory.txt', 'a')
                                    file.write(
                                        'In this game you hid like a coward and rode a bike into the city. You'
                                        ' stopped a couple bandits from robbing a store.\n One got away though'
                                        ' and you followed him to the hideout.\n You snuck in and fought a '
                                        'bunch of bandits.\n In the end, you decided to cut your losses and'
                                        ' make a new weighted D20.\n')
                                    file.close()
                                    save = False
                                    cont = False

                            elif choice == 'rush' or choice == 'Rush':
                                print('You rush the front door. Inside are four bandits waiting to greet you.')
                                hp = thug(thug(thug(thug(hp))))

                                if hp <= 0:
                                    print("You throw everything into the fight. It isn't enough though.")
                                    print('In the end, you are beaten.')
                                    print('Thanks for playing. You should have used a medkit though.')

                                    file = open('gamehistory.txt', 'a')
                                    file.write(
                                        'In this game you hid like a coward and rode a bike into the city. You'
                                        ' stopped a couple bandits from robbing a store.\n One got away though'
                                        ' and you followed him to the hideout.\n You rushed in the front door and'
                                        ' fought a bunch of bandits.\n In the end, you were defeated.\n'
                                        ' No weighted D20 for you.\n')
                                    file.close()
                                    save = False
                                    cont = False
                                else:
                                    print("You throw everything into the fight, and make it out by the skin"
                                          " of your teeth. I suggest you use a medkit.")

                                    heal = input('Would you like to use a medkit? You have {0}.'
                                                 ' yes or no'.format(bag['Medkit']))

                                    if heal == 'yes' or heal == "Yes":
                                        if bag['Medkit'] == 1:
                                            hp = medkit(hp)
                                            bag['Medkit'] = 0
                                        else:
                                            hp = medkit(hp)
                                            bag['Medkit'] = 1

                                    print('After defeating the bandits, you search their bodies for your D20. '
                                          'DRAT! Its not there.')
                                    choice = input('Do you proceed to search the rest of the Hideout, or'
                                                   ' do you forget about it? You can always make another weighted D20.'
                                                   ' door or escape')

                                    if choice == 'door' or choice == 'Door':
                                        print('You burst through the door to see the Bandit Boss. He is sitting '
                                              'at his desk rolling YOUR dice. Glee sparkles in his eyes at the power '
                                              'he holds.')
                                        print('Angrily, you rush forward, "That is my dice!"')
                                        print('You and the Boss roll to the ground, a whirlwind of fists flying through'
                                              ' the air.')
                                        hp = boss(hp)

                                        if hp < 0:
                                            print('As you deliver the final blow, you feel a pain in your side. '
                                                  'Looking down you see a dagger protruding from your side.')
                                            print(
                                                'You reach to the desk, weakily you grab the dice. As you make your way'
                                                ' to the door, you drop to the floor.')
                                            print('Thanks for playing. You got your D20, but it cost you everything.'
                                                  ' Should have used more Medkits.')

                                            file = open('gamehistory.txt', 'a')
                                            file.write(
                                                'In this game you hid like a coward and rode a bike into the city. You'
                                                ' stopped a couple bandits from robbing a store.\n One got away though'
                                                ' and you followed him to the hideout.\n You rushed in the front door '
                                                'and fought a bunch of bandits and their boss.\n '
                                                'You died in the end though.\n')
                                            file.close()
                                            save = False
                                            cont = False

                                        else:
                                            print('Finally, you defeat the Boss. Grabbing your dice from the desk,'
                                                  ' you hurry back out the way you came in.')
                                            print("You can once again kill your friends at will when DM'ing.")

                                            file = open('gamehistory.txt', 'a')
                                            file.write(
                                                'In this game you hid like a coward and rode a bike into the city. You'
                                                ' stopped a couple bandits from robbing a store.\n One got away though'
                                                ' and you followed him to the hideout.\n You rushed in the front door'
                                                ' and fought a bunch of bandits and their boss.\n '
                                                'In the end you were victorious and got back your precious D20.\n')
                                            file.close()
                                            save = False
                                            cont = False

                                    elif choice == 'escape' or choice == 'Escape':
                                        print('You realize that it is easy to make another weighted D20 and all '
                                              'of this has been a waste of time.')
                                        print(
                                            'Not to mention all the cuts and bruises your have. Going back out the way '
                                            'you came in, you head to the game store.')
                                        print('Time to get a new D20.')

                                        file = open('gamehistory.txt', 'a')
                                        file.write(
                                            'In this game you hid like a coward and rode a bike into the city. You'
                                            ' stopped a couple bandits from robbing a store.\n One got away though'
                                            ' and you followed him to the hideout.\n You rushed in the front door and'
                                            ' fought a bunch of bandits.\n In the end, you decided to cut your losses'
                                            ' and make a new weighted D20.\n')
                                        file.close()
                                        save = False
                                        cont = False

                        elif choice == 2 or choice == 'Two' or choice == 'two':
                            print('You rush the closest bandit and tackle him to the ground. He manages get off a '
                                  'lucky punch before you know him out.')
                            hp = thug(hp)
                            print("Springing to your feet, the second bandit comes for you. He stabs at you with"
                                  " his knife. You don't dodge fast enough as the blade cuts you across the ribs."
                                  " You slightly wince in pain as you land a blow across his jaw.")
                            hp = thug(hp)
                            print("The second thug goes hits the ground hard. You riffle through their pockets,"
                                  " finding your weighted dice. The day is won. You can once again kill your friends "
                                  "at will when DM'ing.")

                            file = open('gamehistory.txt', 'a')
                            file.write('In this game you hid like a coward, rode a bike into town and stopped a'
                                       'convenience store from being robbed.\n All to get your precious dice'
                                       'back.\n')
                            file.close()
                            save = False
                            cont = False

                        else:
                            print('Invalid selection.')

                    else:
                        print('Invalid selection.')

            elif choice == 'horse' or choice == 'Horse':
                while save:
                    print('Half a mile out of town you are thrown from the horse as it falls over dead.'
                          ' Should have known no one would leave a good horse standing around.')
                    hp = thug(hp)
                    print('You stand up, dust your self and now have a decision to make.')
                    choice = input('Go back to town for the bicycle or walk the rest of the way? bicycle or walk')

                    if choice == 'bicycle' or choice == 'Bicycle':
                        print('A few hours later you pedal into the nearest city. You lost track of the bandits, '
                              'but what do bandits always do after a raid? Go drinking or rob a convenience store.')
                        choice = input('Go to the bar or convenience store? bar or store ')

                        if choice == 'bar' or choice == 'Bar':
                            choice = bar()

                            file = open('gamehistory.txt', 'a')
                            file.write('In this game you hid like a coward and chased after the bandits with a horse.\n'
                                       'Unfortunately, it died and you went back for the bicycle.\n'
                                       'Then you chose the wrong bar and died.')
                            file.close()

                            if choice == 'yes' or choice == 'Yes':
                                cont = True
                                save = False
                            else:
                                cont = False
                                save = False

                        elif choice == 'store' or choice == 'Store':
                            choice = store()

                            if choice == '1' or choice == 'one' or choice == 'One':
                                print('You rush the closest bandit and tackle him to the ground. He manages get off a '
                                      'lucky punch before you knock him out.')
                                hp = thug(hp)
                                bag['Medkit'] = 2
                                heal = input('Would you like to use a medkit? You have {0}.'
                                             ' yes or no'.format(bag['Medkit']))

                                if heal == 'yes' or heal == "Yes":
                                    hp = medkit(hp)
                                    bag['Medkit'] = 1

                                print('As you stand the other bandit drops his knife in fear of you and bolts for the'
                                      ' door.')
                                print('You chase him out of the store and down the street several blocks where he runs '
                                      'into an abandoned building. This must be their Hideout.')
                                choice = input('Do you sneak inside or rush the front door? sneak or rush')

                                if choice == 'sneak' or choice == 'Sneak':
                                    print('Sneaking around to the side, you find an open window. Climbing inside '
                                          'you spy the guy from the store.')
                                    print(
                                        'You follow him via the catwalk in the rafters where you see him enter a room. '
                                        'Stealthily, you climb down to the main floor and enter the room.')
                                    print('Inside, however, is not only the guy from the store but two of his buddies. '
                                          'They rush you as you prepare to defend yourself.')
                                    hp = thug(thug(thug(hp)))

                                    heal = input('Would you like to use a medkit? You have {0}.'
                                                 ' yes or no'.format(bag['Medkit']))

                                    if heal == 'yes' or heal == "Yes":
                                        if bag['Medkit'] == 1:
                                            hp = medkit(hp)
                                            bag['Medkit'] = 0
                                        else:
                                            hp = medkit(hp)
                                            bag['Medkit'] = 1

                                    print('After defeating the three bandits, you search their bodies for your D20. '
                                          'DRAT! Its not there.')
                                    choice = input('Do you proceed through the door at the back of the room, or'
                                                   ' do you forget about it? You can always make another weighted D20.'
                                                   ' door or escape')
                                    if choice == 'door' or choice == 'Door':
                                        print('You burst through the door to see the Bandit Boss. He is sitting '
                                              'at his desk rolling YOUR dice. Glee sparkles in his eyes at the power '
                                              'he holds.')
                                        print('Angrily, you rush forward, "That is my dice!"')
                                        print('You and the Boss roll to the ground, a whirlwind of fists flying through'
                                              ' the air.')
                                        hp = boss(hp)

                                        if hp < 0:
                                            print('As you deliver the final blow, you feel a pain in your side. '
                                                  'Looking down you see a dagger protruding from your side.')
                                            print(
                                                'You reach to the desk, weakily you grab the dice. As you make your way'
                                                ' to the door, you drop to the floor.')
                                            print('Thanks for playing. You got your D20, but it cost you everything.'
                                                  ' Should have used more Medkits.')

                                            file = open('gamehistory.txt', 'a')
                                            file.write(
                                                'In this game you hid like a coward and rode a bike into the city. You'
                                                ' stopped a couple bandits from robbing a store.\n One got away though'
                                                ' and you followed him to the hideout.\n You snuck in and fought a '
                                                'bunch of bandits and their boss.\n You died in the end though.\n')
                                            file.close()
                                            save = False
                                            cont = False

                                        else:
                                            print('Finally, you defeat the Boss. Grabbing your dice from the desk,'
                                                  ' you hurry back out the way you came in.')
                                            print("You can once again kill your friends at will when DM'ing.")

                                            file = open('gamehistory.txt', 'a')
                                            file.write(
                                                'In this game you hid like a coward and rode a bike into the city. You'
                                                ' stopped a couple bandits from robbing a store.\n One got away though'
                                                ' and you followed him to the hideout.\n You snuck in and fought a '
                                                'bunch of bandits and their boss.\n In the end you were victorious and'
                                                ' got back your precious D20.\n')
                                            file.close()
                                            save = False
                                            cont = False

                                    elif choice == 'escape' or choice == 'Escape':
                                        print('You realize that it is easy to make another weighted D20 and all '
                                              'of this has been a waste of time.')
                                        print(
                                            'Not to mention all the cuts and bruises your have. Going back out the way '
                                            'you came in, you head to the game store.')
                                        print('Time to get a new D20.')

                                        file = open('gamehistory.txt', 'a')
                                        file.write(
                                            'In this game you hid like a coward and rode a bike into the city. You'
                                            ' stopped a couple bandits from robbing a store.\n One got away though'
                                            ' and you followed him to the hideout.\n You snuck in and fought a '
                                            'bunch of bandits.\n In the end, you decided to cut your losses and'
                                            ' make a new weighted D20.\n')
                                        file.close()
                                        save = False
                                        cont = False

                                elif choice == 'rush' or choice == 'Rush':
                                    print('You rush the front door. Inside are four bandits waiting to greet you.')
                                    hp = thug(thug(thug(thug(hp))))

                                    if hp <= 0:
                                        print("You throw everything into the fight. It isn't enough though.")
                                        print('In the end, you are beaten.')
                                        print('Thanks for playing. You should have used a medkit though.')

                                        file = open('gamehistory.txt', 'a')
                                        file.write(
                                            'In this game you hid like a coward and rode a bike into the city. You'
                                            ' stopped a couple bandits from robbing a store.\n One got away though'
                                            ' and you followed him to the hideout.\n You rushed in the front door and'
                                            ' fought a bunch of bandits.\n In the end, you were defeated.\n'
                                            ' No weighted D20 for you.\n')
                                        file.close()
                                        save = False
                                        cont = False
                                    else:
                                        print("You throw everything into the fight, and make it out by the skin"
                                              " of your teeth. I suggest you use a medkit.")

                                        heal = input('Would you like to use a medkit? You have {0}.'
                                                     ' yes or no'.format(bag['Medkit']))

                                        if heal == 'yes' or heal == "Yes":
                                            if bag['Medkit'] == 1:
                                                hp = medkit(hp)
                                                bag['Medkit'] = 0
                                            else:
                                                hp = medkit(hp)
                                                bag['Medkit'] = 1

                                        print('After defeating the bandits, you search their bodies for your D20. '
                                              'DRAT! Its not there.')
                                        choice = input('Do you proceed to search the rest of the Hideout, or'
                                                       ' do you forget about it? You can always make another weighted D20.'
                                                       ' door or escape')

                                        if choice == 'door' or choice == 'Door':
                                            print('You burst through the door to see the Bandit Boss. He is sitting '
                                                  'at his desk rolling YOUR dice. Glee sparkles in his eyes at the power '
                                                  'he holds.')
                                            print('Angrily, you rush forward, "That is my dice!"')
                                            print(
                                                'You and the Boss roll to the ground, a whirlwind of fists flying through'
                                                ' the air.')
                                            hp = boss(hp)

                                            if hp < 0:
                                                print('As you deliver the final blow, you feel a pain in your side. '
                                                      'Looking down you see a dagger protruding from your side.')
                                                print(
                                                    'You reach to the desk, weakily you grab the dice. As you make your way'
                                                    ' to the door, you drop to the floor.')
                                                print(
                                                    'Thanks for playing. You got your D20, but it cost you everything.'
                                                    ' Should have used more Medkits.')

                                                file = open('gamehistory.txt', 'a')
                                                file.write(
                                                    'In this game you hid like a coward and rode a bike into the city. You'
                                                    ' stopped a couple bandits from robbing a store.\n One got away though'
                                                    ' and you followed him to the hideout.\n You rushed in the front door '
                                                    'and fought a bunch of bandits and their boss.\n '
                                                    'You died in the end though.\n')
                                                file.close()
                                                save = False
                                                cont = False

                                            else:
                                                print('Finally, you defeat the Boss. Grabbing your dice from the desk,'
                                                      ' you hurry back out the way you came in.')
                                                print("You can once again kill your friends at will when DM'ing.")

                                                file = open('gamehistory.txt', 'a')
                                                file.write(
                                                    'In this game you hid like a coward and rode a bike into the city. You'
                                                    ' stopped a couple bandits from robbing a store.\n One got away though'
                                                    ' and you followed him to the hideout.\n You rushed in the front door'
                                                    ' and fought a bunch of bandits and their boss.\n '
                                                    'In the end you were victorious and got back your precious D20.\n')
                                                file.close()
                                                save = False
                                                cont = False

                                        elif choice == 'escape' or choice == 'Escape':
                                            print('You realize that it is easy to make another weighted D20 and all '
                                                  'of this has been a waste of time.')
                                            print(
                                                'Not to mention all the cuts and bruises your have. Going back out the way '
                                                'you came in, you head to the game store.')
                                            print('Time to get a new D20.')

                                            file = open('gamehistory.txt', 'a')
                                            file.write(
                                                'In this game you hid like a coward and rode a bike into the city. You'
                                                ' stopped a couple bandits from robbing a store.\n One got away though'
                                                ' and you followed him to the hideout.\n You rushed in the front door and'
                                                ' fought a bunch of bandits.\n In the end, you decided to cut your losses'
                                                ' and make a new weighted D20.\n')
                                            file.close()
                                            save = False
                                            cont = False

                            elif choice == '2' or choice == 'Two' or choice == 'two':
                                print('You rush the closest bandit and tackle him to the ground. He manages get off a '
                                      'lucky punch before you know him out.')
                                hp = thug(hp)
                                print("Springing to your feet, the second bandit comes for you. He stabs at you with"
                                      " his knife. You don't dodge fast enough as the blade cuts you across the ribs."
                                      " You slightly wince in pain as you land a blow across his jaw.")
                                hp = thug(hp)
                                print("The second thug goes hits the ground hard. You riffle through their pockets,"
                                      " finding your weighted dice. The day is won. You can once again kill your friends "
                                      "at will when DM'ing.")

                                file = open('gamehistory.txt', 'a')
                                file.write('In this game you hid like a coward, rode a bike into town and stopped a'
                                           'convenience store from being robbed.\n All to get your precious dice'
                                           'back.\n')
                                file.close()
                                save = False
                                cont = False

                            else:
                                print('Invalid selection.')
                        else:
                            print('Invalid selection.')

                    elif choice == 'walk' or choice == 'Walk':
                        print("Later that night, you stumble into town and the bandit's trail is long gone. "
                              "You think to yourself, 'Where do bandits go this late at night?' Then it comes "
                              "to you, 'Duh, the bar or the fight club.'")
                    choice = input('Which would you like to go to? bar or club')

                    if choice == 'bar' or choice == 'Bar':
                        choice = bar()

                        file = open('gamehistory.txt', 'a')
                        file.write('In this game you hid like a coward and chased after the bandits with a horse.\n'
                                   'Unfortunately, it died and you walked to the city.\n'
                                   'Then you chose the wrong bar and died.')
                        file.close()

                        if choice == 'yes' or choice == 'Yes':
                            cont = True
                            save = False
                        else:
                            cont = False
                            save = False

                    elif choice == 'club' or choice == 'Club':
                        print('Hurrying over to the Fight Club, a guy grabs your as you enter and says, "Finally, '
                              'the new fighter is here."')
                        print('Before you can correct him the man throws you into the ring and asks if you want'
                              ' to fight two guys or three?')
                        choice = input('two or three')

                        if choice == 'two' or choice == 'Two' or '2':
                            print('As you enter the ring, two of the bandits enter opposite you.')
                            print('A bell rings and the two run toward you.')
                            hp = thug(thug(hp))
                            print('After a couple minutes, both bandits lay on the floor passed out. '
                                  'You quickly search their pockets for the D20. Nothing.')
                            print("The announcer's voice could be heard over the loud speaker introducing the"
                                  " next fighter.")
                            print("The announcer came again over the loud speaker informing that the challenger"
                                  " had forfeit.")
                            print('As you exit the ring, the man that grabbed you places something into your hand.')
                            bag['Medkit'] = 2

                            heal = input('Would you like to use a medkit? You have {0}.'
                                         ' yes or no'.format(bag['Medkit']))

                            if heal == 'yes' or heal == "Yes":
                                hp = medkit(hp)
                                bag['Medkit'] = 1

                            print("As you exit the building, you spot another bandit. Following him down the "
                                  "street, he leads you to the docks, where he meets up with two other bandits.")
                            print('You watch as the three bandits talk around a pile of crates. Eventually, the'
                                  'bandit from the Fighting Club reaches into his pocket and pulls out the D20.')
                            print('Two thoughts race through your mind.')
                            choice = input('Try and steal it from him or fight the three bandits. steal or fight')

                            if choice == 'steal' or choice == 'Steal':
                                print('Slowly you sneak around the pile of crates. Moving closer, the bandit with'
                                      'your D20 stands, inches away from you.')
                                print('It feels like hours go by as you wait for the perfect moment. Then, it '
                                      'comes. The bandit sets the D20 down on the crate right in front of you.')
                                print('Slowly, you reach out and grasp the D20.')
                                print('Quietly, you back away. When the bandits are out of sight, you rejoice in '
                                      'your victory.')
                                print('Congratulations, you got your D20 back. Now you can go dispense'
                                      'unrighteous justice on unwitting D&D players.')

                                file = open('gamehistory.txt', 'a')
                                file.write('In this game you hid like a coward, road a horse that died and walked'
                                           'to the city.\n You fought at Fight Club and won.\n Then you snuck onto'
                                           'a dock where stole your precious dice back.\n')
                                file.close()
                                save = False
                                cont = False
                            elif choice == 'fight' or choice == 'Fight':
                                print('Taking a deep breath, you rush the three bandits.')
                                hp = thug(thug(thug(hp)))

                                if hp <= 0:
                                    print('You valiantly fight the three bandits, but in the end they are too'
                                          'much for you.')
                                    print('After you fall unconscious they throw you in the ocean.')
                                    print('Thanks for playing, sorry you died like that. Should have used more'
                                          'Medkits.')

                                    file = open('gamehistory.txt', 'a')
                                    file.write(
                                        'In this game you hid like a coward, road a horse that died and walked'
                                        'to the city.\n You fought at Fight Club and won.\n Then you tried to'
                                        'fight three bandits and lost.\n'
                                    )
                                    file.close()
                                    save = False
                                    cont = False

                                else:
                                    print('You valiantly fight off the three bandits. Searching their pockets,'
                                          ' you find your D20.')
                                    print('You walk away head held high that you can once again, cheat at D&D.')

                                    file = open('gamehistory.txt', 'a')
                                    file.write(
                                        'In this game you hid like a coward, road a horse that died and walked'
                                        'to the city.\n You fought at Fight Club and won.\n Then you tried to'
                                        'fight three bandits and kicked the crap out of them, winning back'
                                        'your D20.\n'
                                    )
                                    file.close()
                                    save = False
                                    cont = False

                        elif choice == 'three' or 'Three' or '3':
                            print('As you enter the ring, three bandits enter the opposite side as you.'
                                  'A bell rings and the three bandits rush you.')
                            hp = thug(thug(thug(hp)))
                            print('You manage to dodge and evade most of the assault and one by one take'
                                  'them down.')
                            print('Once all the bandits are passed out on the floor, you seach their pockets.'
                                  'At last you find your D20. Now you can once again get all the critical'
                                  'roles you want.')

                            file = open('gamehistory.txt', 'a')
                            file.write(
                                'In this game you hid like a coward, road a horse that died and walked'
                                'to the city.\n You fought at Fight Club and won.\n'
                            )
                            file.close()
                            save = False
                            cont = False

                        else:
                            print('Invalid selection.')
                    else:
                        print('Invalid selection.')
                else:
                    print('Invalid selection.')
                    save = True

        else:
            print('Invalid selection.')
            save = True

else:
    print('Invalid selection.')
    cont = True
