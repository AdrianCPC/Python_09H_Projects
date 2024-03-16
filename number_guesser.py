import random 

top_range = input('Digita un número: ')

if top_range.isdigit():
    top_range = int(top_range)
    
    if top_range <= 0:
        print('Por favor, digita un número más grande que 0, la proxima vez!')
        quit()
else:
    print('Por favor, digita un número la proxima vez!')
    quit()
    
random_number = random.randint(0,top_range)
print(random_number)

while True:
    user_guess = input('Adivina el número: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Por favor, digita un número la proxima vez!')
        continue
    
    if user_guess == random_number:
        print('Adivinaste!')
        break
    else:
        print('Te equivocaste!')
