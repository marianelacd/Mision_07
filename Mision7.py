#Autor: Marianela Contreras
#Mision 07. Ciclos While. Programa para crear un menu donde se peuda dividir, encontrar el mayor, o salir.

#función para dividir restando, mandando como parámetros dividendo y divisor.
def dividir(dividendo,divisor):
    cociente = 1
    residuo = dividendo - divisor

    if divisor > dividendo:
        print(dividendo,"/",divisor,"= 0 sobra", dividendo)
    else:
        while residuo >= divisor :
            residuo = residuo - divisor
            cociente +=1
        print(dividendo,"/", divisor, "=", cociente, "sobra", residuo)


#función para encontrar el número mayor de un conjunto de valores que teclea el usuario.
def encontrarMayor():
    print ("Tecela una serie de números para encontrar el mayor.")
    número1= 0
    número2=0

    while número2 != -1:
        número2= int(input("Teclea un número [-1 para salir]:"))
        if número2 <-1:
            print ("Error. No se pueden utilizar valores negativos.")
        elif número1> número2:
            número1 = número1
        elif número2 >número1:
            número1 = número2

    if número1 == 0 and número2 ==-1:
        print ("No hay mayor")
    else:
        print ("El mayor es:",número1)


#función principal del programa y la que se correrá.
def main():
    print("Misión 07. Ciclos while\nAutor: Marianela Contreras Domínguez \nMatrícula: A01374769")
    print ("1.Calcular divisiones\n2.Encontrar el mayor\n3.Salir")
    opción= int(input("Teclea tu opción:"))

    while opción >0:
        if opción== 1:
            dividendo= int(input("Dividendo:"))
            divisor= int(input("Divisor:"))
            dividir(dividendo,divisor)
            print("Misión 07. Ciclos while\nAutor: Marianela Contreras Domínguez \nMatrícula: A01374769")
            print("1.Calcular divisiones\n2.Encontrar el mayor\n3.Salir")
            opción = int(input("Teclea tu opción:"))
        elif opción ==2:
            encontrarMayor()
            print("Misión 07. Ciclos while\nAutor: Marianela Contreras Domínguez \nMatrícula: A01374769")
            print("1.Calcular divisiones\n2.Encontrar el mayor\n3.Salir")
            opción = int(input("Teclea tu opción:"))
        elif opción !=1 and opción !=2 and opción !=3:
            print ( "ERROR, teclea 1, 2 o 3")
            print("Misión 07. Ciclos while\nAutor: Marianela Contreras Domínguez \nMatrícula: A01374769")
            print("1.Calcular divisiones\n2.Encontrar el mayor\n3.Salir")
        elif opción ==3:
            print ("Gracias por usar este programa, regresa pronto.")
            break


main()