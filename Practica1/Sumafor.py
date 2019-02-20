print()
print("Imprime los primeros N numeros y la suma de los mismos")
n = input ("Inserta número N positivo:    ")

n = int(n)
suma = 0

for numero in range(0,n+1,1):
	suma = suma+numero

print("La suma de los primeros",n,"numeros es:")
print(suma)
print()
print("los primeros",n,"numeros son:")

for i in range (1,n+1):
	print(i,end=",")

print()
print()


