import random

user_wins = 0
computer_wins = 0

options = ["piedra","papel","tijera"]

while True:
    user_input = input("Escribe pierda/papel/tijera o Q para salir: ").lower()
    if user_input == "q":
        break
    
    if user_input not in ["piedra","papel","tijera"]:
        continue
    
    random_number = random.randint(0,2)
    #piedra: 0, papel: 1, tijera: 2
    computer_pick = options[random_number]
    print("La computadora selecciono", computer_pick + ".")
    
    if user_input == "piedra" and computer_pick == "tijera":
        print("Has ganado")
        user_wins += 1
        continue
    
print("Adios!")