#Crear una calculadora, donde se pase como argumentos luego de la opción -o el operador que se va a ejecutar (+,-,*,/), luego de -n el primer número de la operación, y de -m el segundo número.

#Ejemplo:
#python3 calc.py -o + -n 5 -m 6
#5 + 6 = 11
#Considerar que el usuario puede ingresar los argumentos en cualquier orden. El programa deberá verificar que los argumentos sean válidos (no repetidos, números enteros, y operaciones válidas."

import getopt 
import sys

(options, arguments) = getopt.getopt(sys.argv[1:], 'o:n:m:')

print("Opciones: ",options)
print("Argumentos: ",arguments)

for op, ar in options:
	if op == "-o":
		operator = ar
	elif op == "-n":
		first = int(ar)
	elif op == "-m":
		second = int(ar)
	else:
		print("Opción Invalida")

#res = first operator second;
#print(res)
exec{"print (primer {} segundo }".format(op)}
	
