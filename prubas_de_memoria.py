from bestFit_algorithm import best_fit,bestFit_algorithm_salida_hex
archivo = open('memoria.txt', 'r')
texto_del_archivo = archivo.read()
print(texto_del_archivo)
archivo.close()
w = [
    (0, 2047),     # 2048 bytes
    (123, 8191),  # 4096 bytes
    [213,213], # 1024 bytes
    [123123, 1312], # 8192 bytes
    (28672, 30719), # 2048 bytes
    (36864, 45055), # 8192 bytes
    (53248, 57343), # 4096 bytes
    (61440, 1000)  # 4096 bytes
]

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
# x = eval(texto_del_archivo)
# print(x)
# x = 14
# print(x)
# x = (x + 1)%16
# print(x)
# x = (x + 1)%16
# print(x)
# x = (x - 1)%16
# print(x)
# x = int(0x321321)
# x = 0%10
# print(x)
print(w)
x = best_fit(w,1000,0)
print(x)
x = bestFit_algorithm_salida_hex(w,1000,0)
print(x)


