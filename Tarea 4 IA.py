from random import randint
from math import inf

def ev_peso (solu: str, a: list) ->float:
    peso = 0
    for j in range(len(solu)): 
        peso += a[j]*int(solu[j])
    return peso

def gen_solu(a:list, peso_max: int)->str:
    e=len(a)
    solucion=""
    for j in range(e):
        solucion += str(randint(0,1))
    while ev_peso(solucion, a)>peso_max:
        solucion = ""
        for j in range(e): 
            solucion += str(randint(0, 1))
    return solucion
    
def ev_benef(solu: str, i: list)->float: 
    beneficio = 0
    for j in range(len(solu)): 
        beneficio += b[j]*int(sol[j])
    return beneficio

def seleccion(pobl: list, i: list): 
    h_muestra = 10
    solucion = ""
    for j in range(h_muestra): 
        muestra = pobl[randint(0, len(pobl)-1)]
        if ev_benef(muestra, i) > ev_benef(solucion, i): 
            solucion = muestra
    return solucion
    
def cruce(papa, mama, a: list, peso_max: int, proba = 90): 
    if randint(1, 100) <= proba: 
        e = len(papa)//2
        n1 = papa[:e] + mama[e:]
        n2 = mama[:e] + papa[e:]
        if ev_peso(n1, a) > peso_max: 
            n1 = papa
        if ev_peso(n2, a) > peso_max: 
            n2 = mama
        return n1, n2
    return papa, mama

def mutacion(solu: str, a: list, peso_max: int, proba = 5): 
    if randint(1, 100) <= proba: 
        h = randint(0, len(solu)-1)
        mutante = sol[:h]
        mutante += "0" if solu[h] == "1" else "1"
        mutante += solu[h+1:]
        if ev_peso(solu, a) <= peso_max: 
            return mutante
    return solu
    
def genetico(peso_max: int, i: list, a: list, n_pob = 100, n_gen = 10): 
    poblacion = list()
    for k in range(k_pob): 
        poblacion.append(gen_solu(a, peso_max))
    mejor_solu = ""
    mejor_valor = -inf
    for o in range(m_gen): 
        mejor_solu = ""
        mejor_valor = -inf
        seleccionados = [seleccion(poblacion, i) for j in range(k_pob)]
        hijos = list()
        for j in range(0, k_pob, 2): 
            papa, mama = seleccionados[j], seleccionados[j+1]
            for hijo in cruce(papa, mama, a, peso_max): 
                mutacion(hijo, a, peso_max)
                hijos.append(hijo)
                if ev_benef(hijo, i) > mejor_valor: 
                    mejor_solu = hijo
                    mejor_valor = ev_benef(hijo, i)
        poblacion = hijos
    valor = 0
    for u in poblacion: 
        valor += ev_benef(u, beneficios)
    valor /= len(poblacion)
    print("VALOR PROMEDIO: "+str(valor))
    return (mejor_solu, mejor_valor)
    
if __name__ == "__main__":
    peso_maxi = 269
    k_pob = 100
    m_gen = 0
    beneficios = [100, 94, 506, 416, 992, 649, 237, 457, 815, 446, 422, 791, 359, 667, 598, 7, 544, 334, 766, 700]
    pesos = [995, 485, 326, 248, 421, 322, 795, 43, 845, 955, 252, 9, 901, 122, 94, 738, 574, 715, 882, 72]
    solucion, v = genetico(peso_maxi, beneficios, pesos, k_pob, m_gen)
    print("MEJOR SOLUCION: "+solucion)
    print("MEJOR VALOR: "+str(v))