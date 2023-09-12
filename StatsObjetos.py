import math
class aeosCookie(): #El objeto tiene la opcion de stack que otorga un valor adicional.
    def aeosCookie(nivelObjeto, nivelStack):
        aeosCookieHP = []
        if nivelObjeto >=1 and nivelObjeto < 10:
            stack=100
        elif nivelObjeto >=10 and nivelObjeto < 20:
            stack=150
        else:
            stack=200
        for nivel in range(1,31):
            hp = 8 * nivel
            aeosCookieHP.append(hp)

        hpFinal= (aeosCookieHP[nivelObjeto-1]) + (stack * nivelStack)
        return hpFinal

class assaultVest():
    def assaultVestHP(nivelObjeto):
        assaultVestHP=[]
        start = 18
        end = 270
        assaultVestHP.append(start)
        for nivel in range(1,15):
            hpPar = 18 * nivel
            hpImpar = 18 + 18 * nivel
            assaultVestHP.append(hpPar)
            assaultVestHP.append(hpImpar)
        assaultVestHP.append(end)
        hpFinalnivel = assaultVestHP[nivelObjeto - 1]
        return hpFinalnivel

    def assaultVestSpDef(nivelObjeto):
        assaultVestSpDef=[]
        start = 0
        end = 51
        assaultVestSpDef.append(start)
        for nivel in range(15):
            hpPar = (3.4 * nivel)
            hpImpar = (3.4 + 3.4 * nivel)
            assaultVestSpDef.append(hpPar)
            assaultVestSpDef.append(hpImpar)
        assaultVestSpDef.append(end)
        hpPorNivel = assaultVestSpDef[nivelObjeto-1]
        return hpPorNivel

class attackWeight():
    def attackWeight(nivelObjeto, nivelStack):
        attackWeightAtk = []
        if nivelObjeto >=1 and nivelObjeto < 10:
            stack=6
        elif nivelObjeto >=10 and nivelObjeto < 20:
            stack=9
        else:
            stack=12
        for nivel in range(1,31):
            atk = 0.6 * nivel
            attackWeightAtk.append(atk)

        atkFinal= (attackWeightAtk[nivelObjeto-1]) + (stack * nivelStack)
        return atkFinal



#aeosCookie.aeosCookie(10, 2)
# assaultVest.assaultVestHP(15)
# assaultVest.assaultVestSpDef(15)



