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
        self.ataque = "Fogo"
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
        self.habilidades = var.MONSTROS_HABILIDADES[nome]
        MON.append(self)
    def draw(self):
        pyxel.blt(self.x, self.y, self.img, self.u, self.v, self.w, self.h, var.TRANSPARENTE, scale=1.5)    
        
        
        
class Player(Character):
    def __init__(self, nome, classe, x, y):
        super().__init__(nome, x, y)
        self.classe = classe
        self.w = var.CHAR_W
        self.h = var.CHAR_H
        self.x = 35
        self.y = 200
        self.maxlife *= self.atributos["Con"]
        self.currentlife = self.maxlife
        self.contador = 0
        self.exp = 0
        self.level = 1
        self.statmult = var.CLASSES["multiplier"][classe]
        self.alvoid = 100
        self.iniciativa = 1 * self.atributos["Dex"]
        self.nomundo = True
        self.movendo = False
    def draw(self):
        if self.is_alive == True:
            if self.contador <= 8:
                pyxel.blt(self.x, self.y, 0, 0, 0, self.w, self.h, colkey = var.TRANSPARENTE, scale = 1.5)
                self.contador += 1
            elif self.contador < 16:
                pyxel.blt(self.x, self.y, 0, 8, 0, self.w, 
                          self.h, colkey = var.TRANSPARENTE, scale = 1.5)
                self.contador += 1
            elif self.contador >= 16:
                pyxel.blt(self.x, self.y, 0, 8, 0, self.w, 
                          self.h, colkey = var.TRANSPARENTE, scale = 1.5)
                self.contador = 0   
        
    def levelup(self):
        for atributo, stats in zip(self.atributos, self.statmult):
            self.atributos[atributo] += stats
        self.maxlife += 100*self.statmult[2]
        self.level += 1
    
    def update(self):
        if self.currentlife <= 0:
            self.is_alive = False
        if self.nomundo:
            self.update_mundo()
        else:
            self.update_combate()
    
    def update_mundo(self, icones, fase):
        if not self.movendo:
            if icones[fase].emcima:
                if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                    self.movendo = True
        elif self.movendo:
            self.move(icones[fase].x, icones[fase].y)
        
    def update_combate(self):
        pass    
    
    def move(self, x, y):
        if self.x == x and self.y == y:
            self.movendo = False
        else:
            self.x = x
            self.y = y
            self.nomundo = False

    
class Seta:
    def __init__(self):
        self.x = var.MENU_COMBATE_I[1] - 10
        self.y = var.MENU_COMBATE_I[0]
        self.blt = [2, 48, 202 ,7, 10]
        self.pos = 0
        self.selalvo = False
    
    def update(self):
        if self.selalvo:
            self.move_setaalvo()
        else:            
            self.move_seta()
    
    def draw(self):
        pyxel.blt(self.x, self.y, self.blt[0], self.blt[1], self.blt[2], 
                  self.blt[3], self.blt[4], colkey= var.TRANSPARENTE)
        
    def reset(self):
        self.__init__()
      
    def move_setaalvo(self, alvos = MON):        
        if len(MON) == 0:
            return
        if len(MON) == 1:
            self.x = MON[0].x - 10
            self.y = MON[0].y - (MON[0].h/2)
            return
        if pyxel.btn(pyxel.KEY_DOWN):
            if self.pos < (len(MON) - 1):
                self.x = MON[self.pos+1].x - 10
                self.y = MON[self.pos+1].y - round((MON[1].h/2))
                self.pos += 1
            elif self.pos == (len(MON) - 1):
                self.x = MON[0].x - 5
                self.y = MON[0].y - (MON[1].h/2)
                self.pos = 0
        if pyxel.btn(pyxel.KEY_UP):
            if self.pos == 0:
                self.x = MON[len(MON) - 1].x - 10
                self.y = MON[len(MON) - 1].y - round((MON[1].h/2))
                self.pos = len(MON) - 1
            elif self.pos < (len(MON) - 1):
                self.x = MON[self.pos - 1].x - 10
                self.y = MON[self.pos - 1].y - round((MON[1].h/2))
                self.pos -= 1
                
        #if pyxel.btn    
        pass
        
    
    def move_seta(self):
        if pyxel.btn(pyxel.KEY_UP):
            if self.pos == 2:
                self.pos = 0
                self.x = var.MENU_COMBATE_I[1] - 10
                self.y = var.MENU_COMBATE_I[0]
            elif self.pos == 3:
                self.pos = 1
                self.x = var.MENU_COMBATE_III[1] - 10
                self.y = var.MENU_COMBATE_III[0]
        elif pyxel.btn(pyxel.KEY_DOWN):
            if self.pos == 0:
                self.pos = 2
                self.x = var.MENU_COMBATE_II[1] - 10
                self.y = var.MENU_COMBATE_II[0]
            elif self.pos == 1:
                self.pos = 3
                self.x = var.MENU_COMBATE_IV[1] - 10
                self.y = var.MENU_COMBATE_IV[0]
        elif pyxel.btn(pyxel.KEY_LEFT):
            if self.pos == 1:
                self.pos = 0
                self.x = var.MENU_COMBATE_I[1] - 10
                self.y = var.MENU_COMBATE_I[0]
            elif self.pos == 3:
                self.pos = 2
                self.x = var.MENU_COMBATE_II[1] - 10
                self.y = var.MENU_COMBATE_II[0]
        elif pyxel.btn(pyxel.KEY_RIGHT):
            if self.pos == 0:
                self.pos = 1
                self.x = var.MENU_COMBATE_III[1] - 10
                self.y = var.MENU_COMBATE_III[0]
            elif self.pos == 2:
                self.pos = 3
                self.x = var.MENU_COMBATE_IV[1] - 10
                self.y = var.MENU_COMBATE_IV[0]

         
        
        
        
class Menu_combate:
    def __init__(self):
        self.x = var.MENU_COMBATE_BORDA_XI
        self.y = var.MENU_COMBATE_BORDA_Y
        self.fase = 0
        self.indice = 0
        self.comando = 0
        
    def update(self, seta):
        if self.comando == 0:
            if pyxel.btn(pyxel.KEY_ESCAPE):
                self.indice = 0
            elif seta.pos == 0 and pyxel.btnp(pyxel.KEY_RETURN):
                if self.indice == 0:
                    self.indice = 1
                elif self.indice == 1:
                    self.indice = 4
                    self.comando = 1
                elif self.indice == 2:
                    self.indice = 4
                    self.comando = 2
            elif seta.pos == 2 and pyxel.btnp(pyxel.KEY_RETURN):
                if self.indice == 0:
                    self.indice = 2
                    seta.pos = 0
                    seta.x = var.MENU_COMBATE_I[1] - 10
                    seta.y = var.MENU_COMBATE_I[0]
        else:   
            return

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
    
    def reset(self):
        self.__init__()
    
    def desenha_MP(self):        
        desenha_letras(var.MENU_COMBATE_I, "Atacar", 2)
        desenha_letras(var.MENU_COMBATE_II, "Skills", 2)
        desenha_letras(var.MENU_COMBATE_III, "Itens", 2)
        desenha_letras(var.MENU_COMBATE_IV, "Fugir", 2)
    def desenha_MS(self):
        desenha_letras(var.MENU_COMBATE_I, "Fogo", 2)
    def desenha_MA(self):        
        desenha_letras(var.MENU_COMBATE_I, "Estocada", 2)
    

class Icone:
    def __init__(self, nome):
        self.nome = nome
        self.x = var.ICONES[nome][0]
        self.y = var.ICONES[nome][1]
        self.img = var.ICONES[nome][2]
        self.u = var.ICONES[nome][3]
        self.v = var.ICONES[nome][4]
        self.larg = var.ICONES[nome][5]
        self.alt = var.ICONES[nome][6]
        self.back = var.ICONES[nome][7]
        self.emcima = False
    
    def update(self):
        mx = pyxel.mouse_x
        my = pyxel.mouse_y
        dentro_horizontal = self.x <= mx <= self.x + self.larg # Verifica a coordenada x do mouse usando a coordenada x do objeto como ref.
        dentro_vertical = self.y <= my <= self.y + self.alt #Verifica agora as coordenadas do eixo y.
        self.emcima = dentro_horizontal and dentro_vertical

    def draw(self):
        pyxel.blt(self.x, self.y, self.img, self.u, self.v, self.larg, self.alt, self.back)
        if 26 <= pyxel.mouse_x <= 26 + 10 and 152 <= pyxel.mouse_y <= 152 + 8:
            pyxel.blt(26, 152, 2, 84, 203, 10, 8, 0)
        if 34 <= pyxel.mouse_x <= 34 + 10 and 48 <= pyxel.mouse_y <= 48 + 8:
            pyxel.blt(34, 48, 2, 96, 203, 10, 8, 0)
                
class Jogo:
    def __init__(self):
        pyxel.init(var.TELA_LARGURA, var.TELA_ALTURA, title="Gaudério Fantasy", fps = 30, quit_key = pyxel.KEY_Q)
        self.scene = var.TELA_MENU
        #self.background = Background()
        self.player = Player("Gauderio", "Guerreiro", 120, 80)
        self.monstro = MON
        self.menu_combate = Menu_combate()
        self.icones = self.gera_icones()
        self.seta = Seta()
        self.combate_fase = 0
        self.jogo_fase = 0
        self.timer = Temporizador()
        self.atacando = False
        self.lvlup = False
        pyxel.mouse(True)
        pyxel.load("mygame.pyxres")
        pyxel.run(self.update, self.draw)        
        
        
    def draw(self):
        pyxel.cls(0)
        if self.scene == var.TELA_MENU:
            self.desenha_menu()
        elif self.scene == var.TELA_MUNDO:
            self.desenha_mundo()
        elif self.scene == var.TELA_COMBATE:
            self.desenha_combate()
        elif self.scene == var.TELA_MORTE:
            self.desenha_tela_morte()
        elif self.scene == var.TELA_VITORIA:
            self.desenha_tela_vitoria()         
    
    def desenha_menu(self):
        desenha_letras(var.MENU_INICIAL_TITULO, "Gauderios Fantasy", 1)
        desenha_letras(var.MENU_INICIAL_NOVOJG, "Novo Jogo", 1)
        desenha_letras(var.MENU_INICIAL_SAIR, "Sair", 1)
        self.delinea()
        
    def desenha_mundo(self):
        pyxel.bltm(0, 0, 0, 192, 0, var.TELA_LARGURA, var.TELA_ALTURA)
        desenha_letras([20,0], "Turno " + str(len(TURNO)), 2)
        self.desenha_icones()
        self.player.draw()
        
    def desenha_combate(self):     
        pyxel.bltm(0, 0, 0, 480, 0, var.TELA_LARGURA, var.TELA_ALTURA)        
        if self.player.ehturno == False or self.timer.atual() <= 0:
            self.player.draw()
        desenha_criaturas(MON)
        self.menu_combate.draw()
        desenha_letras([30,0], "vida " + str(self.monstro[0].currentlife), 2)
        
        if isinstance(TURNO[0], Player):
            self.seta.draw()
            if self.atacando == True:
                if self.player.ataque == "Estocada Jogador":
                    self.player.x -= 16 
                    desenha_letras([10,0], self.player.nome + " Usa Estocada", 2)
                    Habilidade(self.player.ataque).draw_skill(self.timer.atual(), self.player)                    
                    self.player.x += 16
                else:
                    self.player.draw()
                    desenha_letras([10,0], self.player.nome + " Usa " + self.player.ataque, 2)
                    Habilidade(self.player.ataque).draw_skill(self.timer.atual(), self.acha_monstro())  
            else:
                self.player.draw()
        elif isinstance(TURNO[0], Npc) and TURNO[0].ehturno == True and self.atacando == True:
            desenha_letras([10,0], TURNO[0].nome + str() + " usa " + TURNO[0].ataque , 2)
            if TURNO[0].ataque == "Estocada Monstro":
                Habilidade(TURNO[0].ataque).draw_skill(self.timer.atual(), TURNO[0])
            else:
                Habilidade(TURNO[0].ataque).draw_skill(self.timer.atual(), self.player)
    
    def desenha_tela_morte(self):
        desenha_letras([80,50], "GAME OVER", 2)
        pyxel.blt(70, 95, 0, 16, 128, 16, 13)
        desenha_letras([80,100], "PRESSIONE Q PARA SAIR", 2)
        desenha_letras([80,120], "PRESSIONE ENTER PARA VOLTAR AO INICIO", 2)
    
    def desenha_tela_vitoria(self):
        if self.jogo_fase == 3:
            desenha_letras([60,50], "VITORIA", 2)
            desenha_letras([60,30], "ACABOU O JOGO VAZA DAQUI", 2)
        else:
            desenha_letras([60,50], "VITORIA", 2)
            desenha_letras([70,30], "EXP GANHA: 100", 2)        
            if self.lvlup:
                desenha_letras([90,30], self.player.nome, 2)
                desenha_letras([100,20], "Ganhou um Level", 2)
                desenha_letras([110,30], self.player.nome, 2)
                desenha_letras([120,10], " Agora esta level: " + str(self.player.level), 2)
        
        
    def desenha_icones(self):
        for icone in self.icones:
            icone.draw()    
        
    def update(self):
        #self.background.update()
        pyxel.mouse(True)
        if self.scene == var.TELA_MENU:
            self.update_menu()
        elif self.scene == var.TELA_MUNDO:
            self.seta = Seta()
            self.update_mundo()
        elif self.scene == var.TELA_COMBATE:
            pyxel.mouse(False)
            self.update_combate()
        elif self.scene == var.TELA_MORTE:
            self.update_tela_morte()
        elif self.scene == var.TELA_VITORIA:
            self.update_tela_vitoria()
   
    def update_menu(self):
        if pyxel.mouse_x in var.RANGE_NOVOJGX and pyxel.mouse_y in var.RANGE_NOVOJGY:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnp(pyxel.KEY_RETURN):
                self.reset()
                self.scene = var.TELA_MUNDO
        elif pyxel.mouse_x in var.RANGE_SAIRX and pyxel.mouse_y in var.RANGE_SAIRY:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnp(pyxel.KEY_RETURN):
                pyxel.quit()
    
    def clicou_monstro(self):
        if self.icones[self.jogo_fase].emcima:
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and self.player.nomundo:
                return True
    
    def update_mundo(self):
       #self.player.update_mundo(self.icones, self.jogo_fase)
       self.update_icones()
       if self.clicou_monstro():
           self.player.nomundo == False           
           self.gera_monstros()
           self.define_iniciativa()
           self.player.x = 120
           self.player.y = 80
           self.jogo_fase += 1
           self.scene = var.TELA_COMBATE
       elif self.jogo_fase == var.FIM:
           self.scene = var.TELA_VITORIA
       else:
           return
    def update_icones(self):
        for icone in self.icones:
            icone.update()
    
    # def update_monstros(self):
    #     for monstro in self.monstro:
    #         monstro.update()
    
    def update_combate(self):
        if self.combate_fase == 1:   
            cleanup_monstros(self.monstro)
            self.update_turnos()
            if self.player.is_alive == False:
                self.scene = var.TELA_MORTE
            if len(self.monstro) == 0:
                self.update_exp()
                TURNO.pop(0)
                self.scene = var.TELA_VITORIA
        
        elif self.combate_fase == 2:
            self.scene = var.TELA_MUNDO   
    
    def update_turnos(self):          
        if TURNO[0] == self.player:
            self.player.ehturno = True
            self.update_turno_jogador()
        elif isinstance(TURNO[0], Npc):
            TURNO[0].ehturno = True
            self.update_turno_monstro(TURNO[0])   
    
    def update_turno_jogador(self):
        self.seta.update()       
        self.menu_combate.update(self.seta)                
        if self.menu_combate.comando in [1,2] and not self.seta.selalvo:
            self.seta.x = self.monstro[0].x - 10
            self.seta.y = self.monstro[0].y - (self.monstro[0].h/2)
            self.seta.selalvo = True
            self.seta.pos = 0
            self.timer.inicia(10)
        elif self.timer.acabou():
            if not self.atacando:
                if pyxel.btnp(pyxel.KEY_RETURN) and self.menu_combate.indice == 4:
                    self.seta.selalvo = False
                    if self.menu_combate.comando == 1:                        
                        self.player.ataque = "Estocada Jogador"
                    elif self.menu_combate.comando == 2:
                        self.player.ataque = "Fogo"
                    self.player.alvoid = MON[self.seta.pos].referencia
                    self.atacando = True
                    self.menu_combate.reset()
                    self.timer.inicia(40)                    
            elif self.atacando:
                self.player.attack(Habilidade(self.player.ataque), self.acha_monstro())
                self.player.ehturno = False
                self.atacando = False
                TURNO.pop(0)
                TURNO.append(self.player)
                self.seta.reset()
                self.menu_combate.reset()
                self.timer.inicia(40)
        
    
    def update_turno_monstro(self, monstro):
        if self.atacando == False:            
            monstro.ataque = self.define_monstro_ataque(monstro)
            self.atacando = True
        if self.timer.acabou() and self.atacando:            
            monstro.attack(Habilidade(monstro.ataque), self.player)            
            monstro.ehturno = False
            TURNO.pop(0)
            TURNO.append(monstro)
            self.atacando = False
            self.timer.inicia(40)
    
    def update_tela_morte(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_RETURN):
            self.restart()
            self.scene = var.TELA_MENU
            
    def update_tela_vitoria(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            if self.jogo_fase < 3:
                self.lvlup = False
                self.reset()
                self.player.x = self.icones[self.jogo_fase].x
                self.player.y = self.icones[self.jogo_fase].y
                self.player.nomundo = True
                self.scene = var.TELA_MUNDO
            else:
                self.restart()
                self.scene = var.TELA_MENU
            
        elif pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()    
            
    def update_exp(self):
        self.player.exp += 100
        if self.player.exp >= 150:
            self.player.exp -= 150
            self.lvlup = True
            self.player.levelup()
            self.player.currentlife = self.player.maxlife
    
    def trocou_indice(self, indice):
        return not self.menu_combate.indice == indice
    
    def define_monstro_ataque(self, monstro):
        return monstro.habilidades[pyxel.rndi(0, 1)] # retorna uma habilidade aleatória
    
    def define_iniciativa(self):
        if self.player.iniciativa > self.monstro[0].iniciativa:
            TURNO.append(self.player)
            for monstro in self.monstro:
                TURNO.append(monstro)
        else:            
            for monstro in self.monstro:
                TURNO.append(monstro)        
            TURNO.append(self.player)
        self.combate_fase = 1
        self.timer.inicia(40)    
    
    def gera_monstros(self):
        if self.jogo_fase == 0:
            Npc("Goblin", var.MONSTROS_POS["1"][0], var.MONSTROS_POS["1"][1], 0)
        elif self.jogo_fase == 1:
            for i in range (0,3):
                Npc("Morcego", var.MONSTROS_POS["3"][i][0], var.MONSTROS_POS["3"][i][1], i)
        elif self.jogo_fase == 2:
            Npc("Dragao", var.MONSTROS_POS["1"][0], var.MONSTROS_POS["1"][1], 0)
        self.monstro = MON
        MON.sort(key = lambda m: (m.x, m.y))
    
    def restart(self):
        self.scene = var.TELA_MENU
        #self.background = Background()
        self.player = Player("Gauderio", "Guerreiro")
        self.monstro = MON
        self.menu_combate = Menu_combate()
        self.icones = self.gera_icones()
        self.seta = Seta()
        self.combate_fase = 0
        self.jogo_fase = 0
        self.timer = Temporizador()
        self.atacando = False
        self.lvlup = False
    
    def reset(self):
        self.player.ehturno = False
        self.player.is_alive = True
        self.player.ataque = "Estocada Jogador"
        self.menu_combate = Menu_combate()
        self.seta = Seta()
        self.combate_fase = 0
        self.timer = Temporizador()
        self.monstro = MON
        self.atacando = False        
    
            
    def gera_icones(self):
        icn = []
        for icone in var.ICONES:
            icn.append(Icone(icone))
        return icn        
    def acha_monstro(self):
        for monstro in self.monstro:
            if monstro.referencia == self.player.alvoid:
                return monstro
        
    def delinea(self):
        if pyxel.mouse_x in var.RANGE_NOVOJGX and pyxel.mouse_y in var.RANGE_NOVOJGY:
            pyxel.rectb(var.MENU_INICIAL_NOVOJG[1] - 2, var.MENU_INICIAL_NOVOJG[0] - 2,
                        var.TAMANHO_NOVOJG[0], var.TAMANHO_NOVOJG[1], 7)
        elif pyxel.mouse_x in var.RANGE_SAIRX and pyxel.mouse_y in var.RANGE_SAIRY:
            pyxel.rectb(var.MENU_INICIAL_SAIR[1] - 2, var.MENU_INICIAL_SAIR[0] - 2, 
                        var.TAMANHO_SAIR[0], var.TAMANHO_SAIR[1], 7)
        
        
        
        
        
        
        
Jogo()
        
        
        
        
        
        
        
        
        
        
        
        
        
        