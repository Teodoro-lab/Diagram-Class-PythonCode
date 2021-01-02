#!/usr/bin/python
#-*- coding: utf-8 -*-

class Naranja:
    def __init__(self, sabor, color, peso):
        self.sabor = sabor
        self.color = color
        self.peso = peso

    def hacer_Jugo(self, ):
        del(self)

Naranja1 = Naranja("1","2", 200)
print(Naranja1)
Naranja1.hacer_Jugo()
print(Naranja1.sabor)

