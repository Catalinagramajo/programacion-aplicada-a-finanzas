#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 13:27:38 2023

@author: catalinagramajo
"""

#object es la clase principal (madre de todas las clases) == todo depende de object
#al crear un objeto, se crea automaticamente el diccionario con el nombre __dict__

# class A(object): == class A(): == class A: SON LO MISMO

class A():
    x = 23 # agrego atributo 1
class B(A):
    y = 30 # agrego atributo 2
    x = 12 # la ultima definicion es la que prevalece, por eso ese valor es el ultimo 

z = B() # z es una instancia de la clase A

# dentro de los objetos, hay diccionarios

#print (z.__dict__['x']) # pido que dentro del diccionario me busque el atributo 'x'.

# PARA CREAR INSTANCIAS DE CLASES
class A:
    x = 23
class B(A):
    y = 40
    def _init_(self, value): #sirve cada vez que quiero tener atributos asociados a una clase 
    #paso una funcion (1er argumento = self, 2do arg = value)
        self.z = value  #a esa funcion le paso un atributo 
        # el self es para definir que es el diccionario de z y 
        #que se guarde el objeto (el diccionario en z)
        # EL INIT METHOD NO LLEVA RETURN!!!!!! sino da error
        
        