import variaveis as var
import pyxel
from variaveis import MENU_LETRAS
from variaveis import ICONES
TELA_LARGURA = 160
TELA_ALTURA = 220
TITULO = "Aventuras de Outrora"


def gera_icones():
    icn = []
    for icone in var.ICONES:
        icn.append(Icone(icone))
    return icn

class Icone:
    def __init__(self, nome):
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
        pyxel.init(TELA_LARGURA, TELA_ALTURA, title='Jogo', fps=60)
        self.icones = gera_icones()
        pyxel.mouse(True)
        pyxel.load('mygame.pyxres')
        pyxel.run(self.update, self.draw)

    def update_icones(self):
        for icone in self.icones:
            icone.update()

    def update(self):
        self.update_icones()


    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 192, 0, TELA_LARGURA, TELA_ALTURA)
        self.draw_icones()

    def draw_icones(self):
        for icone in self.icones:
            icone.draw()
        
Jogo()