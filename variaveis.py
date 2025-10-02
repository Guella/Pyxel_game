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

MENU_POS_Y = TELA_ALTURA*2/3
MENU_POS_X = TELA_LARGURA/2
TITULO_POS_Y = TELA_ALTURA/4
TITULO_POS_X = TELA_LARGURA/2.3
TURNO_X = TELA_LARGURA/3
TURNO_Y = 20

MENU_COMBATE_BORDA_XI = 0
MENU_COMBATE_BORDA_XF = TELA_LARGURA
MENU_COMBATE_BORDA_Y = TELA_ALTURA - 60

DANO_TIPO = {"Fisico", "magico", "elemental"}



PERSONAGEM_CLASSE_MULT = {"Guerreiro": [5,3,1,0,1,1,5,1,1]}
PERSONAGEM_CLASSE_LVL = {"Guerreiro": [200,10,5,0,1,1,4,1,2]}

MONSTRO_TIPO_MULT = {"Dragao": [10,5,3,10,3,1,20,30,25]}

MONSTRO_TIPO_SKILLS = {"Dragao": ["Bola de Fogo", "Ataque com Garra", "Voar"]}
MONSTRO_DESENHO = {"Dragao": [192,128, 16, 16, 4]}


teste = {k: v * MONSTRO_TIPO_MULT["Dragao"][i] for i, (k, v) in enumerate(ATRIBUTOS_BASE.items())}