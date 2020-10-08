#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"


import csv
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
import mplcursors
import numpy as np

'''
NOTA PARA TODOS LOS EJERCICIOS

Para la resolución de todos los problemas utilizará
el dataset "ventas.csv".

Desde ahora los de datos los generará c/u
con Numpy o comprensión de listas o ambos, queda
a su elección en cada caso. Si quiere usar Numpy
para todo, puede abrir el archivo directamente con Numpy
y trabajar sin pasar por listas o diccionarios.

TIP: Para abrir el archivo CSV con Numpy y que el header no
     quede mezclado con los datos utilizar:
     data = np.genfromtxt('ventas.csv', delimiter=',')
     # Borro la fila 0 del header, los nombres de las columnas
     data = data[1:,:]

NO están permitidos los bucles en la realización de estos ejercicios.

Descripción del dataset "ventas.csv"
- Este dataset contiene el importe facturado por un local
  en la venta de sus productos dividido en 4 categorías
- Se contabiliza lo vendido por categória al cerrar el día,
  el dataset está ordenado por mes y día
- El dataset contiene 3 meses (genéricos) de 30 días c/u

'''


def ej1():
    print('Comenzamos a divertirnos!')

    '''
    Para comenzar a calentar en el uso del dataset se le solicita
    que grafique la evolución de la facturación de la categoría alimentos
    para el primer mes (mes 1) de facturación.
    Realice un line plot con los datos de facturación de alimentos del mes 1
    Deberá poder observar la evolución de ventas(y) vs días(x)

    TIP:
    1) Para aquellos que utilicen listas siempre primero deberan
    emprezar filtrando el dataset en una lista de diccionarios que
    posee solo las filas y columnas que están buscando.
    En este caso todas las filas cuyo mes = 1 y solo la columan
    de día(x) y de alimentos(y).
    Una vez que tiene esa lista de dccionarios reducida a la información
    de interés, debe volver a utilizar comprensión de listas para separar
    los datos de los días(x) y de los alimentos(y)

    2) Para aquellos que utilicen Numpy, si transformaron su CSV en Numpy
    les debería haber quedado una matriz de 6 columnas y de 90 filas
    (recordar sacar la primera fila que es el header)
    mes | dia | alimentos | bazar | limpieza | electrodomesticos
    Luego si quisieramos acceder a solo la columna de los dias (col=1)
    podemos utilizar slicing de Numpy:
    dias = dataset[:, 1]
    ¿Cómo puedo obtener las filas solo del primer mes?
    Aplicando mask de Numpy:
    mes_1 --> col = 0
    filas_mes_1 = dataset[:, 0] == 1
    Obtengo solos los datos del mes uno
    mes_1 = dataset[filas_mes_1, :]

    x --> dias
    Obtengo solo los dias del mes1 de alimentos
    x = dataset[filas_mes_1, 1]
    o tambien puede usar
    x = mes_1[:, 1]

    y --> alimentos
    Obtengo solo los alimentos del mes1 de alimentos
    y = dataset[filas_mes_1, 2]
    o tambien puede usar
    y = mes_1[:, 2]

    '''
    #lista_dias =[]
    with open('ventas.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
    
    x_dia = [int(data[i].get('Dia')) for i in range(len(data)) if int(data[i].get('Mes')) == 1]

    y_alimentos = [int(data[i].get('Alimentos')) for i in range(len(data)) if int(data[i].get('Mes')) == 1]

    fig = plt.figure('Evolución')
    ax = fig.add_subplot()

    ax.plot(x_dia, y_alimentos, color='red', label='Evolución alimentos')
    ax.set_title('"Evolución de la facturación de alimentos en el primer mes"')
    ax.set_facecolor('white')
    ax.set_xlabel('Días')
    ax.set_ylabel('Alimentos')
    ax.grid()
    mplcursors.cursor(multiple=False)
    ax.legend()

    plt.show()

    
def ej2():
    print('Comenzamos a ponernos serios!')

    '''
    Queremos visualizar como ver la tendencia de venta de los alimentos
    a lo largo de todo el año.
    Para eso queremos utilizar el método "np.diff" para obtener la diferencia
    día a día de lo vendido.

    Se debe poder primero discriminar las ventas por la categoría Alimentos,
    1) en el caso de usar listas se debe generar una lista de solo
       ventas de aliementos de todo el año.
    2) En el caso de usar numpy no hace falta generar una lista/array aparte,
       pero si le resulta comodo puede hacerlo.

    Luego que tienen discriminadas las ventas por alimento aplicar el método
    np.diff
    tendencia = np.diff(mis ventas de alimentos)

    Graficar el valor obtenido con un Line Plot

    NOTA: Importante!, en este caso no disponen facilmente del eje "X" de diff,
    para simplificar el caso solamente graficar la variable "tendencia"
    plot(tendencia)

    '''
    with open('ventas.csv') as csvfile:
        data = list(csv.DictReader(csvfile))

    y_alimentos = [int(data[i].get('Alimentos')) for i in range(len(data))]

    tendencia = np.diff(y_alimentos)

    fig = plt.figure('Venta alimentos')
    ax = fig.add_subplot()

    ax.plot(tendencia, color='red', label='Tendencia')
    ax.set_title('"Tendencia de venta de los alimentos a lo largo de todo el año"')
    ax.set_facecolor('lightyellow')
    ax.set_ylabel('Tendencia')
    ax.grid()
    mplcursors.cursor(multiple=False)
    ax.legend()

    plt.show()
      
def ej3():
    print("Buscando la tendencia")

    '''
    Si observa el dataset, los electrodomésticos no siempre
    tienen facturación al finalizar el día.
    Deseamos que generen una nueva lista/array/columna
    en la cual coloquen un "1" si ese día se vendió electrodomésticos
    o un "0" sino se vendio nada (facturación = 0).
    Luego graficar utilizando Line Plot esta nueva lista/array/columna
    para visualizar la tendencia de cuantos días consecutivos hay
    ventas de electrodomésticos.

    '''

    with open('ventas.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
    
    electrodomesticos = [int(data[i].get('Electrodomesticos')) for i in range(len(data))]

    filter_electrod = [x if x == 0 else 1 for x in electrodomesticos]

    fig = plt.figure('Tendencia')
    ax = fig.add_subplot()

    ax.plot(filter_electrod, color='blue', label='Tendencia de ventas de electrodomésticos')
    ax.set_title('"Venta de electrodomesticos"')
    ax.set_facecolor('whitesmoke')
    ax.set_ylabel('Tendencia')
    ax.grid()
    ax.legend()

    plt.show()

   
def ej4():
    print("Exprimiendo los datos")

    '''
    Obtener la facturación total (la suma total en los 3 meses)
    de cada categória por separado. Nos debe quedar el total
    facturado en alimentos, en bazar, en limpieza y en
    electrodomesticos por separado (son 4 valores)

    TIP:
    1) para los que usan listas, para poder obtener estos
    valores primero deberan generar una lista de cada categoría,
    para luego poder aplicar operaciones como sum.
    2) Para los que usan numpy pueden usar directamente np.sum
    y especificando el axis=0 estarán haciendo la suma total de la columna

    Con la información obtenida realizar un Pie Plot
    para visualizar que categoría facturó más en lo que va
    del año
    '''

    with open('ventas.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
    
    electrodomesticos = [int(data[i].get('Electrodomesticos')) for i in range(len(data))]
    
    alimentos = [int(data[i].get('Alimentos')) for i in range(len(data))]
    
    bazar = [int(data[i].get('Bazar')) for i in range(len(data))]

    limpieza = [int(data[i].get('Limpieza')) for i in range(len(data))]
    
    suma ={'Electrodomesticos': sum(electrodomesticos), 'Alimentos': sum(alimentos), 'Bazar': sum(bazar), 'Limpieza': sum(limpieza)}

    fig = plt.figure('Facturación')
    fig.suptitle('"Facturación total"', fontsize=16)
    ax = fig.add_subplot()

    explode = (0.1, 0, 0, 0)

    ax.pie(suma.values(), labels= suma.keys(), explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')

    plt.show()
    
def venta(categoria, mes):
    
    with open('ventas.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
    
        return [int(data[i].get(categoria)) for i in range(len(data)) if int(data[i].get('Mes')) == mes]
       
                

def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Ahora que ya hemos jugado un poco con nuestro dataset,
    queremos realizar 3 gráficos de columnas en una misma figura
    Cada gráfico de columnas deben tener 4 columnas que representan
    el total vendido de cada categoría al final del mes.
    Para poder hacer este ejercicio deben obtener primero
    total facturado por categoria por mes (deben filtrar por mes)
    Es parecido a lo realizado en el ejercicio anterior pero en vez
    de todo el año es la suma total por mes por categoría.

    Siendo que son 4 categorías y 3 meses, deben obtener al final
    12 valores, con esos 12 valores construir 3 listas/arrays
    para poder mostrar los 3 gráficos de columnas

    BONUS Track: Si están cancheros y aún quedan energías para practicar,
    les proponemos que en vez de realizar 3 gráficos de columnas separados
    realicen uno solo y agrupen la información utilizando gráfico de barras
    apilados o agrupados (a su elección)
    '''
        
    #-----------------LISTA PRIMER MES-------------------
    
    electrodomesticos = venta(categoria='Electrodomesticos', mes= 1)
        
    alimentos = venta(categoria='Alimentos', mes= 1)
        
    bazar = venta(categoria='Bazar', mes= 1)

    limpieza = venta(categoria='Limpieza', mes= 1)
    
    #-----------------LISTA SEGUNDO MES-------------------
    
    electrodomesticos2 = venta(categoria='Electrodomesticos', mes= 2)
        
    alimentos2 = venta(categoria='Alimentos', mes= 2)
        
    bazar2 = venta(categoria='Bazar', mes= 2)

    limpieza2 = venta(categoria='Limpieza', mes= 2)
    #----------------- LISTA TERCER MES-------------------

    electrodomesticos3 = venta(categoria='Electrodomesticos', mes= 3)
        
    alimentos3 = venta(categoria='Alimentos', mes= 3)
        
    bazar3 = venta(categoria='Bazar', mes= 3)

    limpieza3 = venta(categoria='Limpieza', mes= 3)

    #----------------- LISTA SUMA POR MES-------------------
    ventas = np.array([1, 2, 3, 4])
    ventas_label = ['Electrodomesticos', 'Alimentos', 'Bazar', 'Limpieza']
    suma_mes1 = [sum(electrodomesticos), sum(alimentos), sum(bazar), sum(limpieza)]
    suma_mes2 = [sum(electrodomesticos2), sum(alimentos2), sum(bazar2), sum(limpieza2)]
    suma_mes3 = [sum(electrodomesticos3), sum(alimentos3), sum(bazar3), sum(limpieza3)]
    
    #------------GRÁFICO DE COLUMNAS-----------
    width = 0.2
    fig = plt.figure('Reporte de ventas por mes')
    fig.suptitle('"Total vendido a final de mes"', fontsize=16)
    ax = fig.add_subplot()

    ax.bar(ventas, suma_mes1, width=width, label='Primer mes', color='violet')
    ax.bar(ventas + width, suma_mes2, width=width, label='Segundo mes', color='grey')
    ax.bar(ventas + 2*width, suma_mes3, width=width, label='Tercer mes', color='cyan')
    ax.set_facecolor('whitesmoke')
    ax.legend()
    ax.set_xticks(ventas + width / 3)
    ax.set_xticklabels(ventas_label)
    
    plt.show(block=False)
    
    #-------APILADOS-------------------
    fig = plt.figure('Ventas final de mes')
    fig.suptitle('"Total vendido a final de mes"', fontsize=16)
    ax = fig.add_subplot()

    ax.bar(ventas_label, suma_mes1, label='Primer mes', color='brown')
    ax.bar(ventas_label, suma_mes2, bottom= suma_mes1, label='Segundo mes', color='pink')
    ax.bar(ventas_label, suma_mes3, bottom= [sum(x) for x in zip(suma_mes1, suma_mes2)], label='Tercer mes', color='darkblue')
    ax.set_facecolor('white')
    ax.legend()
       
    plt.show()

if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    #ej2()
    #ej3()
    #ej4()
    categoria = ''
    mes = int()
    #ej5()
    
