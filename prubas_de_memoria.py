archivo = open('memoria.txt', 'r')
texto_del_archivo = archivo.read()
print(texto_del_archivo)
archivo.close()


# memoria = eval(texto_del_archivo)
# print(memoria)
# print(type(memoria))
# print(len(memoria))
# base_limite = memoria[0]
# print(type(base_limite))
# base = 0
# limite = 1
# print(base_limite[base])
# print(type(base_limite[base]))

# for x in memoria:
#     print(x)


try:
    x = eval(texto_del_archivo)
    print(True)
except SyntaxError as e:
    print('No se puede transformar el archivo, error: ' + str(e))
print(x)