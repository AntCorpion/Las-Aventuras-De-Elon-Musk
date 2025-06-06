## IMPORT

import time
import random

## PERSONAJES

Elon = {
    "Puño": 1,
    "Patada": 1.5,
    "Vida": 100,
    "Velocidad": 1,
    "Fuerza": 1,
    "Energia":100,
    "Nombre": "Elon",
}   

Mark = {
    "Puño": 10,
    "Patada": 15,
    "Vida": 100,
    "Velocidad": 1,
    "Fuerza": 1.2,
    "Energia":100,
    "Nombre": "Mark",

}  

def mensajes1(personaje):
    if personaje["Vida"]>70:
        msg = '''
     se siente fuerte y se rie de su oponente 
    '''
        
    if personaje["Vida"]<70:
        msg = '''
    Elon mira desde lejos una luz blanca 
        '''
    return msg

def mensajes2(personaje):
    if personaje["Vida"]>70:
        msg = '''
    Mark no baja su mirada
    '''
        
    if personaje["Vida"]<70:
        msg = '''
    Mark parece estar cansado
    '''
    return msg
            
def lucha(personaje1,personaje2):
    DesicionMark = random.choice(["Patada","Puño"])
    print(DesicionMark)

    personaje1["Vida"] -= personaje2[DesicionMark] * personaje2["Velocidad"]
    
    print(Mark)
    print(Elon)

msg  = ''' 
    Elon se encuentra sentado en su silla trabajando tranquilamente en su computadora, 
    hasta que recuerda que un dia el tenia que pelear contra Mark, y entonces se puso las pilas.
    
    Dijo que iba a pelear, pero tendria que preparse antes, pero depende de ti que pelee contra un mini peleador, en este caso Nicolas Maduro, para seguir adelante y llegar a Mark Zuckemberg
    Tu elijes:

        1. "Preparse"
        2. "Pelear"

    Tu elijes: '''

inicio = input(msg)

while Elon["Vida"] > 0: 

    msg = '''
        Elon se siente abrumado por el ensordecedor ruido de la hinchada del publico,
        pero no puede distraerse, debe de empezar a pelear contra su contrincante, Mark
        
        Es hora de Elonear, dijo Elon antes de hacer su primer ataque
            
            1. "Patada"
            2. "Puño"
            
        Tu elijes: '''

    DesicionElon = input(msg)


    print("        Aqui viene mark!")

    lucha(Elon,Mark)
    print(mensajes1(Elon))
    lucha(Mark,Elon)
    print(mensajes2(Mark))