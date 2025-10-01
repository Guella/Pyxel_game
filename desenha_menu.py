# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 13:50:36 2025

@author: salma
"""

import pyxel

TELA_LARGURA = 1280
TELA_ALTURA = 720

TELA_MENU = 0
TELA_MAPA = 1
TELA_COMBATE = 2

MENU_POS_Y = round(TELA_ALTURA/2)
MENU_POS_X = round(TELA_LARGURA/3)
TITULO_POS_Y = round(TELA_ALTURA/4)
TITULO_POS_X = round(TELA_LARGURA/2.3)



TITULO = "Gauderio's Gate"
posicoes_letras_1 = [[0,40,8,10],[12,61,7,7],[96,61,7,7],[12,61,7,7],
                   [108,4,7,10],[12,61,7,7],[72,25,7,10],[12,61,7,7]]
posicoes_letras_2 = [[16,4,7,10],[12,61,7,7],[0,61,7,7],[72,58,7,10],
                     [96,23,4,9],[0,61,7,7],[84,61,8,7],[0,25,9,7],[48,61,6,7]]
posicoes_letras_3 = [[60,40,7,10],[0,25,9,7],[96,23,4,9],[48,61,6,7]]

letras_menu = [posicoes_letras_1,posicoes_letras_2,posicoes_letras_3]

class Menu:
    def __init__(self):
        self.x = MENU_POS_X + 70
        self.y = MENU_POS_Y
        self.y2 = self.y + 50
        self.y3 = self.y2 + 50
        self.xf1 = 0
        self.xf2 = 0
        self.xf3 = 0

    def desenha_menu(self):
        for i in posicoes_letras_1:
            pyxel.blt(self.x, self.y,1, i[0], i[1], i[2], i[3], scale = 4)
            self.x = self.x + i[2]*4
        self.xf1 = self.x
        self.x = MENU_POS_X + 70
        for i in posicoes_letras_2:
            pyxel.blt(self.x, self.y2,1, i[0], i[1], i[2], i[3], scale = 4)
            self.x = self.x + i[2]*4
        self.xf2 = self.x
        self.x = MENU_POS_X + 120
        for i in posicoes_letras_3:
            pyxel.blt(self.x, self.y3,1, i[0], i[1], i[2], i[3], scale = 4)
            self.x = self.x + i[2]*4
        self.xf3 = self.x
        self.x = MENU_POS_X + 80
    def delinea(self):
        if pyxel.mouse_x in range(self.x - 20, self.xf1) and pyxel.mouse_y in range(self.y - 20, self.y + 20):
            pyxel.rectb(self.x - 20, self.y - 20, self.xf1 - (MENU_POS_X + 60), 50, 7)
        elif pyxel.mouse_x in range(self.x - 30, self.xf2) and pyxel.mouse_y in range(self.y2 - 20, self.y2 + 20):
            pyxel.rectb(self.x - 30, self.y2 - 20, self.xf2 - (MENU_POS_X + 50), 50, 7)
        elif pyxel.mouse_x in range(self.x + 20, self.xf3) and pyxel.mouse_y in range(self.y3 - 20, self.y3 + 20):
            pyxel.rectb(self.x + 20, self.y3 - 20, self.xf3 - (MENU_POS_X + 100), 50, 7)
    def update(self):
        self.desenha_menu()
        self.delinea()


def desenha_select(pos):
    pos_x = MENU_POS_X + 80
    pos_y = MENU_POS_Y
    for i in pos:
        pyxel.blt(pos_x, pos_y,1, i[0], i[1], i[2], i[3], scale = 4)
        pos_x = pos_x + i[2]*4





pyxel.init(TELA_LARGURA, TELA_ALTURA)
pyxel.load("my_resource.pyxres")

pyxel.mouse(True)

menu = Menu()

class Cursor:
    pass

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    elif pyxel.mouse_x in range(menu.x + 20, menu.xf3) and pyxel.mouse_y in range(menu.y3 - 20, menu.y3 + 20) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.quit()

def draw_menu():
    pyxel.cls(0)
    pyxel.bltm(TITULO_POS_X, TITULO_POS_Y, 0, 0, 0, 110, 20, scale = 4)
    menu.update()

pyxel.run(update, draw_menu)

#%%






