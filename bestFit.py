def bestFit(memory : str, index : int, req : int ): #El indice se manejara como una lista en python que empieza en 0
    base = 0
    limite = 1
    espacio_restante_actual = None
    mejor_base = -1
    mejor_espacio_restante = -1
    try:
        eval(memory) # Hacemos una prueba de la validez del formato de la memoria
    except SyntaxError as e:
        return print('No se puede transformar el archivo, problema de sintaxis, error: ' + str(e))
    memoria_recibida_formateada = eval(memory)
    cabeza = index
    if type(memoria_recibida_formateada) is not list:
        return print('La tabla de memoria recibida no es una lista por lo que no puede ser utilizada')
        
    elif len(memoria_recibida_formateada) == 0:
        return print('La tabla de memoria recibida no tiene valores con los cual operar')
         
    elif type(memoria_recibida_formateada[0]) is not tuple:
        return print('La tabla de memoria recibida no es una lista de tuplas por lo cual no puede ser utilizada')
    elif index < 0:
        return print('El index o cabeza de la tabla no puede ser negativo, por lo tanto no es posible utilizarlo')
    elif req <= 0:
        return print('El valor requerido no puede ser un numero negativo o 0, no se puede utilizar')
    
    while(True):
        tupla_actual = memoria_recibida_formateada[cabeza]
        limite_actual = tupla_actual[limite] 
        base_actual = tupla_actual[base]
        if mejor_base == base_actual:
            break
        if  limite_actual > req:
            espacio_restante_actual = limite_actual - req
            if mejor_espacio_restante == -1: # Verificamos si es la primera iteracion 
                mejor_espacio_restante = espacio_restante_actual
                mejor_base = base_actual
            else:
                if mejor_espacio_restante > espacio_restante_actual:
                    mejor_espacio_restante = espacio_restante_actual
                    mejor_base = base_actual
        cabeza += 1
    if mejor_base == -1:
        return None # No se encontro ninguna base en la cual se pueda haber puesto el requerimiento
    else:
        
        pass

bestFit(0,"hola", 10)