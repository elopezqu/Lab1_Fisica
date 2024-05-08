import time
# Vf = Vi + α∆t
def hallarVeloFinal():
    veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
    if(veloInicial >= 0):
        tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
        if(tiempo > 0):
            aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
            print("Hallando la VELOCIDAD FINAL .... : ")
            time.sleep(2)
            print("La velocidad final es:",veloInicial+ (aceleracion*tiempo),"m/s")
        else:
            while(tiempo <= 0):
                print("!!El valor ingresado no corresponde a TIEMPO!!")
                tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
            aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
            print("Hallando la VELOCIDAD FINAL .... : ")
            time.sleep(2)
            print("La velocidad final es:",veloInicial+ (aceleracion*tiempo),"m/s")
    else:
        while(veloInicial < 0):
            print("!!El valor ingresado no corresponde a VELOCIDAD INICIAL!!")
            veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
        tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
        if(tiempo > 0):
            aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
            print("Hallando la VELOCIDAD FINAL .... : ")
            time.sleep(2)
            print("La velocidad final es:",veloInicial+ (aceleracion*tiempo),"m/s")
        else:
            while(tiempo <= 0):
                print("!!El valor ingresado no corresponde a TIEMPO!!")
                tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
            aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
            print("Hallando la VELOCIDAD FINAL .... : ")
            time.sleep(2)
            print("La velocidad final es:",veloInicial+ (aceleracion*tiempo),"m/s")


# Main
print("Bienvenido a su calculadora de MRUV")
print("Cual es su incognita: ")
print("1) Velocidad final")
print("2) Velocidad Inicial")
print("3) Variacion del tiempo")
print("4) Aceleración")
operacion = float(input("Ingrese el número de su incognita: "))
while(operacion != 1 and operacion != 2 and operacion != 3 and operacion != 4):
    print("!!Número de incognita no disponible!!")
    print("Cual es su incognita: ")
    print("1) Velocidad final")
    print("2) Velocidad Inicial")
    print("3) Variacion del tiempo")
    print("4) Aceleración")
    operacion = float(input("Ingrese el número de su incognita: "))
if(operacion==1):
    print("Se ha seleccionado VELOCIDAD FINAL")
    time.sleep(1)
    hallarVeloFinal()
