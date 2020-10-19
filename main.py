from validation import *
from function import *

__author__ = 'Eder Tassin'

# Enunciado
# 1- Cargar los datos de n registros de tipo Artículo en un arreglo de registros (cargue n por teclado).
    # Puede cargar los datos manualmente, o puede generarlos aleatoriamente (pero si hace carga manual,
    # TODA la carga debe ser manual, y si la hace automática entonces TODA debe ser automática). El arreglo debe crearse de forma que
    # siempre quede ordenado de menor a mayor, según el número de identificación de los artículos, y para hacer esto debe aplicar el
    # algoritmo de inserción ordenada con búsqueda binaria. Se considerará directamente incorrecta la solución basada en cargar el arreglo
    # completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con búsqueda secuencial.
#
# 2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea.
#
# 3- Buscar en el arreglo creado en el punto 1 un registro en el cual el número de identificación del artículo sea igual a un valor
# p ingresado por el usuario. Si existe, mostrar por pantalla solamente: el nombre del artículo, tipo del artículo, y su stock.
# Si no existe, informar con un mensaje.
#
# 4- Usando el arreglo creado en el punto 1, determine el stock disponible de los artículos de cada
# posible país de procedencia por cada tipo posible (o sea, 20 * 15 acumuladores en una matriz de acumulación). Muestre sólo los
# resultados que tengan un stock superior a un valor s que se carga por teclado.
#
# 5- Guarde en un archivo los registros del arreglo cuyo tipo de artículo esté entre dos valores x e y que se cargan por teclado.


def menu():
    print('Menu de Opciones')
    print('1 - Generar los datos')
    print('2 - Buscar por numero de articulo')
    print('3 - Stock disponible de los artículos de cada posible país de procedencia por cada tipo posible')
    print('4 -  Guardaar archivo')
    print('5 -  Mostrar mat')
    print('0 - Salir')
    return int(input('Seleccione su Opcion: '))


def test():
    n = s = 0
    option = -1
    file = 'nombre.dat'
    vec = []

    while option != 0:
        option = menu()

        if option == 1:
            n = validation_1(0, 'Ingrese la cantidad da cargar: ')
            generate(n, vec)
            view_obj(vec)

        if vec:
            if option == 2:
                x = validation_1(0, 'Ingrese el numero que quiere buscar: ')
                search(vec, x)
            elif option == 3:
                s = validation_1(0, 'Stock mayor a: ')
                m = matriz(vec)
                view_matriz(m, s)
            elif option == 4:
                tipo_articulo = validation_2(0, 14, 'Ingrese el articulo (0 , 14): ')
                generate_arc(vec, file, tipo_articulo)
            elif option == 5:
                prom_stock = prom(vec)
                view_arch(file, prom_stock)

        else:
            print("\nDEBE GENERAR EL ARTCHIVO\n")


if __name__ == '__main__':
    test()
