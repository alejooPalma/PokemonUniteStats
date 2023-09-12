from Preguntas import *
from StatsPoke import *
from StatsObjetos import *

class menu():
    def pokemon():
        print("Esta aplicacion otorga las estadisticas de los Pokemon para el juego de Pokemon"
              "Unite segun su nivel")
        print("\n1.Aegislash \n2.Azumarril\n")
        optionPokemon= int(input("Basado en la lista anterior, elija el pokemon que desea ver: \n"))
        nivelPokemon= int(input("En un rango del 1 al 15, elija el nivel del Pokemon: \n"))

        cantidadObjetos = 0
        while cantidadObjetos <3:
            cantidadObjetos =cantidadObjetos+1
            print("Tenemos una lista de objetos que se pueden equipar a los Pokemon: \n"
                  "1.Aeos Cookie\n2.Assault Vest\n3.Attack Weight")
            objeto=int(input("De la lista anterior, seleccione un objeto a equipar: \n"))
            objetoNivel= int(input("Los objetos tienen un nivel del 1 al 30 otorgando mejoras en estadisticas, elija"
                                   " un nivel: \n"))
            if objeto == 1 or objeto == 3:
                nivelStack = int(input("Que nivel de stack tiene el Pokemon, del 1 al 6:\n"))
            else:
                nivelStack = 0

            preguntas.preguntaPoke(optionPokemon, (nivelPokemon - 1), objeto, objetoNivel, nivelStack)





menu.pokemon()