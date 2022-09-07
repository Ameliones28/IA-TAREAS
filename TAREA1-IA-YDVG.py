###Yuvia Damaris Vargas González 1869708
###Ejercicio 1:
    ###Función que calcule el cubo de un número entero. Ejemplo: cubo(2) devuelve el valor de 8.
def cubo(num1):
    c = num1 * num1 * num1
    return print("El cubo de", num1, "es", c)

cubo(6)


###Ejercicio 2:
    ###Función que calcule el valor factorial de un número entero positivo. Ejemplo: factorial(4) devuelve el valor de 24.
def factorial(num2):
    if num2 == 1:
        return 1
    else:
        return(num2 * factorial(num2 - 1))

print(factorial(7))



###Ejercicio 3:
    ###Función que cuente cuantas veces se repite el patrón en una cadena de caracteres incluyendo si se superponen. Ejemplo: cuenta_patron(('ab'), ('abcebabf'')) debería regresar el valor de 2, y cuenta_patrón(('aba'), ('gabababa')) debería regresar el valor de 3. 
def repeticion(patron, cadena):
    r = cadena.count(patron)
    return print("se repite", r, "veces")

cadena = 'g a b a b a b a'
patron = 'a b a'
repeticion(patron, cadena)


###Ejercicio 4:
    ###Función que devuelva la parte de un árbol de acuerdo con su índice.
        ###Ejemplo: El árbol anterior se puede representar en Python por [[[1, 2], 3], [4, [5, 6]], 7, [8, 9, 10]]. Por lo que, para seleccionar el número nueve de esa estructura deberíamos poder hacerlo de la siguiente forma arbol_ref(tree, (3,1)), donde ‘tree’ representa la tupla con los datos del árbol y (3,1) la rama y el lugar que ocupa ese valor en esa rama. Tomemos en cuenta que estamos tomando índices iniciando en 0. Otro ejemplo sería obtener el 6, por lo que la forma de hacerlo sería arbol_ref(tree, (1,1,1)). También hay que tener en cuenta que no es necesario que siempre devuelva una hoja, puede devolver una parte del árbol, ejemplo: arbol_ref(tree, (0,)) debería devolver ((1,2),3). 
def profundidad(exp):
    p=0
    n=0
    for i in range(len(exp)):
        if exp[i] == '(':
            p = p + 1
            if n < p:
                n = p
        elif exp[i] == ')':
            p = p - 1
    if p == 0:
        return print("La profundidad es de", n)
    else:
        return print("Funcion no valida")


profundidad('(3(5+6))')

###Ejercicio 5:
    ###Función que desarrolle una expresión algebraica. Ejemplo: (2 * (x + 1) * (y + 3)), debería devolver: ((2 * x * y) + (2 * x * 3) + (2 * 1 * y) + (2 * 1 * 3)) o su versión simplificada ((2 * x * y) + (6 * x) + (2 * y) + 6)). 
        
        from sympy import expand


        def expresion(num3):
            return expand(num3)

        print (expresion("(2*(x+1)*(y+3))"));