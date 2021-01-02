#!/usr/bin/python
# -*- coding: utf-8 -*-
from Naranja import Naranja

naranjaDulce = Naranja("Dulce", "Amarillo", 200)
print(naranjaDulce.sabor)


class Canasta:
    def __init__(self):
        self.capacidadDeNaranjas = 100
        self.Naranjas = []

    def añadir_Naranja(self, ):
        numNaranjas = int(
            input("Ingrese el numero de naranjas que desea agregar: "))

        for i in range(numNaranjas):
            sabor = input("\nIngrese el sabor de la naranja: ")
            color = input("\nIngrese el color de la naranja: ")
            peso = int(input("\nIngrese el peso de la naranja: "))
            nuevaNaranja = Naranja(peso, color, peso)
            self.Naranjas.append(nuevaNaranja)

    def quitar_Naranja(self, ):
        pass


canasta1 = Canasta()
canasta1.añadir_Naranja()

print("\n", canasta1.Naranjas[0].sabor,
      canasta1.Naranjas[0].color,
      canasta1.Naranjas[0].peso)
