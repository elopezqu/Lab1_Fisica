import time

# Método para hallar la distancia 
def hallarDistancia():
    tiempo = int(input("Ingrese el tiempo(segundos): "))
    if(tiempo > 0):
        velocidad = int(input("Ingrese la velocidad(metros/segundos): "))
        if(velocidad > 0):
            print("Hallando DISTANCIA .... : ")
            time.sleep(2)
            print("La distancia es:",velocidad*tiempo,"m")

# Método para hallar el tiempo 
def hallarTiempo():
    distancia = int(input("Ingrese la distancia(metros): "))
    if(distancia >= 0):
        velocidad = int(input("Ingrese la velocidad(metros/segundos): "))
        if(velocidad > 0):
            print("Hallando TIEMPO .... : ")
            time.sleep(2)
            print("El tiempo es:",distancia/velocidad,"s")


# Main
print("Bienvenido a su calculadora de MRU")
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
    



