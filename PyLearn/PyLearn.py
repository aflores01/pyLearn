#Lambda: Programación funcional (Recibe datos de entrada y obtiene datos de salida)

listMultiplyAt1000 = [(i,i * i) for i in range(10)]
print(listMultiplyAt1000)

#Función lambda

multiply = lambda a,b: a*b 
result = multiply(5,5)
print(str(result))

