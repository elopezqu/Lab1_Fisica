import time

# Método para hallar la distancia 
def hallarDistancia():
    tiempo = float(input("Ingrese el tiempo (segundos): "))
    if tiempo > 0:
        velocidad = float(input("Ingrese la velocidad (metros/segundos): "))
        if velocidad > 0:
            print("Hallando DISTANCIA .... : ")
            time.sleep(2)
            print("La distancia es:", velocidad * tiempo, "m")
        else:
            while velocidad <= 0:
                print("El valor ingresado no se puede ingresar a VELOCIDAD")
                velocidad = float(input("Ingrese la velocidad (metros/segundos): "))
            print("Hallando DISTANCIA .... : ")
            time.sleep(2)
            print("La distancia es:", velocidad * tiempo, "m")
    else:
        while tiempo <= 0:
            print("El valor ingresado no se puede ingresar a TIEMPO")
            tiempo = float(input("Ingrese el tiempo (segundos): "))
        velocidad = float(input("Ingrese la velocidad (metros/segundos): "))
        if velocidad > 0:
            print("Hallando DISTANCIA .... : ")
            time.sleep(2)
            print("La distancia es:", velocidad * tiempo, "m")
        else:
            while velocidad <= 0:
                print("El valor ingresado no se puede ingresar a VELOCIDAD")
                velocidad = float(input("Ingrese la velocidad (metros/segundos): "))
            print("Hallando DISTANCIA .... : ")
            time.sleep(2)
            print("La distancia es:", velocidad * tiempo, "m")


# Método para hallar el tiempo 
def hallarTiempo():
    distancia = float(input("Ingrese la distancia (metros): "))
    if distancia >= 0:
        velocidad = float(input("Ingrese la velocidad (metros/segundos): "))
        if velocidad > 0:
            print("Hallando TIEMPO .... : ")
            time.sleep(2)
            print("El tiempo es:", distancia / velocidad, "s")
        else:
            while velocidad <= 0:
                print("El valor ingresado no se puede ingresar a VELOCIDAD")
                velocidad = float(input("Ingrese la velocidad (metros/segundos): "))
            print("Hallando TIEMPO .... : ")
            time.sleep(2)
            print("El tiempo es:", distancia / velocidad, "s")
    else:
        while distancia < 0:
            print("El valor ingresado no se puede ingresar a DISTANCIA")
            distancia = float(input("Ingrese la distancia (metros): "))
        velocidad = float(input("Ingrese la velocidad (metros/segundos): "))
        if velocidad > 0:
            print("Hallando TIEMPO .... : ")
            time.sleep(2)
            print("El tiempo es:", distancia / velocidad, "s")
        else:
            while velocidad <= 0:
                print("El valor ingresado no se puede ingresar a VELOCIDAD")
                velocidad = float(input("Ingrese la velocidad (metros/segundos): "))
            print("Hallando TIEMPO .... : ")
            time.sleep(2)
            print("El tiempo es:", distancia / velocidad, "s")

# Método para hallar la velocidad 
def hallarVelocidad():
    distancia = float(input("Ingrese la distancia (metros): "))
    if distancia >= 0:
        tiempo = float(input("Ingrese el tiempo (segundos): "))
        if tiempo > 0:
            print("Hallando VELOCIDAD .... : ")
            time.sleep(2)
            print("La velocidad es:", distancia / tiempo, "m/s")
        else:
            while tiempo <= 0:
                print("El valor ingresado no se puede ingresar a TIEMPO")
                tiempo = float(input("Ingrese el tiempo (segundos): "))
            print("Hallando VELOCIDAD .... : ")
            time.sleep(2)
            print("La velocidad es:", distancia / tiempo, "m/s")
    else:
        while distancia < 0:
            print("El valor ingresado no se puede ingresar a DISTANCIA")
            distancia = float(input("Ingrese la distancia (metros): "))
        tiempo = float(input("Ingrese el tiempo (segundos): "))
        if tiempo <= 0:
            print("Hallando VELOCIDAD .... : ")
            time.sleep(2)
            print("La velocidad es:", distancia / tiempo, "m/s")
        else:
            while tiempo <= 0:
                print("El valor ingresado no se puede ingresar a TIEMPO")
                tiempo = float(input("Ingrese el tiempo (segundos): "))
            print("Hallando VELOCIDAD .... : ")
            time.sleep(2)
            print("La velocidad es:", distancia / tiempo, "m/s")

# Main
print("Bienvenido a su calculadora de MRU")
print("Cual es su incognita: ")
print("1) Distancia")
print("2) Tiempo")
print("3) Velocidad")
operacion = int(input("Ingrese el número de su incognita: "))
while(operacion != 1 and operacion != 2 and operacion != 3 ):
    print("!!Número de incognita no disponible!!")
    print("Cual es su incognita: ")
    print("1) Distancia")
    print("2) Tiempo")
    print("3) Velocidad")
    operacion = int(input("Ingrese el número de su incognita: "))
if(operacion==1):
    print("Se ha seleccionado DISTANCIA")
    time.sleep(1)
    hallarDistancia()
else:
    if(operacion == 2):
        print("Se ha seleccionado TIEMPO")
        time.sleep(1)
        hallarTiempo()
    else:
        print("Se ha seleccionado VELOCIDAD")
        time.sleep(1)
        hallarVelocidad()
      
