print('Bienvenido a mi juego de prueba!')

playing = input('¿Quieres jugar? ')

if playing.lower() != 'yes':
    quit()

print('Esta bien! Juguemos :D')
score = 0

#Questions
answer = input('¿Qué significa CPU? ')
if answer.lower() == 'unidad central de procesamiento':
    print('Bien, hecho!')
    score += 1
else:
    print('Incorrecto!')
#Que significa CPU
#Unidad central de procesamiento
answer = input('¿Qué es una GPU?')
if answer.lower() == 'unidad procesadora de graficos':
    print('Bien, hecho')
    score +=1
else:
    print('Incorrecto!')

answer = input('¿Qué es la RAM?')
if answer.lower() == 'memoria de acceso aleatorio':
    print('Bien, hecho!')
    score += 1
else:
    print('Incorrecto')

answer = input('¿Qué es la PSU?')
if answer.lower() == 'fuente de alimentación':
    print('Bien,hecho!')
    score +=1
else:
    print('Incorrecto')
    
print('Tienes ' + str(score) + ' de preguntas correctas!')
print('Tienes ' + str((score/4)*100) + '%.')
