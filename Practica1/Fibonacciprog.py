
#Tomando como serie de Fibonacci: 0,1,1,2,3,5,8,13,21...,y como primer termino al 0,segundo termino al 1, etc

print("Calcula los primeros N terminos de la serie de Fibonacci")
n=int(input("inserta N:  "))

a=0
b=1


if(n<0):
	print("invalido")
elif n==0:
	print("error") #pues no puede haber un termino cero
elif n == 1:
	print(a)

else:
	A=0
	B=1
	print(A)
	print(B)
	i=0
	m=n-2
	while i<m:
		C=A+B
		A=B
		B=C
		print(C)
		i+=1

