name = input("Escribe tú nombre: ")
print("Bienvenido", name, " a esta aventura!")

answer = input("Estas en el camino en mal estado, al final del mismo puedes ir tanto a la izquierda o derecha. ¿Cuál camino te gustaria elegir? ").lower()

if answer == "izquierda":
    answer = input("Ve al rio, camina alrededor o cruza nadando: ")
    
    if answer == "nadar":
        print("Nadaste a traves del rio y fuiste comido por un cocodrilo. ")
    elif answer == "caminar":
        print("Caminaste muchos kilometros, alrededor del rio y perdiste el juego.")
    else:
        print("Sin opción valida. Perdiste!.")
        
elif answer == "derecha":
    answer = input("Ve al puente, parece inestable, ¿Quieres cruzarlo o devolverte?.")
    if answer == "volver":
        print("Vuelves y pierdes.")
    elif answer == "cruzar":
        answer = input("Cruzas el puente y conoces un extraño. Les hablas a ellos(si/no)? ")
        
        if answer == "si":
            print("Le hablas al extraño y ellos te dan oro, Ganaste!.")
        
        elif answer == "no":
            print("Ignoras al extraño y ellos se ofenden. Perdiste!.")
    else:
        print("No es una opcion valida. Perdiste.")
        
else:
    print("No es una opcion valida. Perdiste!.")
print("Gracias por intentarlo", name)