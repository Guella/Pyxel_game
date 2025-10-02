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
#from .variaveis import * as var

MENU_COMBATE_I = [var.MENU_COMBATE_BORDA_Y + 10, var.MENU_COMBATE_BORDA_XI + 40]
MENU_COMBATE_II = [MENU_COMBATE_I[0] + 20, MENU_COMBATE_I[1]]
MENU_COMBATE_III = [MENU_COMBATE_I[0], MENU_COMBATE_I[1] + 50]
MENU_COMBATE_IV = [MENU_COMBATE_I[0] + 20, MENU_COMBATE_I[1] + 50]


ICONES = {
    "floresta": [0,8,104, 8, 8, 0],
    }


MENU_LETRAS = {
	"A": [2, 0, 5, 6, 7],
	"B": [2, 12, 5, 6, 7],
	"C": [2, 24, 5, 6, 7],
	"D": [2, 36, 5, 6, 7],
	"E": [2, 48, 5, 6, 7],
	"F": [2, 60, 5, 6, 7],
	"G": [2, 72, 5, 6, 7],
	"H": [2, 84, 5, 6, 7],
	"I": [2, 96, 5, 6, 7],
	"J": [2, 108, 5, 6, 7],
	"K": [2, 120, 5, 6, 7],
	"L": [2, 132, 5, 6, 7],
	"M": [2, 144, 5, 9, 7],
	"N": [2, 0, 41, 6, 7],
	"O": [2, 12, 41, 6, 7],
	"P": [2, 24, 41, 6, 7],
	"Q": [2, 36, 41, 6, 7],
	"R": [2, 48, 41, 6, 7],
	"S": [2, 60, 41, 6, 7],
	"T": [2, 72, 41, 6, 7],
	"U": [2, 84, 41, 6, 7],
	"V": [2, 96, 41, 6, 7],
	"W": [2, 108, 41, 9, 7],
	"X": [2, 120, 41, 6, 7],
	"Y": [2, 132, 41, 6, 7],
	"Z": [2, 144, 41, 6, 7],
	"a": [2, 0, 24, 8, 7],
	"b": [2, 12, 24, 8, 7],
	"c": [2, 24, 24, 6, 7],
	"d": [2, 36, 24, 8, 7],
	"e": [2, 48, 24, 8, 7],
	"f": [2, 60, 24, 8, 7],
	"g": [2, 72, 26, 8, 7],
	"h": [2, 84, 24, 8, 7],
	"i": [2, 96, 24, 5, 7],
	"j": [2, 108, 24, 8, 7],
	"k": [2, 120, 24, 8, 7],
	"l": [2, 132, 24, 5, 7],
	"m": [2, 144, 24, 8, 7],
	"n": [2, 0, 59, 8, 7],
	"o": [2, 12, 59, 8, 7],
	"p": [2, 24, 59, 8, 7],
	"q": [2, 36, 59, 8, 7],
	"r": [2, 48, 59, 8, 7],
	"s": [2, 60, 59, 8, 7],
	"t": [2, 72, 59, 6, 7],
	"u": [2, 84, 59, 8, 7],
	"v": [2, 96, 59, 8, 7],
	"w": [2, 108, 59, 8, 7],
	"x": [2, 120, 59, 8, 7],
	"y": [2, 132, 59, 8, 7],
	"z": [2, 144, 59, 8, 7]
}

TITULO = "Gauderio's Gate"

pyxel.init(var.TELA_LARGURA, var.TELA_ALTURA)
pyxel.load("mygame.pyxres")

class Cursor:
    pass

def desenha_opcoes(menu_pos, texto):
    pos_y = menu_pos[0]
    pos_x = menu_pos[1]
    for letra in texto:
        pyxel.blt(pos_x, pos_y,MENU_LETRAS[letra][0], MENU_LETRAS[letra][1], 
                     MENU_LETRAS[letra][2], MENU_LETRAS[letra][3], MENU_LETRAS[letra][4], 0)
        pos_x += MENU_LETRAS[letra][3]
    

def desenha_menu():
    pyxel.rect(0, var.MENU_COMBATE_BORDA_Y, var.MENU_COMBATE_BORDA_XF, var.TELA_ALTURA, col = 1)
    desenha_opcoes(MENU_COMBATE_I, "Atacar")
    desenha_opcoes(MENU_COMBATE_II, "Skills")
    desenha_opcoes(MENU_COMBATE_III, "Itens")
    desenha_opcoes(MENU_COMBATE_IV, "Fugir")

def define_iniciativa(lista_personagens):
    return sorted(lista_personagens, key = lambda personagem: personagem.iniciativa)        
    pass
        
def ordem_combate(lista_personagens):
    pyxel.blt(var.TURNO_X, var.TURNO_Y, 0, 0, 0, 8, 8, colkey = 0)
    pyxel.blt(var.TURNO_X + 18, var.TURNO_Y, 0, var.MONSTRO_DESENHO["Dragao"][0], var.MONSTRO_DESENHO["Dragao"][1], var.MONSTRO_DESENHO["Dragao"][2],
              var.MONSTRO_DESENHO["Dragao"][3], colkey = 0)
    pass

def desenha_monstro(x,y,nome):
    pyxel.blt(x, y, 0, var.MONSTRO_DESENHO[nome][0], var.MONSTRO_DESENHO[nome][1], var.MONSTRO_DESENHO[nome][2], var.MONSTRO_DESENHO[nome][3], colkey = 0)

def draw_chacter(x,y):
    pyxel.blt(x, y, 0, 0, 0, 8, 8, colkey = 0)
    pass

class Spell:
    def __init__(self, nome):
        self.nome = nome
        self.casted = False
        self.x = 0
        self.y = 0
        self.damage = 10

class Menu:
    def __init__(self):
        self.x = var.TELA_LARGURA/2
        self.y = var.TELA_ALTURA/4
        

class Personagem:
    def __init__(self, nome, x, y, w = var.CHARACTER_W, h = var.CHARACTER_H, iniciativa = 1):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.nome = nome
        self.newx = x
        self.newy = y
        self.movendo = False
        self.ehturno = False
        self.iniciativa = iniciativa
        
    def __repr__(self):
        return f"Personagem(nome='{self.nome}', iniciativa={self.iniciativa}"


class NPC(Personagem):
    def __init__(self, nome, x, y, tipo, w = var.CHARACTER_W, h = var.CHARACTER_H, iniciativa = 1):
        super().__init__(nome, x, y, iniciativa)
        self.movendo = False
        self.ehturno = False
        self.tipo = tipo
        self.w = var.MONSTRO_DESENHO[nome][2]
        self.h = var.MONSTRO_DESENHO[nome][3]
    def update(self):
        desenha_monstro(self.x, self.y, self.nome)
       

class Player(Personagem):
    def __init__(self, nome, x, y, classe, w = var.CHARACTER_W, h = var.CHARACTER_H):
        super().__init__(nome, x, y, w = var.CHARACTER_W, h = var.CHARACTER_H)
        self.movendo = False
        self.ehturno = False
        self.classe = classe
        self.selected = False
        self.movimento = 8
        self.casting = False
    def desenha_area_mov(self):
        if self.selected == True and self.movimento > 0:
            pyxel.circb(self.x + (self.w/2), self.y + (self.h/2), self.movimento * 5, 12)
    def delineate(self):
        if self.selected == True:
            pyxel.rectb(self.x, self.y - 1, self.w + 1, self.h + 2, 7)
    def update(self):
        draw_chacter(self.x, self.y)
        self.desenha_area_mov()
        if self.selected == True and self.movendo == False:
            if not (pyxel.mouse_x in range(self.x - self.h , self.x + self.h) and pyxel.mouse_y in range(self.y - self.w, self.y + self.w)):
                if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and self.selected == True:
                    self.movendo = True
                    self.newx = pyxel.mouse_x
                    self.newy = pyxel.mouse_y
        if self.movendo == True:
            if self.newx != self.x or self.newy != self.y:
                if self.newx < self.x:
                    self.x = self.x - 1                    
                elif self.newx > self.x:
                    self.x = self.x + 1
                if self.newy < self.y:
                    self.y = self.y - 1
                elif self.newy > self.y:
                    self.y = self.y + 1
            else:
                self.movendo = False
        
    def cast_spell(self, enemy_list):
        if self.movendo == False:
            if self.selected == True and pyxel.btn(pyxel.KEY_C) and self.casting == False:
                if pyxel.mouse_x in enemy_list.x and pyxel.mouse_y in enemy_list.y:
                    magia = Spell("Bola de Fogo")
                    magia.x = self.x + self.w*4
                    magia.y = self.y
                    magia.casted = True
                    self.casting = True
                    pyxel.blt(self.x + self.w*4, self.y, 0, 16, 32, 8, 8, colkey = 0)
                
                    
    
p1 = Player("Dude", 120, 100, "Guerreiro")
dragao = NPC("Dragao", 20, 100, "Dragao")

personagens = [p1,dragao]
ordem_turno = [p1,dragao]

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw_menu():
    pyxel.cls(0)
    pyxel.mouse(visible=True)
    pyxel.bltm(0, 0, 0, 0, 0, var.TELA_LARGURA, var.TELA_ALTURA)
    desenha_menu()
    dragao.update()    
    p1.delineate()
    p1.update()
    p1.cast_spell(NPC)
    ordem_combate(ordem_turno)
    #pyxel.text(pyxel.mouse_x + 1, pyxel.mouse_y, p1.nome, 7)
    #
    if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) and p1.selected == True:
        p1.selected = False
    if pyxel.mouse_x in range(p1.x - p1.h + 1 , p1.x + p1.h - 1) and pyxel.mouse_y in range(p1.y - p1.w + 1, p1.y + p1.w - 1):
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and p1.selected == False:
            p1.selected = True
            
        pyxel.text(pyxel.mouse_x + 10, pyxel.mouse_y + 10, p1.nome, 7)
    

pyxel.run(update, draw_menu)