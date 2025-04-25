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

EntrenamientoOPelea = input("Quieres entrenarle a Elon antes de pelear contra maduro? : ")


if(EntrenamientoOPelea == "pelea"):
    
 while True: 

        if(Elon["Fuerza"] > 1.5 or Elon["Velocidad"] > 100 or Elon["Puño"] > 25 or Elon["Patada"]):
            break

        # Eleccion
        
        DominadaOSentadillas = input("Quieres hacer ?: ")

    

## PELEA
    
while True:

    if(EntrenamientoOPelea == "No" or Elon["Fuerza"] > 1.5 or Elon["Velocidad"] > 100 or Elon["Puño"] > 25 or Elon["Patada"]):

        # Condicion para el final

        if(Elon["Vida"] < 0 or Maduro["Vida"] < 0):
            break
        
        # Patada o Puño

        eleccion = input ("Tienes que elejir entre dar una Patada o un Puño: ")

        # Golpe

        if(eleccion == "Patada"):
            Maduro["Vida"] -= Elon["Patada"]
        if(eleccion == "Puño"): 
            Maduro["Vida"] -= Elon["Puño"] 
        
        # Resultados Maduro

        print(f"Maduro: {Maduro}")

        # Golpe Maduro & Resultados Elon

        Elon["Vida"] -= random.choice([Maduro["Patada"], Maduro["Puño"]])

        print(f"Elon: {Elon}")