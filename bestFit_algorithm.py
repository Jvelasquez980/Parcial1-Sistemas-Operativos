def best_fit(memory, req : int, index : int  ): #ESTA ES LA FUNCION PARA EL PARCIAL
    base = 0
    limite = 1
    espacio_restante_actual = None
    mejor_base = -1
    mejor_espacio_restante = -1
    cabeza_con_mejor_rendimiento = -1
    # Hacemos una prueba de la validez de los datos ingresados, para no tener errores 
    if validacion_de_parametros(memory, req,index) == None:
        return None
    memoria_recibida_formateada,cabeza, tamano_de_la_tabla, req=validacion_de_parametros(memory, req,index)
    
    while(True):
        tupla_actual = memoria_recibida_formateada[cabeza]
        limite_actual = tupla_actual[limite] 
        base_actual = tupla_actual[base]
        if index == cabeza and mejor_espacio_restante != -1:
            break 
        if  limite_actual >= req:
            espacio_restante_actual = limite_actual - req
            if mejor_espacio_restante == -1: # Verificamos si es la primera iteracion 
                mejor_espacio_restante = espacio_restante_actual
                mejor_base = base_actual
                cabeza_con_mejor_rendimiento = cabeza
                mejor_tupla = tupla_actual
                if mejor_espacio_restante == 0:
                    break
            else:
                if mejor_espacio_restante > espacio_restante_actual:
                    mejor_espacio_restante = espacio_restante_actual
                    mejor_base = base_actual
                    cabeza_con_mejor_rendimiento = cabeza
                    mejor_tupla = tupla_actual
                    if mejor_espacio_restante == 0:
                        break

        cabeza = (cabeza + 1)%(tamano_de_la_tabla)
        if mejor_base == -1 and cabeza == index:
            
            return print("No se encontro ninguna base con el espacio requerido") 
    if mejor_espacio_restante == 0:
        nueva_memoria = memoria_recibida_formateada.copy()
        nueva_memoria.remove(mejor_tupla)
        tamano_de_la_tabla = tamano_de_la_tabla - 1
        creacion_nueva_memoria_txt(nueva_memoria)
        if cabeza_con_mejor_rendimiento == tamano_de_la_tabla:
            cabeza_con_mejor_rendimiento = (cabeza_con_mejor_rendimiento)%(tamano_de_la_tabla)
            return nueva_memoria, mejor_base, req, cabeza_con_mejor_rendimiento
        return nueva_memoria, mejor_base, req, cabeza_con_mejor_rendimiento
        
    tupla_a_actualizar = list(mejor_tupla)
    tupla_a_actualizar[base] = tupla_a_actualizar[base] + req
    tupla_a_actualizar[limite] = tupla_a_actualizar[limite] - req
    nueva_memoria = memoria_recibida_formateada.copy()
    nueva_memoria[cabeza_con_mejor_rendimiento] = tuple(tupla_a_actualizar)
    creacion_nueva_memoria_txt(nueva_memoria)
    return nueva_memoria, mejor_base, req, cabeza_con_mejor_rendimiento 

def creacion_nueva_memoria_txt(nueva_memoria_txt): # Funcion para crear un txt con la nueva memoria
    with open("nueva_memoria.txt", "w") as archivo:
        archivo.write("[\n")  # Abre la lista
        for base, limite in nueva_memoria_txt:
            archivo.write(f"    ({base}, {limite}),\n")  
        archivo.write("]\n")  # Cierra la lista
        archivo.close()
        
def validacion_de_parametros(memory, req : int, index : int  ): # Funcion para validar los parametros ingresados
    if type(memory) is str:    
        try:
            memoria_recibida_formateada = eval(memory) 
        except SyntaxError as e:
            return print('La memoria tiene un formato no valido, problema de sintaxis, error: ' + str(e))
        except NameError as e:
            return print('La memoria tiene un formato no valido, problema de sintaxis, error: ' + str(e))
    else:
        try:
            memoria_recibida_formateada = memory.copy()
        except AttributeError as e:
            return print('La memoria tiene un formato no valido,  error: ' + str(e))
            
    cabeza = index
    tamano_de_la_tabla = len(memoria_recibida_formateada)
    if type(memoria_recibida_formateada) is not list:
        return print('La tabla de memoria recibida no es una lista por lo que no puede ser utilizada')
        
    elif len(memoria_recibida_formateada) == 0:
        return print('La tabla de memoria recibida no tiene valores con los cual operar')
         
    elif type(index) is not int:
        try:
            index = int(index)
        except ValueError as e:
            return print('El valor del index no puede ser procesado error: ValueError ' + str(e))
        except TypeError as e:
            return print('El valor del index no puede ser procesado error: TypeError ' + str(e))
    elif index < 0:
        return print('El index o cabeza de la tabla no puede ser negativo, por lo tanto no es posible utilizarlo')
    elif index > tamano_de_la_tabla - 1:
        return print('El index o cabeza de la tabla no puede estar fuera de los limites de la misma')
    elif type(req) is not int:
        try:
            req = int(req)
        except ValueError as e:
            return print('El valor del requerimiento no puede ser procesado error: ValueError ' + str(e))
        except TypeError as e:
            return print('El valor del requerimiento no puede ser procesado error: TypeError ' + str(e))
    elif req <= 0:
        return print('El valor requerido no puede ser un numero negativo o 0, no se puede utilizar')
    for x in memoria_recibida_formateada:
        if len(x) != 2:
            return print('La memoria tiene un formato no valido')
        elif type(x) is not tuple:
            if type(x) is not list:
                return print('La memoria tiene un formato no valido')
        for y in x:
            if type(y) is not int:
                return print('La memoria tiene un formato no valido, hay valores dentro de la misma que no son numeros')
    return memoria_recibida_formateada,cabeza, tamano_de_la_tabla, req

def bestFit_algorithm_salida_hex(memory, req : int, index : int  ): #El indice se manejara como una lista en python que empieza en 0
    base = 0
    limite = 1
    espacio_restante_actual = None
    mejor_base = -1
    mejor_espacio_restante = -1
    cabeza_con_mejor_rendimiento = -1
    posicion_para_transformar_salida = 0
    # Hacemos una prueba de la validez de los datos ingresados, para no tener errores 
    if validacion_de_parametros(memory, req,index) == None:
        return None
    memoria_recibida_formateada,cabeza, tamano_de_la_tabla, req=validacion_de_parametros(memory, req,index)
    
    while(True):
        tupla_actual = memoria_recibida_formateada[cabeza]
        limite_actual = tupla_actual[limite] 
        base_actual = tupla_actual[base]
        if index == cabeza and mejor_espacio_restante != -1:
            break 
        if  limite_actual >= req:
            espacio_restante_actual = limite_actual - req
            if mejor_espacio_restante == -1: # Verificamos si es la primera iteracion 
                mejor_espacio_restante = espacio_restante_actual
                mejor_base = base_actual
                cabeza_con_mejor_rendimiento = cabeza
                mejor_tupla = tupla_actual
                if mejor_espacio_restante == 0:
                    break
            else:
                if mejor_espacio_restante > espacio_restante_actual:
                    mejor_espacio_restante = espacio_restante_actual
                    mejor_base = base_actual
                    cabeza_con_mejor_rendimiento = cabeza
                    mejor_tupla = tupla_actual
                    if mejor_espacio_restante == 0:
                        break

        cabeza = (cabeza + 1)%(tamano_de_la_tabla)
        if mejor_base == -1 and cabeza == index:
            
            return print("No se encontro ninguna base con el espacio requerido") 
    if mejor_espacio_restante == 0:
        nueva_memoria = memoria_recibida_formateada.copy()
        nueva_memoria.remove(mejor_tupla)
        tamano_de_la_tabla = tamano_de_la_tabla - 1
        creacion_nueva_memoria_txt_hex(nueva_memoria)
        if cabeza_con_mejor_rendimiento == tamano_de_la_tabla:
            cabeza_con_mejor_rendimiento = (cabeza_con_mejor_rendimiento)%(tamano_de_la_tabla)
            
            for x in nueva_memoria:
                x = list(x)
                x[base] = hex(x[base])
                x[limite] = hex(x[limite])
                nueva_memoria[posicion_para_transformar_salida] = tuple(x)
                posicion_para_transformar_salida += 1
            return nueva_memoria, hex(mejor_base), hex(req), hex(cabeza_con_mejor_rendimiento) 
        for x in nueva_memoria:
            x = list(x)
            x[base] = hex(x[base])
            x[limite] = hex(x[limite])
            nueva_memoria[posicion_para_transformar_salida] = tuple(x)
            posicion_para_transformar_salida += 1
        return nueva_memoria, hex(mejor_base), hex(req), hex(cabeza_con_mejor_rendimiento) 
        
    tupla_a_actualizar = list(mejor_tupla)
    tupla_a_actualizar[base] = tupla_a_actualizar[base] + req
    tupla_a_actualizar[limite] = tupla_a_actualizar[limite] - req
    nueva_memoria = memoria_recibida_formateada.copy()
    nueva_memoria[cabeza_con_mejor_rendimiento] = tuple(tupla_a_actualizar)
    creacion_nueva_memoria_txt_hex(nueva_memoria)
    for x in nueva_memoria:
        x = list(x)
        x[base] = hex(x[base])
        x[limite] = hex(x[limite])
        nueva_memoria[posicion_para_transformar_salida] = tuple(x)
        posicion_para_transformar_salida += 1
    return nueva_memoria, hex(mejor_base), hex(req), hex(cabeza_con_mejor_rendimiento) 

def creacion_nueva_memoria_txt_hex(nueva_memoria_txt): # Funcion para crear un txt con la nueva memoria en hexadecimal
    with open("nueva_memoria_hex.txt", "w") as archivo:
        archivo.write("[\n")  # Abre la lista
        for base, limite in nueva_memoria_txt:
            archivo.write(f"    ({hex(base)}, {hex(limite)}),\n")  
        archivo.write("]\n")  # Cierra la lista
        archivo.close()