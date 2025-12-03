'''
IES Alonso de Ercilla
Desarrollo de Aplicaciones Multiplataforma
Alumno: Rafa
'''

def calcular_total():
    pass

# Metodo para saludar
def saludar(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años") # Print imprime por pantalla


def pedir_nombre():
    nombre = input("Nombre de usuario: ")
    apellidos = input("Apellido de usuario: ")
    return nombre, apellidos

def sumar(a, b=0):
    return a + b

if __name__ == '__main__':
    print("inicio")

    suma = sumar(4)
    print(f"La suma es: {suma}")


    nombre, apellidos = pedir_nombre()
    print(nombre,apellidos)



    saludar("Rafa",20)
    lista = [3,6,1]
    print(lista[1])
    tupla = (1, 'a', True)
    print(tupla)
    diccionario = {'nombre': 'Juan', 'edad': 30}
    print(diccionario)

