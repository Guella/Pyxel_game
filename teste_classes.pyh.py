# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 17:53:14 2025

@author: salma
"""
import pyxel
import sys
sys.path.append("C:/Users/salma/Documents/FURG/Algoritmos/Pyxel_game/")
sys.path.append("G:/Outros computadores/Meu computador/FURG/Algoritmos/Pyxel_game")
import variaveis as var

PER = []
MON = []


def update_entities(entities):
    for entity in entities:
        entity.update()
        
def draw_entities(entities):
    for entity in entities:
        entity.draw()
        
def cleanup_entities(entities):
    for i in range(len(entities) - 1, -1, -1):
        if not entities[i].is_alive:
            del entities[i]
            
class Player:
    def __init__(self, nome, x, y, classe, iniciativa, w = var.CHARACTER_W, h = var.CHARACTER_H):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.nome = nome
        self.newx = x
        self.newy = y
        self.iniciativa = iniciativa
        self.ehturno = False
        self.classe = classe
        self.selected = False
        self.movimento = 8
        self.casting = False
        PER.append(self)
    def update(self):
        pyxel.circb(self.x - self.w * 2 + 2, self.y - self.h * 2 + 2, self.movimento * 20, 12)

class Npc:
    def __init__(self, nome, x, y, iniciativa, w = var.CHARACTER_W, h = var.CHARACTER_H):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.nome = nome
        self.newx = x
        self.newy = y
        self.iniciativa = iniciativa
        self.ehturno = False
        self.movimento = 8
        self.casting = False
        MON.append(self)

class Magia:
    def __init__(self, nome, x, y, direcao):
        self.x = x
        self.y = y
        self.direcao = direcao
        self.atributos = var.HABILIDADES.loc[nome]
    def cast_magia(self):
        pass
        

class Menu_combate:
    def __init__(self):
        self.x = var.MENU_COMBATE_BORDA_XI
        self.y = var.MENU_COMBATE_BORDA_Y