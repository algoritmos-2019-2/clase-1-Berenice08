print("Calcula el factorial de un numero N")
num=int(input("Ingresa N:  "))
factorial=1
for i in range(num):
	factorial=factorial*num
	num=num-1
print("El factorial es")
print(factorial)


