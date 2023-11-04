'''
*	Solución de ecuaciones lineales nxn usando el algoritmo Bareiss-Montante
*	Autor: José Isaías Vázquez Macías
'''

'''
*	Descripción:
*	Función para validar que una cadena pueda representar un número real
*	
*	Parámetros:
*	- "string" : la cadena a analizar
*	
*	Valor de retorno:
*	Booleano : validez de la cadena como número real
'''
def isFloat(string):
	validChars = ".-0123456789" # caracteres válidos en un número real
	slashFound = False  # variable para registrar si se halló algún guión en la cadena
	dotFound = False    # variable para registrar si se halló algún punto en la cadena
	
	if len(string) > 0: # si el tamaño de la cadena es mayor a 0...
		if '-' in string and string[0] != '-':  # si la cadena contiene un guión, pero dicho guión no se ubica como el primer caracter...
			return False    # la cadena no es un número real válido
		else:   # sino...
			for c in string:    # iterando en cada caracter de la cadena
				if c not in validChars: # si el caracter iterado no se encuentra en los caracteres validos...
					return False    # la cadena no es un número real válido
				
				if c == '-':    # si el caracter iterado es un guión...
					if not slashFound:  # si aún no se ha hallado algún guión...
						slashFound = True   # registrar que ya hay un guión en la cadena
					else:   # sino...
						return False    # la cadena no es un número real válido
				if c == '.':    # si el caracter iterado es un punto...
					if not dotFound:    # si aún no hay registro de algún punto...
						dotFound = True # registrar que ya hay un punto en la cadena
					else:   # sino...
						return False    # la cadena no es un número real valido
	else:   # sino...
		return False    # la cadena no es un número real válido
	return True # si a pesar de las trabas llega a este punto, es un número real válido

'''
*	Descripción:
*	Función para validar que una cadena pueda representar un número entero
*	
*	Parámetros:
*	- "string" : la cadena a analizar
*	- "forcePositive" : especifica si la cadena analizada debe ser, a parte de entero, un número positivo
*	
*	Valor de retorno:
*	Booleano : validez de la cadena como número entero (y positivo si requerido)
'''
def isInt(string, forcePositive):
	validChars = "-0123456789"  # caracteres válidos en un número entero
	slashFound = False  # variable para registrar si se halló algún guión en la cadena
	if len(string) > 0: # si el tamaño de la cadena es mayor a 0...
		for c in string:    # iterando en cada caracter de la cadena
			if c not in validChars: # si el caracter iterado no se encuentra en los caracteres validos...
				return False    # la cadena no es un número real válido
			
			if c == '-':    # si el caracter iterado es un guión...
				if not forcePositive:   # si el entero no debe ser un positivo forzosamente...
					if not slashFound and len(string) >= 2: # si aún no se ha hallado un guión y el tamaño de la cadena es mayor o igual a 2...
						slashFound = True   # registrar que ya hay un guión en la cadena
					else:   # sino...
						return False    # la cadena no es un número entero válido
				else:   # sino...
					return False    # la cadena no es un número entero positivo válido
	else:   # sino...
		return False    # la cadena no es un número entero válido
	return True # si a pesar de las trabas llega a este punto, es un número entero válido

'''
*	Descripción:
*	Función para generar una matriz identidad de la dimensión que se especifique
*	
*	Parámetros:
*	- "dimension" : la cantidad de filas y columnas de la matriz
*	
*	Valor de retorno:
*	Lista : matriz identidad de la dimension especificada
'''
def generateMatrixIdentity(dimension):
	matrix = list()	# lista donde se almacena las filas de la matriz
	
	for i in range(0, dimension):	# ciclo controlador de las filas
		row = list()	# fila actual

		for j in range(0, dimension):	# ciclo controlador de las columnas
			if i == j:	# si el índice de la fila es el mismo que el índice de la columna, la posición actual es parte de la diagonal, así que...
				row.append(1)	# se asigna un 1 a la posición actual
			else:	# si se encuentra en cualquier otra fila o columna...
				row.append(0)	# se asigna un 0 a la posición actual
		matrix.append(row)	# incorporar la fila actual a la lista de filas de la matriz
	return matrix	# se regresa la matriz identidad final

'''
*	Descripción:
*	Función para resolver la matriz usando el algoritmo Bareiss-Montante
*	
*	Parámetros:
*	- "matrix" : la matriz a operar
*	
*	Valor de retorno:
*	Lista : lista de matrices, la primera siendo la matriz principal y la segunda la secundaria
'''
def solve(matrix):
	dimension = len(matrix)	# la dimension de la matriz obtenida a partir de la longitud de la lista de filas (matriz) en el parámetro de la función
	identity = generateMatrixIdentity(dimension)	# genera una matriz identidad a partir de la dimensión de la matriz principal
	
	currentPivot = None	# almacena el valor del pivote actual
	lastPivot = 1	# almacena el valor del último pivote, de acuerdo al algoritmo comienza en 1
	
	for currentIteration in range(0, dimension):	# ciclo controlador de la iteración actual (también se usa como controlador de la posición de la diagonal)
		currentPivot = matrix[currentIteration][currentIteration]	# asignar el pivote actual al valor de la diagonal en la que nos encontramos iterando

		print("==========")
		print(matrix)
		print(identity)
		print(f"Piv. Anterior: {lastPivot}")
		print(f"Piv. Actual: {currentPivot}")
		
		for i in range(0, dimension):	# ciclo controlador de filas
			for j in range(0, dimension):	# ciclo controlador de columnas
				if i != currentIteration:	# si la fila actual es diferente a la de la fila pivote...
					if j != currentIteration:	# si la columna actual es diferente a la de la columna pivote...
						#print(f"matrix[{i}][{j}] = (({currentPivot} * {matrix[i][j]}) - ({matrix[currentIteration][j]} * {matrix[i][currentIteration]})) / {lastPivot}")
						#print(f"= ({(currentPivot * matrix[i][j])} - {matrix[currentIteration][j] * matrix[i][currentIteration]}) / {lastPivot}")
						#print(f"= {(currentPivot * matrix[i][j]) - (matrix[currentIteration][j] * matrix[i][currentIteration])} / {lastPivot}")
						#print(f"= {((currentPivot * matrix[i][j]) - (matrix[currentIteration][j] * matrix[i][currentIteration])) / lastPivot}")

						# los valores de la matriz principal cambian solo cuando la fila y la columna son diferentes a las del pivote
						matrix[i][j] = ((currentPivot * matrix[i][j]) - (matrix[currentIteration][j] * matrix[i][currentIteration])) / lastPivot	# realizar cálculo esencial del algoritmo en la matriz principal

					#print(f"identity[{i}][{j}] = (({currentPivot} * {identity[i][j]}) - ({identity[currentIteration][j]} * {matrix[i][currentIteration]})) / {lastPivot}")
					#print(f"= ({(currentPivot * identity[i][j])} - {identity[currentIteration][j] * matrix[i][currentIteration]}) / {lastPivot}")
					#print(f"= {(currentPivot * identity[i][j]) - (identity[currentIteration][j] * matrix[i][currentIteration])} / {lastPivot}")
					#print(f"= {((currentPivot * identity[i][j]) - (identity[currentIteration][j] * matrix[i][currentIteration])) / lastPivot}")

					# los valores de la matriz secundaria cambian solo cuando la fila es diferente a la del pivote
					identity[i][j] = ((currentPivot * identity[i][j]) - (identity[currentIteration][j] * matrix[i][currentIteration])) / lastPivot	# realizar cálculo esencial del algoritmo en la matriz secundaria
		
		for i in range(0, dimension):	# ciclo controlador de la fila, esta estructura busca reemplazar los demás valores de la columna del pivote con 0
			if i == currentIteration:	# si la fila actual es la fila del pivote...
				continue	# no hacer cambios y continuar con el ciclo
			else:	# si no...
				matrix[i][currentIteration] = 0	# asignar 0 a la posición actual
		
		#currentIteration = currentIteration + 1 # error, no se debe aumentar manualmente porque el ciclo ya lo hace por sí solo
		lastPivot = currentPivot	# Asignar el pivote actual como último pivote
	return [matrix, identity]	# una vez terminado el procedimiento, regresar la lista de matrices

'''
*	Descripción:
*	Función principal. Pide el ingreso de los datos y manda llamar a todas las demás.
*	
*	Parámetros:
*	No tiene.
*	
*	Valor de retorno:
*	No tiene.
'''
def main():
	
	infoInput = None	# variable temporal que almacena la información ingresada por el usuario
	
	keepAskingDimension = True	# variable temporal usada para saber si la información ingresada fue correcta
	dimension = 0	# almacena la dimension de la matriz. Nunca es cero; posteriormente es reemplazado por la info. ingresada
	
	while keepAskingDimension:	# ciclo controlador del ingreso de la dimensión
		infoInput = input("Ingresa la cantidad de filas y columnas de la matriz (numero entero mayor a 1): ")
		
		if isInt(infoInput, True):	# si la información ingresada es un entero positivo...
			dimension = int(infoInput)	# asignar la información ingresada a la dimension
			
			if dimension >= 2:	# si la dimensión es válida (mayor a 1/mayor o igual a 2)...
				keepAskingDimension = False	# salir del ciclo
			else:	# sino...
				print("- El numero de filas y columnas debe ser mayor a 1.")
		else:	# sino...
			print("- La informacion introducida no es un numero entero mayor a 1.")
	
	matrix = list()	# almacena la lista de filas de la matriz principal
	
	for i in range(0, dimension):	# ciclo controlador de filas
	
		currentRow = list()	# variable temporal que almacena la fila siendo ingresada
		for j in range(0, dimension):	# ciclo controlador de columnas
		
			keepAskingValue = True	# variable temporal usada para saber si la información ingresada fue correcta
			while keepAskingValue:	# ciclo controlador del ingreso del coeficiente actual
				infoInput = input(f"Ingresa el coeficiente de la fila {i+1} y la columna {j+1} (numero entero): ")
				
				if isInt(infoInput, False):	# si el valor ingresado es un entero válido...
					currentRow.append(int(infoInput))	# asignar el valor ingresado a la posición actual
					keepAskingValue = False	# salir del ciclo
				else:	# si no...
					print("- La informacion introducida no es un numero entero.")
		
		matrix.append(currentRow)	# agregar la fila ingresada a la lista de filas (matriz principal)
	
	matrixEquals = list()	# lista de los términos independientes de las ecuaciones
	for i in range(0, dimension):	# ciclo controlador de ecuación

		keepAskingEqual = True	# variable temporal usada para saber si la información ingresada fue correcta
		while keepAskingEqual:	# ciclo controlador del ingreso del término independiente
			infoInput = input(f"Término independiente de la ec. {i+1} (numero real): ")

			if isFloat(infoInput):	# si la información ingresada es un número real válido...
				matrixEquals.append(float(infoInput))	# asignar el término independiente a la lista
				keepAskingEqual = False	# salir del ciclo
			else:	# si no...
				print("- La informacion introducida no es un numero real.")
	
	result = solve(matrix)	# llama a la función de solución

	print("==========")
	print(f"Matriz principal: {result[0]}")
	print(f"Matriz secundaria: {result[1]}")

	matrixDeterminant = result[0][0][0]	# almacena el determinante de la matriz a partir de la primer diagonal
	for i in range(1, dimension):	# para cada diagonal después del primero...
		if result[0][i][i] != matrixDeterminant:	# si la diagonal actual es diferente a la primera...
			print("- La diagonal de la matriz principal no es igual. El procedimiento contiene algun error.")
			# notifica error pero no se detiene
	
	inverse = result[1].copy()	# clona la matriz secundaria y la almacena en una variable nueva
	for i in range(0, dimension):	# ciclo controlador de filas
		for j in range(0, dimension):	# ciclo controlador de columnas
			inverse[i][j] = inverse[i][j] / matrixDeterminant	# dividir la posición actual entre el determinante
	
	print(f"Matriz inversa: {inverse}")

	solutions = [0] * dimension	# almacena las soluciones al sistema
	for i in range(0, dimension):	# ciclo controlador de filas
		for j in range(0, dimension):	# ciclo controlador de columnas
			solutions[i] = solutions[i] + inverse[i][j] * matrixEquals[j]	# obtener soluciones a partir de la matriz secundaria

	print(f"Soluciones: {solutions}")
	
main()	# ejecuta la función principal