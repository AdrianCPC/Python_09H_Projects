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