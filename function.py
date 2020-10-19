import random
import os.path
import pickle
from classIns import *
from validation import *

__author__ = 'Eder Irineo Tassin - 77097'


def view_obj(vec):
    print('Lista de articulos')
    for i in vec:
        print(to_string(i))


def search(vec, x):
    izq, der = 0, len(vec) - 1
    while izq <= der:
        med = (izq + der) // 2
        if vec[med].nro_identificacion == x:
            print('\n')
            return print(to_string(vec[med]))

        if x < vec[med].nro_identificacion:
            der = med - 1
        else:
            izq = med + 1
    return print('\n No hay articulo')


def short(vec, obj):
    izq, der = 0, len(vec) - 1
    pos = 0
    while izq <= der:
        med = (izq + der) // 2
        if vec[med].nro_identificacion == obj.nro_identificacion:
            pos = med
            break

        if obj.nro_identificacion < vec[med].nro_identificacion:
            der = med - 1
        else:
            izq = med + 1

    if izq > der:
        pos = izq

    vec[pos:pos] = [obj]


def matriz(v):
    m = [[0] * 15 for i in range(20)]
    for i in range(len(v)):
        fila = v[i].pais
        columna = v[i].tipo_art
        m[fila][columna] += 1
    return m


def view_matriz(m, s):
    for j in range(20):
        for c in range(15):
            if m[j][c] != s:
                print("Pais de origen:", j, "Stock de articulo:", c)


def prom(vec):
    pr = 0
    for i in range(len(vec)):
        pr += vec[i].stock
    pr_r = pr // len(vec)
    return pr_r


def view_arch(file, prom_stock):
    if not os.path.exists(file):
        print('No existe ningun archivo')
        return

    m = open(file, 'rb')
    size = os.path.getsize(file)
    while m.tell() < size:
        register = pickle.load(m)
        if register.stock > prom_stock:
            print(to_string(register))

    m.close()


def generate_arc(vec, file, tipo_articulo):
    m = open(file, 'wb')
    for i in vec:
        if i.tipo_art == tipo_articulo:
            pickle.dump(i, m)
    m.close()


def generate(n, vec):
    for i in range(n):
        nom = ['juegute', 'florero', 'bazar', 'adorno', 'mueble']
        nro_identificacion = random.randint(1, 500)
        nombre_art = random.choice(nom)
        precio = random.randint(1, 15000)
        pais = random.randint(0, 19)
        tipo_art = random.randint(0, 14)
        stock = random.randint(0, 20)

        obj = MyClass(nro_identificacion, nombre_art, precio, pais, tipo_art, stock)
        short(vec, obj)
