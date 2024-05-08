import time
# ∆x = Vi∆t +(α(∆t)^2)/2

# Método para hallar  la distancia
def hallarDistancia():
    veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
    if(veloInicial >= 0):
        tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
        if(tiempo > 0):
            aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
            print("Hallando DISTANCIA .... : ")
            time.sleep(2)
            print("La distancia es:",veloInicial*tiempo + (aceleracion*tiempo**2/2),"m")
        else:
            while(tiempo <= 0):
                print("!!El valor ingresado no se puede ingresar a TIEMPO!!")
                tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
            aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
            print("Hallando DISTANCIA .... : ")
            time.sleep(2)
            print("La distancia es:",veloInicial*tiempo + (aceleracion*tiempo**2/2),"m")
    else:
        while(veloInicial < 0):
            print("!!El valor ingresado no se puede ingresar a VELOCIDAD INICIAL!!")
            veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
        tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
        if(tiempo > 0):
            aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
            print("Hallando DISTANCIA .... : ")
            time.sleep(2)
            print("La distancia es:",veloInicial*tiempo + (aceleracion*tiempo**2/2),"m")
        else:
            while(tiempo <= 0):
                print("!!El valor ingresado no se puede ingresar a TIEMPO!!")
                tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
            aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
            print("Hallando DISTANCIA .... : ")
            time.sleep(2)
            print("La distancia es:",veloInicial*tiempo + (aceleracion*tiempo**2/2),"m")

# Main
print("Bienvenido a su calculadora de MRUV")
print("Cual es su incognita: ")
print("1) Distancia")
print("2) Tiempo")
print("3) Velocidad Inicial")
print("4) Aceleración")
operacion = float(input("Ingrese el número de su incognita: "))
while(operacion != 1 and operacion != 2 and operacion != 3 and operacion != 4):
    print("!!Número de incognita no disponible!!")
    print("Cual es su incognita: ")
    print("1) Distancia")
    print("2) Tiempo")
    print("3) Velocidad Inicial")
    print("4) Aceleración")
    operacion = float(input("Ingrese el número de su incognita: "))
if(operacion==1):
    print("Se ha seleccionado DISTANCIA")
    time.sleep(1)
    hallarDistancia()
