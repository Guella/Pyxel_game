# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 12:29:07 2025

@author: salma
"""
import pandas as pd
import numpy as np


##### atributos base


ATRIBUTOS_BASE = {"VIDA": 100,
"ARMADURA": 10,
"RESISTENCIA_MAGICA": 10,
"MANA": 10,
"MOV": 4,
"INICIATIVA": 1,
"FOR": 1,
"INT": 1,
"DEX": 1}

HABILIDADES = pd.DataFrame(np.array([[20,"elemental_fogo",5, 10, 2]]), columns = ["dano", "dano_tipo", "area", "alcance", "cd"], index = ["Bola de Fogo"])


CHARACTER_W = 8
CHARACTER_H = 8

TELA_LARGURA = 160
TELA_ALTURA = 220
TELA_MENU = 0
TELA_MUNDO = 1
TELA_COMBATE = 2

MENU_POS_Y = TELA_ALTURA*2/3
MENU_POS_X = TELA_LARGURA/2
TITULO_POS_Y = TELA_ALTURA/4
TITULO_POS_X = TELA_LARGURA/2.3
TURNO_X = TELA_LARGURA/3
TURNO_Y = 20

MENU_COMBATE_BORDA_XI = 0
MENU_COMBATE_BORDA_XF = TELA_LARGURA
MENU_COMBATE_BORDA_Y = TELA_ALTURA - 40

DANO_TIPO = {"Fisico", "magico", "elemental"}

ICONES = {
#    "Caverna_Entrada":[26, 152, 2, 84, 203, 10, 8, 0],
#    "Caverna_Saída": [34, 48, 2, 96, 203, 10, 8, 0],
    "Portão": [112, 16, 0, 56, 120, 8, 8, 0],
    "Guardião Espectro": [110, 38, 0, 177, 97, 14, 15, 0]}
    

PERSONAGEM_CLASSE_MULT = {"Guerreiro": [5,3,1,0,1,1,5,1,1]}
PERSONAGEM_CLASSE_LVL = {"Guerreiro": [200,10,5,0,1,1,4,1,2]}

MONSTRO_TIPO_MULT = {"Dragao": [10,5,3,10,3,1,20,30,25]}

MONSTRO_TIPO_SKILLS = {"Dragao": ["Bola de Fogo", "Ataque com Garra", "Voar"]}
MONSTRO_DESENHO = {"Dragao": [192,128, 16, 16, 4]}

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
