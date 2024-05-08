import time
# Vf = Vi + α∆t
def hallarVeloFinal():
    veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
    while(veloInicial < 0):
        print("!!El valor ingresado no corresponde a VELOCIDAD INICIAL!!")
        veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
    tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
    while(tiempo <= 0):
        print("!!El valor ingresado no corresponde a TIEMPO!!")
        tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
    aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
    while(aceleracion == 0):
      print("!!El valor ingresado no corresponde a ACELERACION!!")
      aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
    print("Hallando la VELOCIDAD FINAL .... : ")
    time.sleep(2)
    print("La velocidad final es: ",veloInicial + (aceleracion*tiempo),"m/s")

# Metodo para hallar la velocidad inicial
def hallarVeloInicial():
    veloFinal = float(input("Ingrese la velocidad final(metros/segundos): "))
    while(veloFinal == 0):
        print("!!El valor ingresado no corresponde a VELOCIDAD FINAL!!")
        veloFinal = float(input("Ingrese la velocidad final(metros/segundos): "))
    tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
    while(tiempo <= 0):
        print("!!El valor ingresado no corresponde a TIEMPO!!")
        tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
    aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
    while(aceleracion == 0):
      print("!!El valor ingresado no corresponde a ACELERACION!!")
      aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
    print("Hallando la VELOCIDAD INICIAL .... : ")
    time.sleep(2)
    print("La velocidad inicial es: ",veloFinal - (aceleracion*tiempo),"m/s")

# Metodo para hallar la variacion del tiempo
def hallarTiempo():
    veloFinal = float(input("Ingrese la velocidad final(metros/segundos): "))
    while(veloFinal == 0):
        print("!!El valor ingresado no corresponde a VELOCIDAD FINAL!!")
        veloFinal = float(input("Ingrese la velocidad final(metros/segundos): "))
    veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
    while(veloInicial < 0):
        print("!!El valor ingresado no corresponde a VELOCIDAD INICIAL!!")
        veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
    aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
    while(aceleracion == 0):
      print("!!El valor ingresado no corresponde a ACELERACION!!")
      aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
    print("Hallando la VARIACION DEL TIEMPO .... : ")
    time.sleep(2)
    print("La variacion del tiempo es: ",(veloFinal - veloInicial)/aceleracion,"s")

#  Metodo para hallar la aceleracion
def hallarAceleracion():
    veloFinal = float(input("Ingrese la velocidad final(metros/segundos): "))
    while(veloFinal == 0):
        print("!!El valor ingresado no corresponde a VELOCIDAD FINAL!!")
        veloFinal = float(input("Ingrese la velocidad final(metros/segundos): "))
    veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
    while(veloInicial < 0):
        print("!!El valor ingresado no corresponde a VELOCIDAD INICIAL!!")
        veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
    tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
    while(tiempo <= 0):
        print("!!El valor ingresado no corresponde a TIEMPO!!")
        tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
    print("Hallando la ACELERACION .... : ")
    time.sleep(2)
    print("La aceleracion es: ",(veloFinal - veloInicial)/tiempo,"s")


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
elif(operacion == 2):
        print("Se ha seleccionado VARIACIÓN INICIAL")
        time.sleep(1)
        hallarVeloInicial()
elif(operacion == 3):
        print("Se ha seleccionado VELOCIDAD DEL TIEMPO")
        time.sleep(1)
        hallarTiempo()
else:
        print("Se ha seleccionado ACELERACION")
        time.sleep(1)
        hallarAceleracion()
