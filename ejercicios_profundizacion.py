#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
import mplcursors  # [Opcional cursores]


def ej1():
    # Line Plot
    # Se desea graficar tres funciones en una misma figura
    # en tres gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = list(range(-10, 11, 1))

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # Utilizar comprension de listas para generar
    # y1, y2 e y3 basado en los valores de x

    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    # graf1
    # ------
    # graf2    
    # ------
    # graf3
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "3 filas" "1 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    y1 = [i ** 2 for i in x]
    y2 = [i ** 3 for i in x]
    y3 = [i ** 4 for i in x]

    fig = plt.figure()
    ax1 = fig.add_subplot(3, 1, 1)
    ax2 = fig.add_subplot(3, 1, 2)
    ax3 = fig.add_subplot(3, 1, 3)

    ax1.plot(x, y1, color='black', label='y=x**2')
    ax1.set_facecolor('lavender')
    ax1.set_xlabel('Eje x')
    ax1.set_ylabel('Eje y')
    ax1.legend()
    
    ax2.plot(x, y2, color='red', label='y=x**3')
    ax2.set_facecolor('mintcream')
    ax2.set_xlabel('Eje x')
    ax2.set_ylabel('Eje y')
    ax2.legend()
    
    ax3.plot(x, y3, color='green', label='y=x**4')
    ax3.set_facecolor('papayawhip')
    ax3.set_xlabel('Eje x')
    ax3.set_ylabel('Eje y')
    ax3.legend()

    plt.show()


def ej2():
    # Scatter Plot
    # Se desea graficar dos funciones en una misma figura
    # en dos gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = np.arange(0, 4*np.pi, 0.1)

    # Realizar dos gráficos que representen
    # y1 = sin(x)
    # y2 = cos(x)
    # Utilizar los métodos de Numpy para calcular
    # "y1" y "y2" basado en los valores de x

    # Esos dos gráficos deben estar colocados
    # en la diposición de 1 fila y 2 columnas:
    # ------
    #  graf1 | graf2
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "1 fila" "2 columnas" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un mark distinto
    # a su elección.

    y1 = np.sin(x)
    y2 = np.cos(x)

    fig = plt.figure()

    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.plot(x, y1, color='black', label='y=sin(x)',  marker='.')
    ax1.set_title('sin(x)')
    ax1.set_facecolor('bisque')
    ax1.set_xlabel('Valores de x')
    ax1.set_ylabel('Valores de y')
    ax1.legend()

    ax2.plot(x, y1, color='red', label='y=cos(x)', marker='^')
    ax2.set_title('cos(x)')
    ax2.set_facecolor('lightgrey')
    ax2.set_xlabel('Valores de x')
    ax2.set_ylabel('Valores de y')
    ax2.legend()

    plt.show()

def ej3():
    # Bar Plot
    # Generar un gráfico de barras simple a partir
    # de la siguiente información:

    lenguajes = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
    performance = [10, 8, 6, 4, 2, 1]

    # Realizar un gráfico de barras en donde se pueda ver el uso
    # de cada lenguaje, se debe utilizar los labels "lenguajes"
    # como valor del eje X

    # Se debe colocar título al gráfico.
    # Se debe cambiar la grilla y el fondo a su elección.

    fig = plt.figure('Uso de los lenguajes')
    fig.suptitle('"Uso de los lenguajes de programación"', fontsize=16)
    ax = fig.add_subplot()
   
    ax.bar(lenguajes, performance, label='Lenguajes', color='violet')
    ax.set_facecolor('lightyellow')
    ax.grid(ls='dashed')
    ax.set_xlabel('Lenguajes de programación')
    ax.set_ylabel('Uso de cada lenguaje')
    ax.legend()

    plt.show()

def ej4():
    # Pie Plot
    # Se desea realizar un gráfico de torta con la siguiente
    # información acerca del % de uso de lenguajes en nuevos
    # programadores
    uso_lenguajes = {'Python': 29.9, 'Javascript': 19.1,
                     'Go': 16.2, 'Java': 10.5, 'C++': 10.2,
                     'C#': 8.2, 'C': 5.9
                     }

    # El gráfico debe tener usar como label las keys del diccionario,
    # debe usar como datos los values del diccionario
    # Se desea resaltar (explode) el dato de Python
    # Se desea mostrar en el gráfico los porcentajes de c/u
    # Se debe colocar un título al gráfico

    
    fig = plt.figure('Gráfico Pie')
    fig.suptitle('"Uso de los lenguajes de programación"', fontsize=16)
    ax = fig.add_subplot()

    explode = (0.1, 0, 0, 0, 0, 0, 0)

    ax.pie(uso_lenguajes.values(), labels=uso_lenguajes.keys(), explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')

    plt.show()



def ej5():
    # Uso de múltiples líneas en un mismo gráfico (axes)
    # En el siguiente ejemplo generaremos una señal senoidal
    # haciendo uso solamente de comprension de listas
    step = 0.1
    sample_size = 100
    signal = [{'X': i*step, 'Y': math.sin(i*step)} for i in range(sample_size)]

    # Se generó una lista de diccionarios con dos columnas "X" e "Y"
    # que corresponden a los valores de nuestra señal senoidal.
    # Se pide usar comprensión de listas para generar las dos listas
    # por separado de los valoresde "X" e "Y" para poder utilizar
    # el line plot y observar la señal
   
    signal_x = [data['X'] for data in signal]
    signal_y = [data['Y'] for data in signal]
 
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(signal_x, signal_y, c='red')
    ax.set_title('"Señal senoidal"')
    ax.set_facecolor('mintcream')
    ax.set_xlabel('Eje x')
    ax.set_ylabel('Eje y')
    ax.grid()
    
    plt.show(block=False)

    # Ahora que han visto la señal senoidal en su gráfico, se desea
    # que generen otras dos listas de "X" e "Y" pero filtradas por
    # el valor de "Y". Solamente se debe completar la lista
    # con aquellos valores de "Y" cuyo valor absoluto (abs)
    # supere 0.7

    filter_signal_x = [data['X'] for data in signal if abs(data['Y']) > 0.7]
    filter_signal_y = [data['Y'] for data in signal if abs(data['Y']) > 0.7]

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.scatter(filter_signal_x, filter_signal_y, c='blue')
    ax.set_title('"Señal senoidal filtrada"')
    ax.set_facecolor('mintcream')
    ax.set_xlabel('Eje x')
    ax.set_ylabel('Eje y')
    ax.grid()
    
    plt.show(block=False)
    # Graficar juntas ambos conjuntos de listas y observar
    # el resultado. Graficar filter como scatter plot

    # plot(signal_x, signal_y)
    # scatter(filter_signal_x, filter_signal_y)

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(signal_x, signal_y, color='red', label='signal')
    ax.scatter(filter_signal_x, filter_signal_y, color='blue', label='filter_signal')
    ax.set_title('"Señal senoidal"')
    ax.set_facecolor('mintcream')
    ax.set_xlabel('Eje x')
    ax.set_ylabel('Eje y')
    ax.grid()
    ax.legend()
    plt.show()

    # Pueden ver el concepto y la utilidad de
    # realizar un gráfico encima de otro para filtrar datos?
    #ES DE UTILIDAD PARA COMPARAR DATOS Y PODER VISUALIZAR LAS DIFERENCIAS.

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
