import time
# ∆x = Vi∆t +(α(∆t)^2)/2

# Método para hallar la variacion de la distancia
def hallarDistancia():
    veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
    if(veloInicial >= 0):
        tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
        if(tiempo > 0):
            aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
            print("Hallando VARIACiÓN DE LA DISTANCIA .... : ")
            time.sleep(2)
            print("La distancia es:",veloInicial*tiempo + (aceleracion*tiempo**2/2),"m")
        else:
            while(tiempo <= 0):
                print("!!El valor ingresado no corresponde a TIEMPO!!")
                tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
            aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
            print("Hallando VARIACiÓN DE LA DISTANCIA .... : ")
            time.sleep(2)
            print("La distancia es:",veloInicial*tiempo + (aceleracion*tiempo**2/2),"m")
    else:
        while(veloInicial < 0):
            print("!!El valor ingresado no corresponde a VELOCIDAD INICIAL!!")
            veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
        tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
        if(tiempo > 0):
            aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
            print("Hallando VARIACiÓN DE LA DISTANCIA .... : ")
            time.sleep(2)
            print("La distancia es:",veloInicial*tiempo + (aceleracion*tiempo**2/2),"m")
        else:
            while(tiempo <= 0):
                print("!!El valor ingresado no corresponde a TIEMPO!!")
                tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
            aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
            print("Hallando VARIACiÓN DE LA DISTANCIA .... : ")
            time.sleep(2)
            print("La distancia es:",veloInicial*tiempo + (aceleracion*tiempo**2/2),"m")

# Metodo para hallar la variacion del tiempo
def hallarTiempo():
    veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
    if(veloInicial >= 0):
        distancia = float(input("Ingrese variacion de la distancia(metros): "))
        if(distancia >= 0):
            aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
            print("Hallando VARIACiÓN DEL TIEMPO .... : ")
            time.sleep(2)
            print("La variación del tiempo es:", formula_general(aceleracion/2,veloInicial,-distancia),"s")
        else:
            while(distancia < 0):
                print("!!El valor ingresado no corresponde a VARIACION DE LA DISTANCIA!!")
                distancia = float(input("Ingrese variacion de la distancia(metros): "))
            aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
            print("Hallando VARIACiÓN DEL TIEMPO .... : ")
            time.sleep(2)
            print("La variación del tiempo es:", formula_general(aceleracion/2,veloInicial,-distancia),"s")
    else:
        while(veloInicial < 0):
            print("!!El valor ingresado no corresponde a VELOCIDAD INICIAL!!")
            veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
        distancia = float(input("Ingrese variacion de la distancia(metros): "))
        if(distancia >= 0):
            aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
            print("Hallando VARIACiÓN DEL TIEMPO .... : ")
            time.sleep(2)
            print("La variación del tiempo es:", formula_general(aceleracion/2,veloInicial,-distancia),"s")
        else:
            while(distancia < 0):
                print("!!El valor ingresado no corresponde a VARIACION DE LA DISTANCIA!!")
                distancia = float(input("Ingrese variacion de la distancia(metros): "))
            aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
            print("Hallando VARIACiÓN DEL TIEMPO .... : ")
            time.sleep(2)
            print("La variación del tiempo es:", formula_general(aceleracion/2,veloInicial,-distancia),"s")

def formula_general(a, b, c):
    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    if x1 >= 0:
      return x1
    elif x2 >= 0:
      return x2


# Main
print("Bienvenido a su calculadora de MRUV")
print("Cual es su incognita: ")
print("1) Variación de la Distancia")
print("2) Variación del Tiempo")
print("3) Velocidad Inicial")
print("4) Aceleración")
operacion = float(input("Ingrese el número de su incognita: "))
while(operacion != 1 and operacion != 2 and operacion != 3 and operacion != 4):
    print("!!Número de incognita no disponible!!")
    print("Cual es su incognita: ")
    print("1) Variación de la Distancia")
    print("2) Variación del Tiempo")
    print("3) Velocidad Inicial")
    print("4) Aceleración")
    operacion = float(input("Ingrese el número de su incognita: "))
if(operacion==1):
    print("Se ha seleccionado VARIACIÓN DE LA DISTANCIA")
    time.sleep(1)
    hallarDistancia()
elif(operacion == 2):
        print("Se ha seleccionado VARIACIÓN DEL TIEMPO")
        time.sleep(1)
        hallarTiempo()
