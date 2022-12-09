import random


Knight = False
Archer = False
Mage = False

choices = [1, 2, 3]

enemies = ["Giant Spider", "Himerra", "Skeleton Knight"]

# LIST STATTS OF CHARACTERS

HIM_STATS = [135, 80, 75]
SPD_STATS = [125, 70, 45]
SK_STATS = [105, 85, 65]

K_STATS = [120, 75, 50]
A_STATS = [100, 85, 50]
M_STATS = [90, 100, 25]

HP = 1

print("welcome")
print()
print("\n1.Knigh \n2.Archer \n3.Mage")
print()

while HP != 0:

    user_ = int(input("Choice fighte: "))
    print()

    if user_ == 1:
        Knight = True
        print("HP:", K_STATS[0], "\nATT:", K_STATS[1], "\nDEF:", K_STATS[2])
        print()
        print("Great you choice Knight\nWish you luck...")
        HP += K_STATS[0] - 1
    elif user_ == 2:
        Archer = True
        print("HP:", A_STATS[0], "\nATT:", A_STATS[1], "\nDEF:", A_STATS[2])
        print()
        print("Great you choice Archer\nWish you luck...")
        HP += A_STATS[0] - 1
    elif user_ == 3:
        Mage = True
        print("HP:", M_STATS[0], "\nATT:", M_STATS[1], "\nDEF:", M_STATS[2])
        print()
        print("Great you choice Mage\nWish you luck...")
        HP += M_STATS[0] - 1
    else:
        print("Not a choice... try again")
        continue

    if user_ not in choices:
        print("Error")

    else:
        print()
        print("You are walking in the forest.. suddenly you are in a crossroad ...")
        print(
            "\n1.Front intro the dark forest.  \n2.Left you see in the distance leak  \n3.Right you see graveyard"
        )
        print()

        user_ = int(input("Where do you go: "))

        if user_ == 1:
            print("You walk with confident like you are not afraid of the dark..")
            print("In the distantnce intro the dark someting is moving")
            enemy = random.choice(enemies)
            print(f"{enemy} hit you in a surprice..")
            if Knight:
                if enemy == enemies[1]:
                    K_STATS[0] = K_STATS[0] - (
                        K_STATS[0] - HIM_STATS[1] - (K_STATS[2] / 10)
                    )
                    print("HP:", K_STATS[0])
                elif enemy == enemies[0]:
                    K_STATS[0] = K_STATS[0] - (
                        K_STATS[0] - SPD_STATS[1] - (K_STATS[2] / 10)
                    )
                    print("HP:", K_STATS[0])
                elif enemy == enemies[2]:
                    K_STATS[0] = K_STATS[0] - (
                        K_STATS[0] - SK_STATS[1] - (K_STATS[2] / 10)
                    )
                    print("HP:", K_STATS[0])
            elif Archer:
                if enemy == enemies[1]:
                    A_STATS[0] = A_STATS[0] - (
                        A_STATS[0] - HIM_STATS[1] - (A_STATS[2] / 10)
                    )
                    print("HP:", A_STATS[0])
                elif enemy == enemies[0]:
                    A_STATS[0] = A_STATS[0] - (
                        A_STATS[0] - SPD_STATS[1] - (A_STATS[2] / 10)
                    )
                    print("HP:", A_STATS[0])
                elif enemy == enemies[2]:
                    A_STATS[0] = A_STATS[0] - (
                        A_STATS[0] - SK_STATS[1] - (A_STATS[2] / 10)
                    )
                    print("HP:", A_STATS[0])
            else:
                if enemy == enemies[1]:
                    M_STATS[0] = M_STATS[0] - (
                        M_STATS[0] - HIM_STATS[1] - (M_STATS[2] / 10)
                    )
                    print("HP:", M_STATS[0])
                elif enemy == enemies[0]:
                    M_STATS[0] = M_STATS[0] - (
                        M_STATS[0] - SPD_STATS[1] - (M_STATS[2] / 10)
                    )
                    print("HP:", M_STATS[0])
                elif enemy == enemies[2]:
                    M_STATS[0] = M_STATS[0] - (
                        M_STATS[0] - SK_STATS[1] - (M_STATS[2] / 10)
                    )
                    print("HP:", M_STATS[0])
            print("YOU STAPE BACK..... You have a choice to Fight or Run for it")
            print("1.Fight Back \n2.RUN")
            user_ = int(input("What do you choice: "))
            if user_ == 1:
                print(
                    "You strike back you take out you sword and hit it right in the kisser"
                )
                if Knight:
                    if enemy == enemies[1]:
                        HIM_STATS[0] = HIM_STATS[0] - (
                            HIM_STATS[0] - K_STATS[1] - (HIM_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", HIM_STATS[0])

                    elif enemy == enemies[0]:
                        SPD_STATS[0] = SPD_STATS[0] - (
                            SPD_STATS[0] - K_STATS[1] - (SPD_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SPD_STATS[0])

                    elif enemy == enemies[2]:
                        SK_STATS[0] = SK_STATS[0] - (
                            SK_STATS[0] - K_STATS[1] - (SK_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SK_STATS[0])
                elif Archer:
                    if enemy == enemies[1]:
                        HIM_STATS[0] = HIM_STATS[0] - (
                            HIM_STATS[0] - A_STATS[1] - (HIM_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", HIM_STATS[0])

                    elif enemy == enemies[0]:
                        SPD_STATS[0] = SPD_STATS[0] - (
                            SPD_STATS[0] - A_STATS[1] - (SPD_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SPD_STATS[0])

                    elif enemy == enemies[2]:
                        SK_STATS[0] = SK_STATS[0] - (
                            SK_STATS[0] - A_STATS[1] - (SK_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SK_STATS[0])
                else:
                    if enemy == enemies[1]:
                        HIM_STATS[0] = HIM_STATS[0] - (
                            HIM_STATS[0] - M_STATS[1] - (HIM_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", HIM_STATS[0])

                    elif enemy == enemies[0]:
                        SPD_STATS[0] = SPD_STATS[0] - (
                            SPD_STATS[0] - M_STATS[1] - (SPD_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SPD_STATS[0])

                    elif enemy == enemies[2]:
                        SK_STATS[0] = SK_STATS[0] - (
                            SK_STATS[0] - M_STATS[1] - (SK_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SK_STATS[0])

            elif user_ == 2:
                print("You are a FIGHTER this is not a choice... or never mine RUN..")
                print()
                print(f"The {enemy} attacks you in back.. you are dead.. ")
                print()
                print("...Game Over...")
            else:
                print("Not a choice champ..")
                print(f"{enemy} attack you in a surprice.. you are DEAD champ.. ")
                quit()
        elif user_ == 2:
            print("You walk with confident like you can sweam..")
            print("In the distantnce intro the dark someting is moving")
            enemy = random.choice(enemies)
            print(f"{enemy} hit you in a surprice..")
            if Knight:
                if enemy == enemies[1]:
                    K_STATS[0] = K_STATS[0] - (
                        K_STATS[0] - HIM_STATS[1] - (K_STATS[2] / 10)
                    )
                    print("HP:", K_STATS[0])
                elif enemy == enemies[0]:
                    K_STATS[0] = K_STATS[0] - (
                        K_STATS[0] - SPD_STATS[1] - (K_STATS[2] / 10)
                    )
                    print("HP:", K_STATS[0])
                elif enemy == enemies[2]:
                    K_STATS[0] = K_STATS[0] - (
                        K_STATS[0] - SK_STATS[1] - (K_STATS[2] / 10)
                    )
                    print("HP:", K_STATS[0])
            elif Archer:
                if enemy == enemies[1]:
                    A_STATS[0] = A_STATS[0] - (
                        A_STATS[0] - HIM_STATS[1] - (A_STATS[2] / 10)
                    )
                    print("HP:", A_STATS[0])
                elif enemy == enemies[0]:
                    A_STATS[0] = A_STATS[0] - (
                        A_STATS[0] - SPD_STATS[1] - (A_STATS[2] / 10)
                    )
                    print("HP:", A_STATS[0])
                elif enemy == enemies[2]:
                    A_STATS[0] = A_STATS[0] - (
                        A_STATS[0] - SK_STATS[1] - (A_STATS[2] / 10)
                    )
                    print("HP:", A_STATS[0])
            else:
                if enemy == enemies[1]:
                    M_STATS[0] = M_STATS[0] - (
                        M_STATS[0] - HIM_STATS[1] - (M_STATS[2] / 10)
                    )
                    print("HP:", K_STATS[0])
                elif enemy == enemies[0]:
                    M_STATS[0] = M_STATS[0] - (
                        M_STATS[0] - SPD_STATS[1] - (M_STATS[2] / 10)
                    )
                    print("HP:", M_STATS[0])
                elif enemy == enemies[2]:
                    M_STATS[0] = M_STATS[0] - (
                        M_STATS[0] - SK_STATS[1] - (M_STATS[2] / 10)
                    )
                    print("HP:", M_STATS[0])
            print("YOU STAPE BACK..... You have a choice to Fight or Run for it")
            print("1.Fight Back \n2.RUN")
            user_ = int(input("What do you choice: "))
            if user_ == 1:
                print(
                    "You strike back you take out you sword and hit it right in the kisser"
                )
                if Knight:
                    if enemy == enemies[1]:
                        HIM_STATS[0] = HIM_STATS[0] - (
                            HIM_STATS[0] - K_STATS[1] - (HIM_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", HIM_STATS[0])

                    elif enemy == enemies[0]:
                        SPD_STATS[0] = SPD_STATS[0] - (
                            SPD_STATS[0] - K_STATS[1] - (SPD_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SPD_STATS[0])

                    elif enemy == enemies[2]:
                        SK_STATS[0] = SK_STATS[0] - (
                            SK_STATS[0] - K_STATS[1] - (SK_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SK_STATS[0])
                elif Archer:
                    if enemy == enemies[1]:
                        HIM_STATS[0] = HIM_STATS[0] - (
                            HIM_STATS[0] - A_STATS[1] - (HIM_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", HIM_STATS[0])

                    elif enemy == enemies[0]:
                        SPD_STATS[0] = SPD_STATS[0] - (
                            SPD_STATS[0] - A_STATS[1] - (SPD_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SPD_STATS[0])

                    elif enemy == enemies[2]:
                        SK_STATS[0] = SK_STATS[0] - (
                            SK_STATS[0] - A_STATS[1] - (SK_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SK_STATS[0])
                else:
                    if enemy == enemies[1]:
                        HIM_STATS[0] = HIM_STATS[0] - (
                            HIM_STATS[0] - M_STATS[1] - (HIM_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", HIM_STATS[0])

                    elif enemy == enemies[0]:
                        SPD_STATS[0] = SPD_STATS[0] - (
                            SPD_STATS[0] - M_STATS[1] - (SPD_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SPD_STATS[0])

                    elif enemy == enemies[2]:
                        SK_STATS[0] = SK_STATS[0] - (
                            SK_STATS[0] - M_STATS[1] - (SK_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SK_STATS[0])
            elif user_ == 2:
                print("You are a FIGHTER this is not a choice... or never mine RUN..")
                print()
                print(f"The {enemy} attacks you in back.. you are dead.. ")
                print()
                print("...Game Over...")
            else:
                print("Not a choice champ..")
                print(f"{enemy} attack you in a surprice.. you are DEAD champ.. ")
                quit()
        elif user_ == 3:
            print(
                "You walk with confident like it's not a night and this is not a graveyard .."
            )
            print("In the distantnce intro the dark someting is moving")
            enemy = random.choice(enemies)
            print()
            print(f"{enemy} hit you in a surprice..")
            if Knight:
                if enemy == enemies[1]:
                    K_STATS[0] = K_STATS[0] - (
                        K_STATS[0] - HIM_STATS[1] - (K_STATS[2] / 10)
                    )
                    print("HP:", K_STATS[0])
                elif enemy == enemies[0]:
                    K_STATS[0] = K_STATS[0] - (
                        K_STATS[0] - SPD_STATS[1] - (K_STATS[2] / 10)
                    )
                    print("HP:", K_STATS[0])
                elif enemy == enemies[2]:
                    K_STATS[0] = K_STATS[0] - (
                        K_STATS[0] - SK_STATS[1] - (K_STATS[2] / 10)
                    )
                    print("HP:", K_STATS[0])
            elif Archer:
                if enemy == enemies[1]:
                    A_STATS[0] = A_STATS[0] - (
                        A_STATS[0] - HIM_STATS[1] - (A_STATS[2] / 10)
                    )
                    print("HP:", A_STATS[0])
                elif enemy == enemies[0]:
                    A_STATS[0] = A_STATS[0] - (
                        A_STATS[0] - SPD_STATS[1] - (A_STATS[2] / 10)
                    )
                    print("HP:", A_STATS[0])
                elif enemy == enemies[2]:
                    A_STATS[0] = A_STATS[0] - (
                        A_STATS[0] - SK_STATS[1] - (A_STATS[2] / 10)
                    )
                    print("HP:", A_STATS[0])
            else:
                if enemy == enemies[1]:
                    M_STATS[0] = M_STATS[0] - (
                        M_STATS[0] - HIM_STATS[1] - (M_STATS[2] / 10)
                    )
                    print("HP:", M_STATS[0])
                elif enemy == enemies[0]:
                    M_STATS[0] = M_STATS[0] - (
                        M_STATS[0] - SPD_STATS[1] - (M_STATS[2] / 10)
                    )
                    print("HP:", M_STATS[0])
                elif enemy == enemies[2]:
                    M_STATS[0] = M_STATS[0] - (
                        M_STATS[0] - SK_STATS[1] - (M_STATS[2] / 10)
                    )
                    print("HP:", M_STATS[0])
            print("YOU STAPE BACK..... You have a choice to Fight or Run for it")
            print("1.Fight Back \n2.RUN")
            user_ = int(input("What do you choice: "))
            if user_ == 1:
                print(
                    "You strike back you take out you sword and hit it right in the kisser"
                )
                if Knight:
                    if enemy == enemies[1]:
                        HIM_STATS[0] = HIM_STATS[0] - (
                            HIM_STATS[0] - K_STATS[1] - (HIM_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", HIM_STATS[0])

                    elif enemy == enemies[0]:
                        SPD_STATS[0] = SPD_STATS[0] - (
                            SPD_STATS[0] - K_STATS[1] - (SPD_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SPD_STATS[0])

                    elif enemy == enemies[2]:
                        SK_STATS[0] = SK_STATS[0] - (
                            SK_STATS[0] - K_STATS[1] - (SK_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SK_STATS[0])
                elif Archer:
                    if enemy == enemies[1]:
                        HIM_STATS[0] = HIM_STATS[0] - (
                            HIM_STATS[0] - A_STATS[1] - (HIM_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", HIM_STATS[0])

                    elif enemy == enemies[0]:
                        SPD_STATS[0] = SPD_STATS[0] - (
                            SPD_STATS[0] - A_STATS[1] - (SPD_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SPD_STATS[0])

                    elif enemy == enemies[2]:
                        SK_STATS[0] = SK_STATS[0] - (
                            SK_STATS[0] - A_STATS[1] - (SK_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SK_STATS[0])
                else:
                    if enemy == enemies[1]:
                        HIM_STATS[0] = HIM_STATS[0] - (
                            HIM_STATS[0] - M_STATS[1] - (HIM_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", HIM_STATS[0])

                    elif enemy == enemies[0]:
                        SPD_STATS[0] = SPD_STATS[0] - (
                            SPD_STATS[0] - M_STATS[1] - (SPD_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SPD_STATS[0])

                    elif enemy == enemies[2]:
                        SK_STATS[0] = SK_STATS[0] - (
                            SK_STATS[0] - M_STATS[1] - (SK_STATS[2] / 10)
                        )
                        print(f"{enemy} HP: ", SK_STATS[0])
            elif user_ == 2:
                print("You are a FIGHTER this is not a choice... or never mine RUN..")
                print()
                print(f"The {enemy} attacks you in back.. you are dead.. ")
                print()
                print("...Game Over...")
            else:
                print("Not a choice champ..")
                print(f"{enemy} attack you in a surprice.. you are DEAD champ.. ")
