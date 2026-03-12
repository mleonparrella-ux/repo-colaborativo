# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:52:05 2026

@author: mom
"""
import funciones_habitos

lista = funciones_habitos.registar_habitos()
diccio = funciones_habitos.analizar_habitos(lista)
print("Resumen de actividades: ")
print(diccio)