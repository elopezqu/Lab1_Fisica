import time
# ∆x = Vi∆t +(α(∆t)^2)/2

# Método para hallar la variacion de la distancia
def hallarDistancia():
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
    print("Hallando VARIACiÓN DE LA DISTANCIA .... : ")
    time.sleep(2)
    print("La distancia es:",veloInicial*tiempo + (aceleracion*tiempo**2/2),"m")

# Metodo para hallar la variacion del tiempo
def hallarTiempo():
    veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
    while(veloInicial < 0):
      print("!!El valor ingresado no corresponde a VELOCIDAD INICIAL!!")
      veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
    distancia = float(input("Ingrese variacion de la distancia(metros): "))
    while(distancia <= 0):
      print("!!El valor ingresado no corresponde a VARIACION DE LA DISTANCIA!!")
      distancia = float(input("Ingrese variacion de la distancia(metros): "))
    aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
    while(aceleracion == 0):
      print("!!El valor ingresado no corresponde a ACELERACION!!")
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

# Metodo para hallar Velocidad Inicial
def hallarVeloInicial():
    tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
    while(tiempo <= 0):
      print("!!El valor ingresado no corresponde a VARIACION DEL TIEMPO!!")
      tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
    distancia = float(input("Ingrese variacion de la distancia(metros): "))
    while(distancia <= 0):
      print("!!El valor ingresado no corresponde a VARIACION DE LA DISTANCIA!!")
      distancia = float(input("Ingrese variacion de la distancia(metros): "))
    aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
    while(aceleracion == 0):
      print("!!El valor ingresado no corresponde a ACELERACION!!")
      aceleracion = float(input("Ingrese la aceleración(metros/segundos al cuadrado): "))
    print("Hallando VELOCIDAD INICIAL .... : ")
    time.sleep(2)
    print("La velocidad inicial es: ",(distancia-((aceleracion/2)*tiempo**2))/tiempo,"m/s")

# Metodo para hallar la aceleracion
def hallarAceleracion():
    tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
    while(tiempo <= 0):
      print("!!El valor ingresado no corresponde a VARIACION DEL TIEMPO!!")
      tiempo = float(input("Ingrese variacion de tiempo(segundos): "))
    distancia = float(input("Ingrese variacion de la distancia(metros): "))
    while(distancia <= 0):
      print("!!El valor ingresado no corresponde a VARIACION DE LA DISTANCIA!!")
      distancia = float(input("Ingrese variacion de la distancia(metros): "))
    veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
    while(veloInicial < 0):
      print("!!El valor ingresado no corresponde a VELOCIDAD INICIAL!!") 
      veloInicial = float(input("Ingrese la velocidad inicial(metros/segundos): "))
    print("Hallando ACELERACION .... : ")
    time.sleep(2)
    print("La aceleracion es: ",2*(distancia-(veloInicial*tiempo))/tiempo**2,"m/s^2")  

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
elif(operacion == 3):
        print("Se ha seleccionado VELOCIDAD INICIAL")
        time.sleep(1)
        hallarVeloInicial()
else:
        print("Se ha seleccionado ACELERACION")
        time.sleep(1)
        hallarAceleracion()

