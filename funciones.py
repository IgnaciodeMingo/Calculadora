def sumar(num1:int,num2:int) -> int:
    suma = num1+num2 #Proceso
    return suma #Salida
def restar(num1:int,num2:int) -> int:
    resta=num1-num2 #Proceso
    return resta #Salida
def dividir(num1:float,num2:float) -> float:
    if num2==0: #Siempre que el divisor sea 0
        xcero='No se puede dividir por 0'
        return xcero #Salida
    else:
        division=num1/num2 #Proceso
        return division #Segunda salida
def multiplicar(num1:int,num2:int) -> int:
    multiplicacion=num1*num2 #Proceso
    return multiplicacion #Salida
def potenciar(num1:int,num2:int) -> int:
    potencia=num1**num2 #Proceso
    return potencia #Salida
def calculo_resto(num1:float,num2:float)->float:
    if num2==0: #Siempre que el segundo número sea 0
        xcero='No se puede calcular el resto por 0'
        return xcero #Salida
    else:
        resto=num1%num2 #Proceso
        return resto #Salida
def calculo_factorial(repetir):
    if repetir < 0: #Siempre que el número sea negativo
        return "El factorial no está definido para números negativos." #Primer salida
    elif repetir == 0 or repetir == 1: #Siempre que el número sea 0 o 1
        return 1 #Segunda salida
    else: #Numeros mayores a 1
        return repetir * calculo_factorial(repetir - 1) #Tercer salida