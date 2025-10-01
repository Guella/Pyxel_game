# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 14:13:46 2025

@author: salma
"""

import pyxel


GAME_NAME = "A Odisséia do Gaudério // Aventuras de Outrora // Memórias dos Pampas // Memórias/Aventuras de um Gaudério"
BASE_LIFE = 100




class Character:
    def __init__(self, name):
        self.x = 10
        self.name = name
        
        
class Playable_Character(Character):
    def __init__(self, name, classe):
        super().__init__(name)
        self.life = 11
        self.classe = classe
        
        def level_up():
            self.life = self.life            
            
            
class NPC_Chacter(Character):
    def __init__(self):
        self.x = 12
        
        
player = Playable_Character("Jhon", "Guerreiro")

player.name
player.classe