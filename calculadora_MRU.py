import time
#∆x = v × ∆t

# Método para hallar la variación de la distancia 
def hallarDistancia():
    tiempo = float(input("Ingrese la variación del tiempo(segundos): ")) 
    while(tiempo <= 0):
        print("El valor ingresado no corresponde a VARIACIÓN DEL TIEMPO")
        tiempo = float(input("Ingrese la variacion del tiempo(segundos): "))
    velocidad = float(input("Ingrese la velocidad(metros/segundos): "))
    while(velocidad <= 0):
        print("El valor ingresado no corresponde a VELOCIDAD")
        velocidad = float(input("Ingrese la velocidad(metros/segundos): "))
    print("Hallando VARIACIÓN DE LA DISTANCIA .... : ")
    time.sleep(2)
    print("la variación de la distancia es:", velocidad * tiempo, "m")


# Método para hallar el tiempo 
def hallarTiempo():
    distancia = float(input("Ingrese la variación de la distancia(metros): "))
    while(distancia <= 0):
        print("El valor ingresado no corresponde a VARIACIÓN DE LA DISTANCIA")
        distancia = float(input("Ingrese la variación de la distancia(metros): "))
    velocidad = float(input("Ingrese la velocidad(metros/segundos): "))
    while(velocidad <= 0):
        print("El valor ingresado no corresponde a VELOCIDAD")
        velocidad = float(input("Ingrese la velocidad(metros/segundos): "))
    print("Hallando VARIACIÓN DEL TIEMPO .... : ")
    time.sleep(2)
    print("El tiempo es:", distancia / velocidad, "s")

# Método para hallar la velocidad 
def hallarVelocidad():
    distancia = float(input("Ingrese la variación de la variación de la distancia(metros): "))
    while(distancia <= 0):
        print("El valor ingresado no corresponde a VARIACIÓN DE LA DISTANCIA")
        distancia = float(input("Ingrese la variación de la distancia(metros): "))
    tiempo = float(input("Ingrese la variación del tiempo(segundos): "))
    while(tiempo <= 0):
        print("El valor ingresado no corresponde a VARIACIÓN DEL TIEMPO")
        tiempo = float(input("Ingrese la variación del tiempo(segundos): "))
    print("Hallando VELOCIDAD .... : ")
    time.sleep(2)
    print("La velocidad es:", distancia / tiempo, "m/s")


# Main
print("Bienvenido a su calculadora de MRU")
print("Cual es su incognita: ")
print("1) Variación de la distancia")
print("2) Variación del tiempo")
print("3) Velocidad")
operacion = int(input("Ingrese el número de su incognita: "))
while(operacion != 1 and operacion != 2 and operacion != 3 ):
    print("!!Número de incognita no disponible!!")
    print("Cual es su incognita: ")
    print("1) Variación de la distancia")
    print("2) Variación del tiempo")
    print("3) Velocidad")
    operacion = int(input("Ingrese el número de su incognita: "))
if(operacion==1):
    print("Se ha seleccionado VARIACIÓN DE LA DISTANCIA")
    time.sleep(1)
    hallarDistancia()
elif(operacion == 2):
    print("Se ha seleccionado VARIACIÓN DEL TIEMPO")
    time.sleep(1)
    hallarTiempo()
else:
    print("Se ha seleccionado VELOCIDAD")
    time.sleep(1)
    hallarVelocidad()
      
