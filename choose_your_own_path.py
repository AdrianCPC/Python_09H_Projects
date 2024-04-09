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
        