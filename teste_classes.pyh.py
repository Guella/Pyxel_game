# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 17:53:14 2025

@author: salma
"""
import pyxel
# import sys
# sys.path.append("C:/Users/salma/Documents/FURG/Algoritmos/Pyxel_game/")
# sys.path.append("G:/Outros computadores/Meu computador/FURG/Algoritmos/Pyxel_game")
import variaveis as var

#PER = []
MON = []
TURNO = []

TELA_LARGURA = 160
TELA_ALTURA = 220
TELA_MENU = 0
TELA_MUNDO = 1
TELA_COMBATE = 2
TELA_MORTE = 3
TRANSPARENTE = 0

FASE_COMBATE = [0]

MENU_POS_Y = 80
MENU_POS_X = TELA_LARGURA - 110
TITULO_POS_Y = 20
TITULO_POS_X = TELA_LARGURA - 140

MENU_COMBATE_I = [var.MENU_COMBATE_BORDA_Y + 8, var.MENU_COMBATE_BORDA_XI + 30] # esquerda cima
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

SETA = [2, 48, 202 ,7, 9]

MONSTROS = {
    "Rato": [0, 131, 17, 10, 12, TRANSPARENTE],
    "Goblin": [0, 131, 36, 9, 11, TRANSPARENTE],
    "Bezouro": [0, 129, 81 , 13, 13, TRANSPARENTE],
    "Dragao": [0, 192, 128, 16, 16, TRANSPARENTE]
    }

MONSTROS_STATS = {
    "Dragao": {"For": 10,
               "Int": 20,
               "Con": 30,
               "Dex": 20
              },
    "Rato": 
        {
            "For": 3,
            "Int": 1,
            "Con": 1,
            "Dex": 6
        }
    }

PLAYER_STATS = {
    "For": 10,
    "Int": 2,
    "Con": 15,
    "Dex": 10
    }

HABILIDADES = {
    "Fogo": { 
        "tipo": "elemental",
        "dano": 100,
        "atributo": "Int"
        },
    "Estocada": {
        "tipo": "fisico",
        "dano": 30,
        "atributo": "For"
        },
    }

ANIMACAO_HABS = {
    "Fogo": {
        "1": [0, 112, 72, 16, 16, TRANSPARENTE],
        "2": [0, 96, 72, 16, 16, TRANSPARENTE],
        "3": [0, 80, 72, 16, 16, TRANSPARENTE]
        },
    "Estocada":
        {
        "1": [0, 40, 0, -16, 8, TRANSPARENTE],
        "2": [0, 0, 168, -16, 8, TRANSPARENTE],
        "3": [0, 0, 176, -16, 8, TRANSPARENTE]
        }
    }

ANIMACAO_PARADO = {
    "1": [0, 0, 0, 8, 8, TRANSPARENTE], 
    "2": [0, 8, 0, 8, 8, TRANSPARENTE]
    }


def update_monstros(monstros):
    for monstro in monstros:
        monstros.update()
        
def desenha_monstros(monstros):
    for monstro in monstros:
        monstros.draw()
        
def cleanup_monstros(monstros):
    for i in range(len(monstros) - 1, -1, -1):
        if not monstros[i].is_alive:
            del monstros[i]

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
        self.tipo = HABILIDADES[nome]["tipo"]
        self.dano = HABILIDADES[nome]["dano"]
        self.atributo = HABILIDADES[nome]["atributo"]
        self.animacao = ANIMACAO_HABS[nome]
    
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
        
        
class Seta:
    def __init__(self):
        self.x = MENU_COMBATE_I[1] - 10
        self.y = MENU_COMBATE_I[0]
        self.blt = [2, 48, 202 ,7, 10]
        self.pos = 0
    
    def update(self):
        self.move_seta()
    def draw(self):
        pyxel.blt(self.x, self.y, self.blt[0], self.blt[1], self.blt[2], self.blt[3], self.blt[4], colkey= TRANSPARENTE)
    def move_seta(self):
        if pyxel.btn(pyxel.KEY_UP):
            if self.pos == 2:
                self.pos = 0
                self.x = MENU_COMBATE_I[1] - 10
                self.y = MENU_COMBATE_I[0]
            elif self.pos == 3:
                self.pos = 1
                self.x = MENU_COMBATE_III[1] - 10
                self.y = MENU_COMBATE_III[0]
        elif pyxel.btn(pyxel.KEY_DOWN):
            if self.pos == 0:
                self.pos = 2
                self.x = MENU_COMBATE_II[1] - 10
                self.y = MENU_COMBATE_II[0]
            elif self.pos == 1:
                self.pos = 3
                self.x = MENU_COMBATE_IV[1] - 10
                self.y = MENU_COMBATE_IV[0]
        elif pyxel.btn(pyxel.KEY_LEFT):
            if self.pos == 1:
                self.pos = 0
                self.x = MENU_COMBATE_I[1] - 10
                self.y = MENU_COMBATE_I[0]
            elif self.pos == 3:
                self.pos = 2
                self.x = MENU_COMBATE_II[1] - 10
                self.y = MENU_COMBATE_II[0]
        elif pyxel.btn(pyxel.KEY_RIGHT):
            if self.pos == 0:
                self.pos = 1
                self.x = MENU_COMBATE_III[1] - 10
                self.y = MENU_COMBATE_III[0]
            elif self.pos == 2:
                self.pos = 3
                self.x = MENU_COMBATE_IV[1] - 10
                self.y = MENU_COMBATE_IV[0]

            
class Character:
    def __init__(self, nome, x, y, iniciativa):
        self.nome = nome
        self.x = x
        self.y = y
        self.ehturno = False
        self.is_alive = True
        self.maxlife = 100
        self.atributos = PLAYER_STATS
        self.iniciativa = 1
    def update(self):
        if self.currentlife <= 0:
            self.is_alive = False
    def attack(self, skill, alvo):
        alvo.currentlife -= (skill.dano + (self.atributos[skill.atributo] * skill.dano)/10)
        pass
        
            
class Player(Character):
    def __init__(self, nome, x, y, classe, iniciativa, w = var.CHARACTER_W, h = var.CHARACTER_H):
        super().__init__(nome, x, y, iniciativa)
        self.classe = classe
        self.w = w
        self.h = h
        self.atributos = PLAYER_STATS
        self.maxlife *= self.atributos["Con"]
        self.currentlife = self.maxlife
        self.contador = 0
        #PER.append(self)    
        pass
    def draw(self):
        if self.is_alive == True:
            if self.contador <= 5:
                pyxel.blt(self.x, self.y, 0, 0, 0, self.w, self.h, colkey = TRANSPARENTE, scale = 1.5)
                self.contador += 1
            elif self.contador < 10:
                pyxel.blt(self.x, self.y, 0, 8, 0, self.w, self.h, colkey = TRANSPARENTE, scale = 1.5)
                self.contador += 1
            elif self.contador >= 10:
                pyxel.blt(self.x, self.y, 0, 8, 0, self.w, self.h, colkey = TRANSPARENTE, scale = 1.5)
                self.contador = 0
        if self.is_alive == False:
            pyxel.blt(self.x, self.y, 0, 0, 0, self.w, self.h, colkey = TRANSPARENTE, scale = 1.5, rotate = 0.5)
            
class Npc(Character):
    def __init__(self, nome, x, y, iniciativa):
        super().__init__(nome, x, y, iniciativa)
        self.img = MONSTROS[nome][0]
        self.u = MONSTROS[nome][1]
        self.v = MONSTROS[nome][2]
        self.w = MONSTROS[nome][3]
        self.h = MONSTROS[nome][4]
        self.maxlife *= MONSTROS_STATS[nome]["Con"]
        self.currentlife = self.maxlife
        MON.append(self)
        
    def draw(self):
        pyxel.blt(self.x, self.y, self.img, self.u, self.v, self.w, self.h, TRANSPARENTE, scale=1.5)

class Menu_combate:
    def __init__(self):
        self.x = var.MENU_COMBATE_BORDA_XI
        self.y = var.MENU_COMBATE_BORDA_Y
        self.fase = FASE_COMBATE[0]
        self.indice = 0
        self.comando = 0
    def update(self):
        pass
    
    def draw(self):
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
        desenha_letras(MENU_COMBATE_I, "Fogo", 2)
        desenha_letras(MENU_COMBATE_IV, "Estocada", 2)
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            self.indice = 0
        pass
        
        
class Jogo:
    def __init__(self):
        pyxel.init(TELA_LARGURA, TELA_ALTURA, title="Gaudério Fantasy", fps = 30, quit_key = pyxel.KEY_Q)
        self.scene = TELA_MENU
        #self.background = Background()
        self.player = Player("Bozo", 120, 80, "Guerreiro", 0)
        self.monstro = Npc("Dragao", 30, 80, 10)
        self.menu_combate = Menu_combate()
        self.seta = Seta()
        self.combate_fase = 0
        self.timer = Temporizador()
        self.atacando = False
        pyxel.mouse(True)
        pyxel.load("mygame.pyxres")
        pyxel.run(self.update, self.draw)
        
    def draw(self):
        pyxel.cls(0)
        if self.scene == TELA_MENU:
            self.desenha_menu()
        # elif self.scene == TELA_MUNDO:
        #     self.update_mundo()
        elif self.scene == TELA_COMBATE:
            self.desenha_combate()
        elif self.scene == TELA_MORTE:
            self.desenha_tela_morte()
             
    def update(self):
        #self.background.update()
        if self.scene == TELA_MENU:
            self.seta = Seta()
            self.player.is_alive = True
            self.update_menu()
        elif self.scene == TELA_MUNDO:
            self.update_mundo()
        elif self.scene == TELA_COMBATE:
            self.update_combate()
        elif self.scene == TELA_MORTE:
            self.update_tela_morte()
    
    
    def reset(self):
        self.player = Player("Bozo", 120, 80, "Guerreiro", 0)
        self.player.ehturno = False
        self.monstro = Npc("Rato", 30, 80, 10)
        self.monstro.ehturno = False
        self.menu_combate = Menu_combate()
        self.seta = Seta()
        self.combate_fase = 0
        self.timer = Temporizador()
        self.atacando = False
    
    def desenha_menu(self):
        desenha_letras(MENU_INICIAL_TITULO, "Gauderios Fantasy", 1)
        desenha_letras(MENU_INICIAL_NOVOJG, "Novo Jogo", 1)
        desenha_letras(MENU_INICIAL_SAIR, "Sair", 1)
        self.delinea()
    
    def delinea(self):
        if pyxel.mouse_x in RANGE_NOVOJGX and pyxel.mouse_y in RANGE_NOVOJGY:
            pyxel.rectb(MENU_INICIAL_NOVOJG[1] - 2, MENU_INICIAL_NOVOJG[0] - 2,
                        TAMANHO_NOVOJG[0], TAMANHO_NOVOJG[1], 7)
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnp(pyxel.KEY_RETURN):
                self.reset()
                self.scene = TELA_COMBATE
        elif pyxel.mouse_x in RANGE_SAIRX and pyxel.mouse_y in RANGE_SAIRY:
            pyxel.rectb(MENU_INICIAL_SAIR[1] - 2, MENU_INICIAL_SAIR[0] - 2, 
                        TAMANHO_SAIR[0], TAMANHO_SAIR[1], 7)
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnp(pyxel.KEY_RETURN):
                pyxel.quit()
    
    
            
    def desenha_combate(self):             
        if self.player.ehturno == False or self.timer.atual() <= 0:
            self.player.draw()
        self.monstro.draw()
        self.menu_combate.draw()
        #desenha_letras([10,0], str(pyxel.frame_count), 2)
        desenha_letras([20,0], "A Vida do Jogador é: " + str(self.player.currentlife), 2)
        desenha_letras([30,0], "A Vida do Monstro é: " + str(self.monstro.currentlife), 2)
        desenha_letras([40,0], "Turno: " + str(TURNO[0]), 2)
        #desenha_letras([20,0], str(self.timer.ativo), 2)
        
        #desenha_letras([10,0], str(self.timer.framefinal) + "   " + str(pyxel.frame_count) + str(self.timer.acabou()) + str(TURNO[0]) + str(self.player.currentlife), 2)
        if self.player.ehturno == True:
            self.seta.draw()
            if self.atacando == True:
                self.player.x -= 16 
                Habilidade("Estocada").draw_skill(self.timer.atual(), self.player)
                self.player.x += 16
        if self.monstro.ehturno == True and self.atacando == True:
            desenha_letras([10,0], self.monstro.nome + " usa Fogo" , 2)
            Habilidade("Fogo").draw_skill(self.timer.atual(), self.player)
        #self.checa_turno()
    
    def desenha_tela_morte(self):
        desenha_letras([80,50], "GAME OVER", 2)
        pyxel.blt(70, 95, 0, 16, 128, 16, 13)
        
    def update_tela_morte(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_RETURN):
            self.scene = TELA_MENU
    def update_menu(self):
        pass
        #self.desenha_menu()
    
    def update_menu_combate(self):
        # if pyxel.btn(pyxel.KEY_A):
        #     self.player.ehturno = True
        # elif pyxel.btn(pyxel.KEY_B):
        #     self.player.ehturno = False
        if self.seta.pos == 0 and self.player.ehturno == True:
            if pyxel.btn(pyxel.KEY_RETURN):
                self.menu_combate.indice = 2
        elif self.menu_combate.indice == 2:
            if pyxel.btn(pyxel.KEY_ESCAPE):
                self.menu_combate.indice = 0
        elif self.seta.pos == 3 and self.player.ehturno == True:
            if pyxel.btn(pyxel.KEY_RETURN):
                self.scene = TELA_MENU                
                self.player.ehturno == False
                return
        if self.menu_combate.indice == 2 and self.seta.pos == 3 and self.atacando == False:
            if pyxel.btn(pyxel.KEY_RETURN):
                self.timer.inicia(40)
                self.atacando = True
    
    def update_turno_jogador(self):
        self.seta.update()
        self.update_menu_combate()        
        if self.timer.acabou() and self.atacando:
            self.player.attack(Habilidade("Estocada"), self.monstro)
            self.player.ehturno = False
            self.atacando = False
            TURNO.pop(0)
            TURNO.append(self.player.nome)
            self.timer.inicia(40)
        # if not self.timer.acabou():
        #     return
        
    def update_turno_monstro(self):
        if self.timer.acabou() and self.atacando:
            self.monstro.attack(Habilidade("Fogo"), self.player)
            self.monstro.ehturno = False
            TURNO.pop(0)
            TURNO.append(self.monstro.nome)
            self.atacando = False
            self.timer.inicia(40)
        if not self.timer.acabou():
            return
              
            
            
    
    def update_turnos(self):
        if self.timer.acabou():            
            if TURNO[0] == self.player.nome:
                self.player.ehturno = True
                self.update_turno_jogador()
            else:
                self.monstro.ehturno = True
                self.atacando = True
                self.update_turno_monstro()

            
    
    def define_iniciativa(self):
        TURNO.append(self.monstro.nome)
        TURNO.append(self.player.nome)
        self.timer.inicia(40)              
        self.combate_fase = 1
        
        
    def update_combate(self):
        if self.combate_fase == 0:
            self.define_iniciativa()
        
        elif self.combate_fase == 1:             
            self.update_turnos()           
        
        elif self.combate_fase == 2:
            self.scene = TELA_MENU
        
        
        if self.player.currentlife <= 0:
            self.player.is_alive = False
        if self.player.is_alive == False:
            self.scene = TELA_MORTE
                
        #self.menu_combate.desenha()
        #pyxel.quit()
        
    def update_mundo(self):
        pyxel.quit()
        
    # def checa_turno(self):
    #     if self.player.ehturno == False:
    #         pyxel.quit()
    
    
    
Jogo()   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    