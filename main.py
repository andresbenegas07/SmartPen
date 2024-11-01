from class_boligrafo import *

boligrafo_1 = Boligrafo("Fino", "Oro")
boligrafo_2 = Boligrafo("Grueso", "Azul")
boligrafo_3 = Boligrafo("Fino", "Amarillo")
boligrafo_4 = Boligrafo("Fino", "Boca")
boligrafo_5 = Boligrafo("Grueso", "Dorado")

boligrafo_1.mostrar_cantidad_de_tinta()
boligrafo_1.escribir("Hola, me llamo Andres")
boligrafo_1.mostrar_cantidad_de_tinta()

boligrafo_1.recargar(5)
boligrafo_1.recargar(40)



lista_boligrafos = [boligrafo_1, boligrafo_2, boligrafo_3, boligrafo_4, boligrafo_5]

def mostrar_boligrafos(lista):
    for i in range(len(lista)):
        print()
        print(f"El boligrafo {i + 1}")
        print(f"El grosor de punta es: {lista[i].mostrar_grosor_punta()}")
        print(f"El color es: {lista[i].mostrar_color()}")
        print(f"La cantidad de tinta es de: {lista[i].mostrar_cantidad_de_tinta()}")
        print()
    


mostrar_boligrafos(lista_boligrafos)


def poner_a_escribir(lista):
    boligrafos_gastados = []

    while len(boligrafos_gastados) == 0 :
        for i in range(len(lista)):
            lista[i].escribir("*")
            if lista[i].cantidad_tinta() == 0:
                boligrafos_gastados.append(lista[i])
                lista.remove(lista[i])
    
    for i in range(len(boligrafos_gastados)):
        boligrafos_gastados[i].recargar(30)
