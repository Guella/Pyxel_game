# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 17:22:15 2025

@author: salma
"""

import pyxel
import variaveis as var

MON = []
TURNO = []

def desenha_criaturas(criaturas):
    for criatura in criaturas:
        criatura.draw()

def cleanup_monstros(monstros):
    for i in range(len(monstros) -1, -1, -1):
        if monstros[i].currentlife <= 0:
            for j in range(len(TURNO) -1, -1, -1):
                if isinstance(TURNO[j], Npc):
                    if TURNO[j].referencia == monstros[i].referencia:
                        TURNO.pop(j)
            del monstros[i]

def desenha_letras(pos_texto, texto, fig_id, escala = 1):
    pos_y = pos_texto[0]
    pos_x = pos_texto[1]
    for letra in texto:
        if letra == ' ':
            pos_x += 4
        else:
            pyxel.blt(pos_x, pos_y,fig_id, var.MENU_LETRAS[letra][0], 
                         var.MENU_LETRAS[letra][1], var.MENU_LETRAS[letra][2], var.MENU_LETRAS[letra][3], 0, scale = escala)
            pos_x += var.MENU_LETRAS[letra][2]

class Temporizador:
    def __init__(self):
        self.framefinal = 0
        self.ativo = False
        
    def inicia(self, frames):
        self.framefinal = pyxel.frame_count + frames
        self.ativo = True
    
    def acabou(self):
        if not self.ativo:
            return True
        if pyxel.frame_count >= self.framefinal:
            self.ativo = False
        return not self.ativo
    def atual(self):
        return self.framefinal - pyxel.frame_count

class Habilidade:
    def __init__(self, nome):
        self.nome = nome
        self.tipo = var.HABILIDADES[nome]["tipo"]
        self.dano = var.HABILIDADES[nome]["dano"]
        self.atributo = var.HABILIDADES[nome]["atributo"]
        self.animacao = var.ANIMACAO_HABS[nome]
    
    def draw_animacao(self, fase, target):
        pyxel.blt(target.x, target.y, self.animacao[fase][0], self.animacao[fase][1], self.animacao[fase][2], 
                  self.animacao[fase][3], self.animacao[fase][4], self.animacao[fase][5], scale=1.5)
    
    def draw_skill(self, timer, target):
        if timer <= 9 or (timer > 22 and timer <= 27):
            self.draw_animacao("1", target)
        elif (timer > 9 and timer <= 13)  or (timer > 17 and timer <= 22):
            self.draw_animacao("2", target)
        elif timer > 13 and timer <= 17:
            self.draw_animacao("3", target)



class Character:            
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y
        self.ehturno = False
        self.is_alive = True
        self.maxlife = 100
        self.atributos = var.PLAYER_STATS
        self.iniciativa = 1
    def attack(self, skill, alvo):
        alvo.currentlife -= (skill.dano + (self.atributos[skill.atributo] * skill.dano)/10)
        pass
      
class Npc(Character):
    def __init__(self,nome, x, y, referencia):
        super().__init__(nome, x, y)
        self.img = var.MONSTROS[self.nome][0]
        self.u = var.MONSTROS[self.nome][1]
        self.v = var.MONSTROS[self.nome][2]
        self.w = var.MONSTROS[self.nome][3]
        self.h = var.MONSTROS[self.nome][4]        
        self.atributos = var.MONSTROS_STATS[nome]
        self.maxlife *= self.atributos["Con"]
        self.currentlife = self.maxlife
        self.referencia = referencia
        self.iniciativa = 1 * self.atributos["Dex"]
        MON.append(self)
    def draw(self):
        pyxel.blt(self.x, self.y, self.img, self.u, self.v, self.w, self.h, var.TRANSPARENTE, scale=1.5)    
        
        
        
class Player(Character):
    def __init__(self, nome, x, y, classe):
        super().__init__(nome, x, y)
        self.classe = classe
        self.w = var.CHAR_W
        self.h = var.CHAR_H
        self.maxlife *= self.atributos["Con"]
        self.currentlife = self.maxlife
        self.contador = 0
        self.exp = 0
        self.level = 1
        self.statmult = var.CLASSES["multiplier"][classe]
        self.alvoid = 100
        self.iniciativa = 1 * self.atributos["Dex"]
    def draw(self):
        if self.is_alive == True:
            if self.contador <= 5:
                pyxel.blt(self.x, self.y, 0, 0, 0, self.w, self.h, colkey = var.TRANSPARENTE, scale = 1.5)
                self.contador += 1
            elif self.contador < 10:
                pyxel.blt(self.x, self.y, 0, 8, 0, self.w, self.h, colkey = var.TRANSPARENTE, scale = 1.5)
                self.contador += 1
            elif self.contador >= 10:
                pyxel.blt(self.x, self.y, 0, 8, 0, self.w, self.h, colkey = var.TRANSPARENTE, scale = 1.5)
                self.contador = 0   
        
    def levelup(self):
        for atributo, stats in zip(self.atributos, self.statmult):
            self.atributos[atributo] += stats
        self.maxlife += 100*self.statmult[2]
        self.level += 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        