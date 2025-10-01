# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 17:53:14 2025

@author: salma
"""
import pyxel
import sys
sys.path.append("C:/Users/salma/Documents/FURG/Algoritmos/Pyxel/")
sys.path.append("G:/Outros computadores/Meu computador/FURG/Algoritmos/Pyxel")
import variaveis as var
#from .variaveis import * as var


TITULO = "Gauderio's Gate"

pyxel.init(var.TELA_LARGURA, var.TELA_ALTURA)
pyxel.load("mygame.pyxres")

class Cursor:
    pass


def desenha_menu():
    pyxel.rect(0, var.MENU_COMBATE_BORDA_Y, var.MENU_COMBATE_BORDA_XF, var.TELA_ALTURA, col = 1)

def define_iniciativa(lista_personagens):
    return sorted(lista_personagens, key = lambda personagem: personagem.iniciativa)        
    pass
        
def ordem_combate(lista_personagens):
    pyxel.blt(var.TURNO_X, var.TURNO_Y, 0, 0, 0, 8, 8, scale = 3)
    pyxel.blt(var.TURNO_X + 18, var.TURNO_Y, 0, var.MONSTRO_DESENHO["Dragao"][0], var.MONSTRO_DESENHO["Dragao"][1], var.MONSTRO_DESENHO["Dragao"][2],
              var.MONSTRO_DESENHO["Dragao"][3], scale = 2)
    pass

def desenha_monstro(x,y,nome):
    pyxel.blt(x, y, 0, var.MONSTRO_DESENHO[nome][0], var.MONSTRO_DESENHO[nome][1], var.MONSTRO_DESENHO[nome][2], var.MONSTRO_DESENHO[nome][3],
              scale = var.MONSTRO_DESENHO[nome][4])

def draw_chacter(x,y):
    pyxel.blt(x, y, 0, 0, 0, 8, 8, scale = 4)
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
            pyxel.circb(self.x - self.w * 2 + 2, self.y - self.h * 2 + 2, self.movimento * 20, 12)
    def delineate(self):
        if self.selected == True:
            pyxel.rectb(self.x - self.w * 2 + 2, self.y - self.h * 2 + 2, self.w * 4 + 4, self.h * 4 + 4, 7)
    def update(self):
        draw_chacter(self.x, self.y)
        self.desenha_area_mov()
        if self.selected == True and self.movendo == False:
            if not (pyxel.mouse_x in range(self.x - (self.h * 4 - 1) , self.x + (self.h * 4)) and pyxel.mouse_y in range(self.y - (self.w * 4 - 1), self.y + (self.w * 4))):
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
                    pyxel.blt(self.x + self.w*4, self.y, 0, 16, 32, 8, 8, scale = 4)
                
                    
    
p1 = Player("Dude", 150, 150, "Guerreiro")
dragao = NPC("Dragao", 400, 150, "Dragao")

personagens = [p1,dragao]
ordem_turno = [p1,dragao]

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw_menu():
    pyxel.cls(0)
    pyxel.mouse(visible=True)
    pyxel.bltm(var.TELA_LARGURA/3 + 83, var.TELA_ALTURA/3 + 10, 0, 0, 0, 340, 168, scale= 4)
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
    if pyxel.mouse_x in range(p1.x - (p1.h * 4 - 1) , p1.x + (p1.h * 4)) and pyxel.mouse_y in range(p1.y - (p1.w * 4 - 1), p1.y + (p1.w * 4)):
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and p1.selected == False:
            p1.selected = True
            
        pyxel.text(pyxel.mouse_x + 10, pyxel.mouse_y + 10, p1.nome, 7)
    

pyxel.run(update, draw_menu)