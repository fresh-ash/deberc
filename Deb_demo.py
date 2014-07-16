#!/usr/bin/python3

from itertools import product
from random import choice

class Gamer():
	def __init__(self):
		self.m_cards = []
		self.m_total = 0
		self.m_table = []
		self.dill = False
		self.bella = False
		self.terc = []
		self.poltos = []
		self.deberc = []	
	
	def m_combination(self, trump):
		pass
				

class Diller():
	"""
			Класс диллер, который может генерировать колоду и раздавать карты в
			различных играх
	"""
	def __init__(self):
		self.cards = []
		self.trump = None
		self.talon = None
	
	def coloda(self, start):
		"""Генерирует колоду карт для соответствующей игры"""
		for i in range(start, 15):
			for j in range(4):
				self.cards.append([i,j]) 

	def dill_card(self, g_cards, number):
		for i in range(number):
			g_cards.append(self.cards.pop(self.cards.index(choice(self.cards))))	
	
	def deberc_dill(self, g1, g2, g3, g4):
		"""Раздача карт в "Деберц" """
		self.coloda(7)
		self.dill_card(g1.m_cards, 6)
		self.dill_card(g2.m_cards, 6)
		self.dill_card(g3.m_cards, 6)
		self.dill_card(g4.m_cards, 6)
		self.talon = self.cards.pop(self.cards.index(choice(self.cards)))
		self.trump = self.talon[1]
		
	def deberc_combination(self, gamer):
		pass
	
			
a = Gamer()
b = Gamer()		
c = Gamer()
d = Gamer()

dill = Diller()
dill.deberc_dill(a,b,c,d)
print (a.m_cards)

