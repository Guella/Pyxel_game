# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 12:29:07 2025

@author: salma
"""

##### atributos base

TELA_LARGURA = 160 # largura da tela
TELA_ALTURA = 220 # altura da tela

##### id das telas
TELA_MENU = 0
TELA_MUNDO = 1
TELA_COMBATE = 2
TELA_MORTE = 3
TELA_VITORIA = 4

##### id da cor transparente
TRANSPARENTE = 0


#### tamanho padrão do personagem
CHAR_W = 8
CHAR_H = 8




MENU_POS_Y = TELA_ALTURA*2/3
MENU_POS_X = TELA_LARGURA/2
TITULO_POS_Y = TELA_ALTURA/4
TITULO_POS_X = TELA_LARGURA/2.3
TURNO_X = TELA_LARGURA/3
TURNO_Y = 20

MENU_POS_Y = 80
MENU_POS_X = TELA_LARGURA - 110
TITULO_POS_Y = 20
TITULO_POS_X = TELA_LARGURA - 140

MENU_COMBATE_BORDA_XI = 0
MENU_COMBATE_BORDA_XF = TELA_LARGURA
MENU_COMBATE_BORDA_Y = TELA_ALTURA - 40


MENU_COMBATE_I = [MENU_COMBATE_BORDA_Y + 8,MENU_COMBATE_BORDA_XI + 30] # esquerda cima
MENU_COMBATE_II = [MENU_COMBATE_I[0] + 15, MENU_COMBATE_I[1]] # esquerda baixo
MENU_COMBATE_III = [MENU_COMBATE_I[0], MENU_COMBATE_I[1] + 60] # direita cima
MENU_COMBATE_IV = [MENU_COMBATE_I[0] + 15, MENU_COMBATE_I[1] + 60] # direita baixo

MENU_INICIAL_TITULO = [TITULO_POS_Y, TITULO_POS_X]
MENU_INICIAL_NOVOJG = [MENU_POS_Y, MENU_POS_X]
MENU_INICIAL_SAIR = [MENU_INICIAL_NOVOJG[0] + 20 ,MENU_INICIAL_NOVOJG[1] + 20]


TAMANHO_NOVOJG = [ 65,  13]
TAMANHO_SAIR = [28,  13]

RANGE_NOVOJGX = range(MENU_INICIAL_NOVOJG[1], MENU_INICIAL_NOVOJG[1] + TAMANHO_NOVOJG[0])
RANGE_NOVOJGY = range(MENU_INICIAL_NOVOJG[0], MENU_INICIAL_NOVOJG[0] + TAMANHO_NOVOJG[1])
RANGE_SAIRX = range(MENU_INICIAL_SAIR[1], MENU_INICIAL_SAIR[1] + TAMANHO_SAIR[0])
RANGE_SAIRY = range(MENU_INICIAL_SAIR[0], MENU_INICIAL_SAIR[0] + TAMANHO_SAIR[1])


DANO_TIPO = {"Fisico", "magico", "elemental"}



####### ATRIBUTOS JOGADOR ######

 
PLAYER_STATS = {
    "For": 1000,
    "Int": 2,
    "Con": 15,
    "Dex": 10
    }

##### Multiplicador de atributo por Classe ######

CLASSES = {
    "multiplier": { "Guerreiro": [3,1,4,2]
        }
    }

##### COORDENADAS IDLE ANIMATION #######

ANIMACAO_PARADO = {
    "1": [0, 0, 0, 8, 8, TRANSPARENTE], 
    "2": [0, 8, 0, 8, 8, TRANSPARENTE]
    }


#### COORDENADA DO DESENHO DOS MONSTROS ####

MONSTROS = {
    "Morcego": [0, 193, 70, 14, 6, TRANSPARENTE],
    "Goblin": [0, 131, 36, 9, 11, TRANSPARENTE],
    "Bezouro": [0, 129, 81 , 13, 13, TRANSPARENTE],
    "Dragao": [0, 192, 128, 16, 16, TRANSPARENTE]
    }

MONSTROS_HABILIDADES = {
    "Morcego": ["Arranhar", "Morder"],
    "Goblin": ["Arranhar", "Estocada Monstro"],
    "Dragao": ["Arranhar", "Fogo"],
    "Bezouro": ["Arranhar", "Morder"]
    }

###### Atributo dos Monstros #######

MONSTROS_STATS = {
    "Dragao": 
        {
            "For": 10,
            "Int": 20,
            "Con": 30,
            "Dex": 20,
            "EXP": 100
        },
    "Morcego": 
        {
            "For": 3,
            "Int": 1,
            "Con": 1,
            "Dex": 6,
            "EXP": 10
        },
    "Goblin": 
        {
            "For": 5,
            "Int": 2,
            "Con": 3,
            "Dex": 5,
            "EXP": 30
        },
    "Bezouro": 
        {
            "For": 6,
            "Int": 2,
            "Con": 5,
            "Dex": 8,
            "EXP": 50
        }
    }

######### LISTA HABILIDADES #######

HABILIDADES = {
    "Fogo": { 
        "tipo": "elemental",
        "dano": 100,
        "atributo": "Int"
        },
    "Estocada Monstro": {
        "tipo": "fisico",
        "dano": 30,
        "atributo": "For"
        },
    "Estocada Jogador": {
        "tipo": "fisico",
        "dano": 30,
        "atributo": "For"
        },
    "Arranhar": {
        "tipo": "fisico",
        "dano": 20,
        "atributo": "Dex"
        },
    "Morder": {
        "tipo": "fisico",
        "dano": 25,
        "atributo": "For"
        }
    }


FIM = 10000
##### ANIMACOES HABILIDADES #####


ANIMACAO_HABS = {
    "Fogo": {
        "1": [0, 112, 72, 16, 16, TRANSPARENTE],
        "2": [0, 96, 72, 16, 16, TRANSPARENTE],
        "3": [0, 80, 72, 16, 16, TRANSPARENTE]
        },
    "Estocada Jogador":
        {
        "1": [0, 40, 0, -16, 8, TRANSPARENTE],
        "2": [0, 0, 168, -16, 8, TRANSPARENTE],
        "3": [0, 0, 176, -16, 8, TRANSPARENTE]
        },
    "Estocada Monstro":
        {
        "1": [0, 131, 36, -16, 12, TRANSPARENTE],
        "2": [0, 3, 188, -16, 12, TRANSPARENTE],
        "3": [0, 3, 200, -16, 12, TRANSPARENTE]
        },
    "Morder":
        {
        "1": [0, 131, 36, -16, 12, TRANSPARENTE],
        "2": [0, 3, 188, -16, 12, TRANSPARENTE],
        "3": [0, 3, 200, -16, 12, TRANSPARENTE]
        },
    "Arranhar":
        {
        "1": [0, 131, 36, -16, 12, TRANSPARENTE],
        "2": [0, 3, 188, -16, 12, TRANSPARENTE],
        "3": [0, 3, 200, -16, 12, TRANSPARENTE]
        }
    }


###### ICONES MAPA MUNDI #######

ICONES = {   
    "Goblin": [45, 170, 0, 131, 36, 9, 11, TRANSPARENTE],
    "Caverna_Entrada":[26, 152, 0, 0, 216, 10, 8, TRANSPARENTE],
    "Portao": [112, 16, 0, 56, 120, 8, 8, TRANSPARENTE],
    "Guardiao_Espectro": [110, 38, 0, 177, 97, 14, 15, TRANSPARENTE]}


##### coordenada desenho da SETA ######
SETA = [2, 48, 202 ,7, 9]

#### coordenada monstros por quantidade #####

MONSTROS_POS = {
    "1" : [30, 80],
    "2": [[30,60],[30,90]],
    "3": [[30,50],[30,80], [30,110]],
    "4": [[10,50],[10,80],
          [45,50],[45,80]],
    "5": [[10,50],[45,60],
          [10,80],[10,110],
          [45,100]],
    }

##### coordenada letras ######

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
	"a": [0, 24, 8, 7],
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
	"z": [144, 59, 8, 9],
    ":": [12, 203, 4, 9],
    "1": [0, 149, 6, 8],
    "2": [12, 149, 6, 8],
    "3": [24, 149, 6, 8],
    "4": [36, 149, 6, 8],
    "5": [48, 149, 6, 8],
    "6": [60, 149, 6, 8],
    "7": [72, 149, 6, 8],
    "8": [84, 149, 6, 8],
    "9": [96, 149, 6, 8],
    "0": [108, 149, 6, 8],
    "é": [72, 93, 6, 11],
    ".": [12, 186, 4, 7],
    "!": [0, 167, 4, 7],
    "-": [120, 168, 7, 5]
}
