def bestFit_algorimth(memory, req : int, index : int  ): #El indice se manejara como una lista en python que empieza en 0
    base = 0
    limite = 1
    espacio_restante_actual = None
    mejor_base = -1
    mejor_espacio_restante = -1
    cabeza_con_mejor_rendimiento = -1
    # Hacemos una prueba de la validez de los datos ingresados, para no tener errores 
    if type(memory) is str:    
        try:
            memoria_recibida_formateada = eval(memory) 
        except SyntaxError as e:
            return print('No se puede transformar el archivo, problema de sintaxis, error: ' + str(e))
        except NameError as e:
            return print('No se puede transformar el archivo, problema de sintaxis, error: ' + str(e))
    else:
        memoria_recibida_formateada = memory.copy()
    cabeza = index
    tamano_de_la_tabla = len(memoria_recibida_formateada)
    if type(memoria_recibida_formateada) is not list:
        return print('La tabla de memoria recibida no es una lista por lo que no puede ser utilizada')
        
    elif len(memoria_recibida_formateada) == 0:
        return print('La tabla de memoria recibida no tiene valores con los cual operar')
         
    elif type(memoria_recibida_formateada[0]) is not tuple:
        return print('La tabla de memoria recibida no es una lista de tuplas por lo cual no puede ser utilizada')
    elif type(index) is not int:
        try:
            index = int(index)
        except ValueError as e:
            return print('El valor del index no puede ser procesado error: ' + str(e))
    elif index < 0:
        return print('El index o cabeza de la tabla no puede ser negativo, por lo tanto no es posible utilizarlo')
    elif type(req) is not int:
        try:
            req = int(req)
        except ValueError as e:
            return print('El valor del index no puede ser procesado error: ' + str(e))
        except TypeError as e:
            return print('El valor del index no puede ser procesado error: ' + str(e))
    elif req <= 0:
        return print('El valor requerido no puede ser un numero negativo o 0, no se puede utilizar')
    
    while(True):
        tupla_actual = memoria_recibida_formateada[cabeza]
        limite_actual = tupla_actual[limite] 
        base_actual = tupla_actual[base]
        if index == base_actual and mejor_espacio_restante != -1:
            break 
        if  limite_actual >= req:
            espacio_restante_actual = limite_actual - req
            if mejor_espacio_restante == -1: # Verificamos si es la primera iteracion 
                mejor_espacio_restante = espacio_restante_actual
                mejor_base = base_actual
                cabeza_con_mejor_rendimiento = cabeza
                mejor_tupla = tupla_actual
            else:
                if mejor_espacio_restante > espacio_restante_actual:
                    mejor_espacio_restante = espacio_restante_actual
                    mejor_base = base_actual
                    cabeza_con_mejor_rendimiento = cabeza
                    mejor_tupla = tupla_actual

        cabeza = (cabeza + 1)%(tamano_de_la_tabla)
        if mejor_base == -1 and cabeza == index:
            
            return print("No se encontro ninguna base con el espacio requerido") 
    if mejor_espacio_restante == 0:
        nueva_memoria = memoria_recibida_formateada.copy()
        nueva_memoria.remove(mejor_tupla)
        tamano_de_la_tabla = tamano_de_la_tabla - 1
        if cabeza_con_mejor_rendimiento == tamano_de_la_tabla:
            cabeza_con_mejor_rendimiento = (cabeza_con_mejor_rendimiento - 1)%(tamano_de_la_tabla)
            return nueva_memoria, mejor_base, req, cabeza_con_mejor_rendimiento
             
        return nueva_memoria, mejor_base, req, cabeza_con_mejor_rendimiento
        
    tupla_a_actualizar = list(mejor_tupla)
    tupla_a_actualizar[base] = tupla_a_actualizar[base] + req
    tupla_a_actualizar[limite] = tupla_a_actualizar[limite] - req
    nueva_memoria = memoria_recibida_formateada.copy()
    nueva_memoria[cabeza_con_mejor_rendimiento] = tuple(tupla_a_actualizar)
    return nueva_memoria, mejor_base, req, cabeza_con_mejor_rendimiento 