from bestFit import bestFit_algorimth
archivo = open('memoria.txt', 'r')
texto_del_archivo = archivo.read()
print(texto_del_archivo)
archivo.close()

# work_memory = [(0x00A00000, 0x000C0000)]
# work_memory = str(work_memory)
# print(work_memory)
# work_memory = eval(work_memory)
# print(work_memory)

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


# try:
#     x = eval(texto_del_archivo)
#     print(True)
# except SyntaxError as e:
#     print('No se puede transformar el archivo, error: ' + str(e))
# print(x)
x = eval(texto_del_archivo)
print(x)
# x = 14
# print(x)
# x = (x + 1)%16
# print(x)
# x = (x + 1)%16
# print(x)
# x = (x - 1)%16
# print(x)
x = int(0x321321)
if bestFit_algorimth(texto_del_archivo,65535,0) != None:
    x,y,z,f = bestFit_algorimth(texto_del_archivo,65535,0)
    print(x)
    print(y)
    print(z)
    print(f)
else:
    valor_none = bestFit_algorimth(texto_del_archivo,65535,0)
    print(valor_none)

