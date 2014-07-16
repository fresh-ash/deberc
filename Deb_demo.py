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
		for i in self.m_cards.sort():
			for j in range(4):
				if i[0] == 12 and i[1] == trump and (i+1) < self.m_cards.len() and (i+1)[0] == 13 and (i+1)[1] == trump:
					self.bella = True
				

class Diller():
	"""Класс диллер, который может генерировать колоду и раздавать карты в различных играх"""
	cards = []
	trump = None
	talon = None
	def coloda(self, start):
		"""Генерирует колоду карт для соответствующей игры"""
		for i in range(start, 15):
			for j in range(4):
				self.cards.append([i,j])
		return (self.cards) 

	def deberc_dill(self, cards, g1, g2, g3, g4):
		"""Раздача карт в "Деберц" """
		g1.dill = True
		for i in range(6):
			g1.m_cards.append(cards.pop(cards.index(choice(cards))))
			g2.m_cards.append(cards.pop(cards.index(choice(cards))))    #КРИВО, но работает!
			g3.m_cards.append(cards.pop(cards.index(choice(cards))))    #Запилить все в функцию и вызывать для каждого
			g4.m_cards.append(cards.pop(cards.index(choice(cards))))    #игрока?!
		self.talon =  cards.pop(cards.index(choice(cards)))                      
		self.trump = self.talon[1]                                                              #Карта прикупа и козырь!
		
	def deberc_combination(self, gamer):
		pass
	
			
a = Gamer()
b = Gamer()		
c = Gamer()
d = Gamer()

dill = Diller()
dill.deberc_dill(dill.coloda(7), a, b, c, d)

print (a)

