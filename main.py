import random

unser_wins = 0
computer_wins = 0

options = ["stein", "papier", "schere"]

while True:
    unser_input = input("Gib ein Stein/Papier/Schere oder Q um zu beenden: ").lower()
    if unser_input == "q":
        break
    
    if unser_input not in options:
        continue
        
    random_number = random.randint(0, 2)
    # stein: 0, papier: 1, schere: 2
    computer_pick = options[random_number]
    print(f"Der Computer wählt {computer_pick}.")
    
    if unser_input == "stein" and computer_pick == "schere":
        print("Du hast gewonnen! :)")
        unser_wins += 1
        
    elif unser_input == "papier" and computer_pick == "stein":
        print("Du hast gewonnen! :)")
        unser_wins += 1
        
    elif unser_input == "schere" and computer_pick == "papier":
        print("Du hast gewonnen! :)")
        unser_wins += 1
        
    elif unser_input == computer_pick:
        print ("Unentschieden.")
        
    else:
        print("Der Computer hat gewonnen.")
        computer_wins +=1

print(f"Du hast {unser_wins}x und der Computer {computer_wins}x gewonnen.")        
print("Auf Wiedersehen!")    
