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

TELA_LARGURA = 160
TELA_ALTURA = 220
TELA_MENU = 0
TELA_MUNDO = 1
TELA_COMBATE = 2
TRANSPARENTE = 0

FASE_COMBATE = [0]

MENU_POS_Y = 80
MENU_POS_X = TELA_LARGURA - 110
TITULO_POS_Y = 20
TITULO_POS_X = TELA_LARGURA - 140

MENU_COMBATE_I = [var.MENU_COMBATE_BORDA_Y + 8, var.MENU_COMBATE_BORDA_XI + 30]
MENU_COMBATE_II = [MENU_COMBATE_I[0] + 15, MENU_COMBATE_I[1]]
MENU_COMBATE_III = [MENU_COMBATE_I[0], MENU_COMBATE_I[1] + 60]
MENU_COMBATE_IV = [MENU_COMBATE_I[0] + 15, MENU_COMBATE_I[1] + 60]

MENU_INICIAL_TITULO = [TITULO_POS_Y, TITULO_POS_X]
MENU_INICIAL_NOVOJG = [MENU_POS_Y, MENU_POS_X]
MENU_INICIAL_SAIR = [MENU_INICIAL_NOVOJG[0] + 20 ,MENU_INICIAL_NOVOJG[1] + 20]


TAMANHO_NOVOJG = [ 65,  13]
TAMANHO_SAIR = [28,  13]

RANGE_NOVOJGX = range(MENU_INICIAL_NOVOJG[1], MENU_INICIAL_NOVOJG[1] + TAMANHO_NOVOJG[0])
RANGE_NOVOJGY = range(MENU_INICIAL_NOVOJG[0], MENU_INICIAL_NOVOJG[0] + TAMANHO_NOVOJG[1])
RANGE_SAIRX = range(MENU_INICIAL_SAIR[1], MENU_INICIAL_SAIR[1] + TAMANHO_SAIR[0])
RANGE_SAIRY = range(MENU_INICIAL_SAIR[0], MENU_INICIAL_SAIR[0] + TAMANHO_SAIR[1])

MENU_LETRAS = {
	"A": [0, 5, 6, 9],
	"B": [12, 5, 6, 9],
	"C": [24, 5, 6, 9],
	"D": [36, 5, 6, 9],
	"E": [48, 5, 6, 9],
	"F": [60, 5, 6, 9],
	"G": [72, 5, 7, 9],
	"H": [84, 5, 6, 9],
	"I": [96, 5, 6, 9],
	"J": [108, 5, 7, 10],
	"K": [120, 5, 6, 9],
	"L": [132, 5, 6, 9],
	"M": [144, 5, 9, 9],
	"N": [0, 41, 6, 9],
	"O": [12, 41, 6, 9],
	"P": [24, 41, 6, 9],
	"Q": [36, 41, 6, 9],
	"R": [48, 41, 6, 9],
	"S": [60, 41, 7, 10],
	"T": [72, 41, 6, 9],
	"U": [84, 41, 6, 9],
	"V": [96, 41, 9, 9],
	"W": [108, 41, 9, 9],
	"X": [120, 41, 6, 9],
	"Y": [132, 41, 6, 9],
	"Z": [144, 41, 6, 9],
	"a": [0, 24, 8, 6],
	"b": [12, 24, 8, 9],
	"c": [24, 24, 6, 9],
	"d": [36, 24, 8, 10],
	"e": [48, 24, 8, 9],
	"f": [60, 24, 8, 9],
	"g": [72, 26, 8, 10],
	"h": [84, 24, 8, 9],
	"i": [96, 24, 4, 9],
	"j": [108, 24, 8, 9],
	"k": [120, 24, 8, 9],
	"l": [132, 24, 5, 9],
	"m": [144, 24, 8, 9],
	"n": [0, 59, 8, 9],
	"o": [12, 59, 8, 9],
	"p": [24, 59, 8, 9],
	"q": [36, 59, 8, 9],
	"r": [48, 59, 6, 9],
	"s": [60, 59, 8, 9],
	"t": [72, 59, 6, 9],
	"u": [84, 59, 8, 9],
	"v": [96, 59, 7, 9],
	"w": [108, 59, 8, 9],
	"x": [120, 59, 8, 9],
	"y": [132, 59, 8, 9],
	"z": [144, 59, 8, 9]
}



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

def desenha_letras(pos_texto, texto, fig_id, escala = 1):
    pos_y = pos_texto[0]
    pos_x = pos_texto[1]
    for letra in texto:
        if letra == ' ':
            pos_x += 2
        else:
            pyxel.blt(pos_x, pos_y,fig_id, MENU_LETRAS[letra][0], 
                         MENU_LETRAS[letra][1], MENU_LETRAS[letra][2], MENU_LETRAS[letra][3], 0, scale = escala)
            pos_x += MENU_LETRAS[letra][2]

            
class Character:
    def __init__(self, nome, x, y, w, h, iniciativa):
        self.nome = nome
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.ehturno = False
    def update(self):
        pass
    def attack(self):
        pass
    
            
class Player(Character):
    def __init__(self, nome, x, y, classe, iniciativa, w = var.CHARACTER_W, h = var.CHARACTER_H):
        super().__init__(nome, x, y, w, h, iniciativa)
        self.nome = nome
        self.classe = classe
        self.ehturno = False
        PER.append(self)
    def update(self):
        pass
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.w, self.h, colkey = TRANSPARENTE, scale = 2)

class Npc(Character):
    def __init__(self, nome, x, y, classe, iniciativa, w, h):
        super().__init__(nome, x, y, w, h, iniciativa)
        self.nome = nome
        self.newx = x
        self.newy = y
        self.ehturno = False
        MON.append(self)

class Menu_combate:
    def __init__(self):
        self.x = var.MENU_COMBATE_BORDA_XI
        self.y = var.MENU_COMBATE_BORDA_Y
        self.fase = FASE_COMBATE[0]
        self.indice = 0
        self.comando = 0
    def update(self):
        pass
    
    def desenha(self):
        pyxel.bltm(x=0,y=var.MENU_COMBATE_BORDA_Y,tm=0,u=0,v=192,w=160,h=80)
        if self.indice == 0:
            self.desenha_MP()
        elif self.indice == 1:
            self.desenha_MA()
        elif self.indice == 2:
            self.desenha_MS()
        elif self.indice == 3:
            self.desenha_MI()
    
    def desenha_MP(self):        
        desenha_letras(MENU_COMBATE_I, "Atacar", 2)
        desenha_letras(MENU_COMBATE_II, "Skills", 2)
        desenha_letras(MENU_COMBATE_III, "Itens", 2)
        desenha_letras(MENU_COMBATE_IV, "Fugir", 2)
    def desenha_MS(self):
        desenha_letras(MENU_COMBATE_I, "Bola de Fogo", 2)
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            self.indice = 0
        pass
        
        
class Jogo:
    def __init__(self):
        pyxel.init(TELA_LARGURA, TELA_ALTURA, title="Gaudério Fantasy", fps = 30, quit_key = pyxel.KEY_Q)
        self.scene = TELA_MENU
        #self.background = Background()
        self.player = Player("Bozo", 120, 80, "Guerreiro", 0)
        self.menu_combate = Menu_combate()
        pyxel.mouse(True)
        pyxel.load("mygame.pyxres")
        pyxel.run(self.update, self.draw)
        
    def draw(self):
        pyxel.cls(0)
        if self.scene == TELA_MENU:
            self.desenha_menu()
            self.delinea()
        # elif self.scene == TELA_MUNDO:
        #     self.update_mundo()
        elif self.scene == TELA_COMBATE:
            self.update_combate()
    
    def update(self):
        #self.background.update()
        if self.scene == TELA_MENU:
            self.update_menu()
        elif self.scene == TELA_MUNDO:
            self.update_mundo()
        elif self.scene == TELA_COMBATE:
            self.update_combate()
    
    def desenha_menu(self):
        desenha_letras(MENU_INICIAL_TITULO, "Gauderios Fantasy", 1)
        desenha_letras(MENU_INICIAL_NOVOJG, "Novo Jogo", 1)
        desenha_letras(MENU_INICIAL_SAIR, "Sair", 1)
    def delinea(self):
        if pyxel.mouse_x in RANGE_NOVOJGX and pyxel.mouse_y in RANGE_NOVOJGY:
            pyxel.rectb(MENU_INICIAL_NOVOJG[1] - 2, MENU_INICIAL_NOVOJG[0] - 2,
                        TAMANHO_NOVOJG[0], TAMANHO_NOVOJG[1], 7)
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.scene = TELA_COMBATE
        elif pyxel.mouse_x in RANGE_SAIRX and pyxel.mouse_y in RANGE_SAIRY:
            pyxel.rectb(MENU_INICIAL_SAIR[1] - 2, MENU_INICIAL_SAIR[0] - 2, 
                        TAMANHO_SAIR[0], TAMANHO_SAIR[1], 7)
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                pyxel.quit()
                
       

    def update_menu(self):
        self.delinea()
    
    def update_combate(self):        
        self.player.draw()
        self.menu_combate.desenha()
        #pyxel.quit()
        
    def update_mundo(self):
        pyxel.quit()
    
    
    
    
Jogo()   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    