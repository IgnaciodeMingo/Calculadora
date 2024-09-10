# -Evitaria abreviar variables a menos de que su nombre quede muy largo (INNECESARIO tanto... capaz si num1 o num2 pero es una boludez)
# -Yo usaria una bandera para validar lo de los calculos, ya que la asignacion de la linea 7 
# puede ser un poco complicada de entender y no se aplica en todos los lenguajes 
# y se ahorraria evaluar la gran condición de la línea 31 (---)
# -Las funciones deben anteponer verbos en su nombre por ejemplo calcular_suma o sumar seria un nombre adecuado,
# pero suma , resta, factorial no lo serian   ARREGLADO
# -No valida división por cero en el resto ni en la división ARREGLADO
# -Falta documentación

from os import system
from funciones import *

def menu():
    num1 = None
    num2 = None
    res_suma = res_resta = res_division = res_multiplicacion = res_potencia = res_resto = None    
    while(True):
        print("MENU CALCULADORA\n1. Ingresar Primer Operando\n2. Ingresar Segundo Operando\n3. Calcular Todas las operaciones\n4. Informar Resultados\n5. Salir")
        opcion = int(input("Su opcion: "))        
        if opcion == 1:
            num1 = int(input("Ingrese el primer número: "))
            print(f"El numero seleccionado es: {num1}")            
        elif opcion == 2:
            num2 = int(input("Ingrese el segundo número: "))
            print(f"El numero seleccionado es: {num2}")            
        elif opcion == 3:
            if num1 is None or num2 is None:
                #Siempre que no se ingrese alguno de las 2 entradas.
                print("Error, no hubo ingreso de 2 números todavía, reiniciando.")
            else:
                #Accede a las funciones que calculan los resultados
                res_suma = sumar(num1, num2)
                res_resta = restar(num1, num2)
                res_division = dividir(num1, num2)
                res_multiplicacion = multiplicar(num1, num2)
                res_potencia = potenciar(num1, num2)
                res_resto = calculo_resto(num1, num2)
                res_factorial=calculo_factorial(num1)
                res_factorial2=calculo_factorial(num2)
                print("Operaciones calculadas.")               
        elif opcion == 4:
            if res_suma is None or res_resta is None or res_division is None or res_multiplicacion is None or res_potencia is None or res_resto is None:
                #Siempre que no se pueda calcular los resultados.
                print("Error, no se han calculado las operaciones todavía.")
            else:
                print(f"El resultado de la suma es: {res_suma}")
                print(f"El resultado de la resta es: {res_resta}")
                print(f"El resultado de la division es: {res_division}")
                print(f"El resultado de la multiplicacion es: {res_multiplicacion}")
                print(f"El resultado de la potencia es: {res_potencia}")
                print(f"El resultado del resto es: {res_resto}")
                print(f"El resultado del factorial de {num1} es: {res_factorial}")
                print(f"El resultado del factorial de {num2} es: {res_factorial2}")                
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opción inválida, ingrese números entre 1-5")
        
        input("Pulse botón para continuar: ")
        system('cls')
menu()
print("Fin del programa")