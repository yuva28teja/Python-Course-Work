p1 = input("Enter the player-1: ")
p2 = input("Enter the player-2: ")

winning_point = 100
p1_sc = 0
p2_sc = 0

# Corrected snakes and ladders (77, not 770)
snakes = {7:1, 18:8, 35:14, 56:40, 77:50, 99:2}
ladders = {5:30, 9:21, 25:45, 48:88, 66:97, 80:94}

import random as ra

while p1_sc < winning_point and p2_sc < winning_point:
    
    # Player 1 turn
    p1_status = input(f"{p1}, continue the game? (y/n): ")
    if p1_status == "y":
        p1_dice = ra.randint(1, 6)
        print(f"{p1}: Dice score = {p1_dice}")
        p1_sc += p1_dice

        # Check snake or ladder
        if p1_sc in snakes:
            p1_sc = snakes[p1_sc]
            print(f"{p1}: Bitten by a snake! New score: {p1_sc}")
        elif p1_sc in ladders:
            p1_sc = ladders[p1_sc]
            print(f"{p1}: Climbed a ladder! New score: {p1_sc}")

        print(f"{p1}: Total score = {p1_sc}")

        if p1_sc >= winning_point:
            print(f"Congratulations {p1}, you win the game!")
            break

    else:
        print(f"{p2} wins the game because {p1} quit!")
        break

    # Player 2 turn
    p2_status = input(f"{p2}, continue the game? (y/n): ")
    if p2_status == "y":
        p2_dice = ra.randint(1, 6)
        print(f"{p2}: Dice score = {p2_dice}")
        p2_sc += p2_dice

        # Check snake or ladder
        if p2_sc in snakes:
            p2_sc = snakes[p2_sc]
            print(f"{p2}: Bitten by a snake! New score: {p2_sc}")
        elif p2_sc in ladders:
            p2_sc = ladders[p2_sc]
            print(f"{p2}: Climbed a ladder! New score: {p2_sc}")

        print(f"{p2}: Total score = {p2_sc}")

        if p2_sc >= winning_point:
            print(f"Congratulations {p2}, you win the game!")
            break

    else:
        print(f"{p1} wins the game because {p2} quit!")
        break
