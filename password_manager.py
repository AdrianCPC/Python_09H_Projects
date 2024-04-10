main_pwd = input("¿Cuál es la contraseña principal?")

def view():
    pass

def add():
    name = input("Nombre de cuenta: ")
    pwd = input("Contraseña: ")
    
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("¿Le gustaria adicionar una nueva contraseña o ver las existentes (ver,adicionar)?, click en Q para salir. ")
    
    if mode == "Q":
        break
    
    if mode == "ver":
        view()
    elif mode == "adicionar":
        add()
    else:
        print("Modo invalido. ")
        continue

