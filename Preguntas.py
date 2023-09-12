import StatsPoke
from StatsPoke import *
from StatsObjetos import *
from database_main import *

class preguntas():
    def preguntaPoke(pokemon,nivel,objeto,nivelObjeto,nivelStack):

            if pokemon == 1:
                aegislash = conexion.aegislash()
                print(list(aegislash[nivel]))
            elif pokemon == 2:
                azumaril = conexion.azumaril()
                print(list(azumaril[nivel]))

            if objeto == 1:
                if pokemon == 1:
                    listaAegislash =conexion.aegislash()
                    listaAegislash=list(listaAegislash[nivel])
                    listaAeosCookie = aeosCookie.aeosCookie(nivelObjeto,nivelStack)
                    sumaStats = ((listaAegislash[1])+ (listaAeosCookie) + nivelStack)-1
                    listaAegislash[1]=sumaStats
                    print(listaAegislash)
                    return listaAegislash
                elif pokemon == 2:
                    listaAzumaril = conexion.azumaril()
                    listaAzumaril = list(listaAzumaril[nivel])
                    listaAeosCookie = aeosCookie.aeosCookie(nivelObjeto,nivelStack)
                    sumaStats = ((listaAzumaril[1])+ (listaAeosCookie) + nivelStack)-1
                    listaAzumaril[1] = sumaStats
                    print(listaAzumaril)
                    return listaAzumaril

            elif objeto == 2:
                if pokemon == 1:
                    listaAegislash = conexion.aegislash()
                    listaAegislash = list(listaAegislash[nivel])
                    listaHP = assaultVest.assaultVestHP(nivelObjeto)
                    listaSpDef= assaultVest.assaultVestSpDef(nivelObjeto)
                    sumaStatsHp = (listaAegislash[1])+ (listaHP)
                    sumaStatsSpDef= (listaAegislash[5])+ (listaSpDef)
                    listaAegislash[1]=sumaStatsHp
                    listaAegislash[5]=sumaStatsSpDef
                    print(listaAegislash)
                    return listaAegislash
                elif pokemon == 2:
                    listaAzumaril = conexion.azumaril()
                    listaAzumaril = list(listaAzumaril[nivel])
                    listaHP = assaultVest.assaultVestHP(nivelObjeto)
                    listaSpDef = assaultVest.assaultVestSpDef(nivelObjeto)
                    sumaStatsHp = (listaAzumaril[1]) + (listaHP)
                    sumaStatsSpDef = (listaAzumaril[5]) + (listaSpDef)
                    listaAzumaril[1] = sumaStatsHp
                    listaAzumaril[5] = sumaStatsSpDef
                    print(listaAzumaril)
                    return listaAzumaril

            elif objeto == 3:
                if pokemon == 1:
                    listaAegislash = conexion.aegislash()
                    listaAegislash = list(listaAegislash[nivel])
                    listaAttackWeight = attackWeight.attackWeight(nivelObjeto,nivelStack)
                    sumaStats = ((listaAegislash[2])+ (listaAttackWeight) + nivelStack)-1
                    listaAegislash[2]=sumaStats
                    print(listaAegislash)
                    return listaAegislash
                elif pokemon == 2:
                    listaAzumaril = conexion.azumaril()
                    listaAzumaril = list(listaAzumaril[nivel])
                    listaAeosCookie = attackWeight.attackWeight(nivelObjeto,nivelStack)
                    sumaStats = ((listaAzumaril[2])+ (listaAeosCookie) + nivelStack)-1
                    listaAzumaril[2] = sumaStats
                    print(listaAzumaril)
                    return listaAzumaril


#preguntas.preguntaPoke(1, 1,3,1, 1)