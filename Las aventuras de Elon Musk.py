## IMPORT

import time
import random

## PERSONAJES

Elon = {
    "Puño": 1,
    "Patada": 1.5,
    "Vida": 100,
    "Velocidad": 0,
    "Fuerza": 1,
}   

Maduro = {
    "Puño": 10,
    "Patada": 15,
    "Vida": 100,
    "Velocidad": 1,
    "Fuerza": 1.2,
}  

msg  = ''' 
    Elon Musk Se encuentra sentado en su silla trabajando tranquilamente en su computadora, 
    hasta que recuerda que un dia el tenia que pelear contra Mark Zuckemberg, y se olvidó de esto.
    
    Dijo que iba a pelear, pero tendria que preparse antes, pero depende de ti que pelee contra un mini peleador, en este caso Nicolas Maduro, para seguir adelante y llegar a Mark Zuckemberg
    Tu elijes:
        1. Preparse"
        2. Pelear"

    Tu elijes: '''

inicio = input(msg)
