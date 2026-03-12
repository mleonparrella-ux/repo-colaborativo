# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:50:11 2026

@author: ramon
"""

def registar_habitos():
    lista_actividades = []
    seguir = input("Desea ingresar actividad ")
    while seguir == "si":
        actividad = input("Ingrese actividad: ")
        lista_actividades.append(actividad)
        seguir = input("Desea ingresar actividad ")
    return lista_actividades

def analizar_habitos(lista):
    diccionario = {}
    for actividad in lista:
        if actividad not in diccionario:
            diccionario[actividad] = 1
        else:
            diccionario[actividad] += 1
    return diccionario

